#!/usr/bin/env python3
"""
Build a local vector index over wiki/ for RAG retrieval.

Methodology (Parent-Child chunking, hand-rolled):
  1. Read wiki/**/*.md directly. Parse YAML frontmatter as the source of
     truth for metadata (title, type, tags, confidence, ...).
  2. Resolve [[wiki-links]] to plain text so embeddings see clean prose.
  3. Split each file into PARENT chunks at `##` headings (≤PARENT_MAX_CHARS),
     greedy-packing oversized sections by paragraph.
  4. Split each parent into CHILD chunks by paragraph (≤CHILD_MAX_CHARS).
     Embed children for precision; return the full parent at query time
     for context.

Stack:
  - Embeddings: Google Gemini (gemini-embedding-001) via google-genai
  - Vector store: ChromaDB (local PersistentClient)
  - Key:         loaded from .env via python-dotenv (gitignored)

Free-tier safety:
  gemini-embedding-001 free tier counts each text in a batch as one request
  against a 100 RPM quota. We pace at ~70 items/min and parse retryDelay
  from any 429 response.

Usage:
    python scripts/build_index.py                  # incremental: skip already-indexed chunks
    python scripts/build_index.py --include-raw    # also index raw_converted/
    python scripts/build_index.py --reset          # wipe collection first
    python scripts/build_index.py --metadata-only  # update metadata, no embedding
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

try:
    import yaml
    import chromadb
    from dotenv import load_dotenv
    from google import genai
    from google.genai import types as genai_types
except ImportError as e:
    sys.exit(f"Missing dependency ({e}). Run: pip install -r scripts/requirements.txt")

REPO_ROOT = Path(__file__).parent.parent
WIKI_ROOT = REPO_ROOT / "wiki"
RAW_CONVERTED = REPO_ROOT / "raw_converted"

# Wiki subdirectories that contain knowledge content
WIKI_INCLUDE_DIRS = ["concepts", "sources", "entities", "analyses", "mocs"]
# Skip these — navigation only, not knowledge
WIKI_SKIP_NAMES = {"index.md", "log.md"}
# overview.md is included as a top-level file

# Chunk sizing — tuned for this wiki's section lengths
PARENT_MAX_CHARS = 2500
CHILD_MAX_CHARS = 1200
CHILD_MIN_CHARS = 150

# Free-tier rate limiting for gemini-embedding-001
EMBED_BATCH = 15
EMBED_SLEEP_SECONDS = 13  # ~70 items/min, well below the 100 RPM cap

# ----- Config -----
load_dotenv(REPO_ROOT / ".env")
API_KEY = os.getenv("GEMINI_API_KEY")
EMBED_MODEL = os.getenv("GEMINI_EMBED_MODEL", "gemini-embedding-001")
DB_PATH = os.getenv("CHROMA_DB_PATH", str(REPO_ROOT / "chroma_db"))
COLLECTION = os.getenv("CHROMA_COLLECTION", "rrag-wiki")


# ----- Frontmatter + wiki-link cleaning -----
def parse_frontmatter(content: str) -> tuple[dict, str]:
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, parts[2].lstrip()


def resolve_wiki_links(text: str) -> str:
    """[[target|display]] -> display; [[page-name]] -> Title Case."""
    # Piped form: keep the display text
    text = re.sub(r"\[\[[^\]]*\|([^\]]+)\]\]", r"\1", text)

    # Bare form: kebab-case -> Title Case (strip path + .md)
    def kebab_to_title(m: re.Match) -> str:
        target = m.group(1)
        name = target.split("/")[-1].replace(".md", "")
        return name.replace("-", " ").title()

    return re.sub(r"\[\[([^\]|]+)\]\]", kebab_to_title, text)


def clean_body(body: str) -> str:
    body = resolve_wiki_links(body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


# ----- Chunking -----
def split_parents(body: str) -> list[str]:
    sections = re.split(r"(?=^##\s)", body, flags=re.MULTILINE)
    sections = [s.strip() for s in sections if s.strip()]
    if not sections:
        sections = [body.strip()]
    parents: list[str] = []
    for sec in sections:
        if len(sec) <= PARENT_MAX_CHARS:
            parents.append(sec)
            continue
        buf = ""
        for para in sec.split("\n\n"):
            if len(buf) + len(para) + 2 > PARENT_MAX_CHARS and buf:
                parents.append(buf.strip())
                buf = para
            else:
                buf = f"{buf}\n\n{para}" if buf else para
        if buf.strip():
            parents.append(buf.strip())
    return parents


def split_children(parent_text: str) -> list[str]:
    paras = [p.strip() for p in parent_text.split("\n\n") if p.strip()]
    children: list[str] = []
    buf = ""
    for p in paras:
        if len(p) > CHILD_MAX_CHARS:
            if buf:
                children.append(buf.strip())
                buf = ""
            for i in range(0, len(p), CHILD_MAX_CHARS):
                children.append(p[i : i + CHILD_MAX_CHARS].strip())
            continue
        if len(buf) + len(p) + 2 > CHILD_MAX_CHARS and buf:
            children.append(buf.strip())
            buf = p
        else:
            buf = f"{buf}\n\n{p}" if buf else p
    if buf.strip():
        children.append(buf.strip())
    return [c for c in children if len(c) >= CHILD_MIN_CHARS]


# ----- Metadata + IDs -----
def build_metadata(fm: dict, source_path: Path, layer: str) -> dict:
    rel = str(source_path.relative_to(REPO_ROOT))
    meta: dict = {
        "source_path": rel,
        "layer": layer,  # 'wiki' (curated) or 'raw' (converted lecture material)
    }
    title = fm.get("title") or source_path.stem.replace("-", " ").title()
    meta["title"] = str(title)

    for key in ("full_name", "author", "date_published", "confidence", "source"):
        if key in fm and fm[key] is not None:
            meta[key] = str(fm[key])
    if "type" in fm:
        meta["page_type"] = str(fm["type"])
    if isinstance(fm.get("tags"), list):
        meta["tags"] = ", ".join(str(t) for t in fm["tags"])

    parts = Path(rel).parts
    # Wiki layer: rel = wiki/<category>/...
    if layer == "wiki" and len(parts) >= 2 and parts[0] == "wiki":
        if len(parts) >= 3:
            meta["category"] = parts[1]
            if parts[1] == "sources" and len(parts) >= 4:
                meta["source_type"] = parts[2]  # courses / mcp / claude-code / ...
        else:
            meta["category"] = "root"  # overview.md
    # Raw layer: rel = raw_converted/<source_type>/...
    elif layer == "raw" and len(parts) >= 2 and parts[0] == "raw_converted":
        meta["category"] = "raw_source"
        if len(parts) >= 3:
            meta["source_type"] = parts[1]
    return meta


def chunk_id(source_path: str, parent_idx: int, child_idx: int) -> str:
    h = hashlib.sha1(f"{source_path}:{parent_idx}:{child_idx}".encode()).hexdigest()[:16]
    return h


# ----- File collection -----
def collect_wiki_files() -> list[Path]:
    files: list[Path] = []
    for sub in WIKI_INCLUDE_DIRS:
        d = WIKI_ROOT / sub
        if d.exists():
            files.extend(sorted(d.rglob("*.md")))
    overview = WIKI_ROOT / "overview.md"
    if overview.exists():
        files.append(overview)
    return [f for f in files if f.name not in WIKI_SKIP_NAMES]


def collect_raw_files() -> list[Path]:
    if not RAW_CONVERTED.exists():
        return []
    return sorted(RAW_CONVERTED.rglob("*.md"))


# ----- Embedding -----
def _parse_retry_delay(err_str: str) -> int:
    m = re.search(r"retry in ([\d.]+)s", err_str)
    if m:
        return int(float(m.group(1))) + 2
    m = re.search(r"'retryDelay':\s*'(\d+)s'", err_str)
    if m:
        return int(m.group(1)) + 2
    return 0


def embed_batch(client: genai.Client, texts: list[str]) -> list[list[float]]:
    for attempt in range(6):
        try:
            resp = client.models.embed_content(
                model=EMBED_MODEL,
                contents=texts,
                config=genai_types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT"),
            )
            return [e.values for e in resp.embeddings]
        except Exception as e:
            wait = _parse_retry_delay(str(e)) or min(60, 5 * (2 ** attempt))
            print(f"    rate-limited; sleeping {wait}s before retry {attempt + 1}/6")
            time.sleep(wait)
    raise RuntimeError("embedding failed after 6 retries")


# ----- Main -----
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--include-raw", action="store_true",
                    help="Also index raw_converted/ as a 'raw' layer")
    ap.add_argument("--reset", action="store_true",
                    help="Delete and recreate the collection before indexing")
    ap.add_argument("--metadata-only", action="store_true",
                    help="Update metadata on existing chunks; skip re-embedding")
    ap.add_argument("--force-reembed", action="store_true",
                    help="Re-embed even chunks that already exist (default: skip them)")
    args = ap.parse_args()

    if not API_KEY and not args.metadata_only:
        sys.exit("GEMINI_API_KEY is not set. Copy .env.example to .env and add your key.")

    files: list[tuple[Path, str]] = [(f, "wiki") for f in collect_wiki_files()]
    if args.include_raw:
        files += [(f, "raw") for f in collect_raw_files()]

    if not files:
        sys.exit("No files to index.")
    print(f"Indexing {len(files)} files "
          f"(wiki={sum(1 for _, l in files if l == 'wiki')}, "
          f"raw={sum(1 for _, l in files if l == 'raw')})")

    chroma = chromadb.PersistentClient(path=DB_PATH)
    if args.reset and not args.metadata_only:
        try:
            chroma.delete_collection(COLLECTION)
            print(f"Deleted existing collection '{COLLECTION}'")
        except Exception:
            pass
    coll = chroma.get_or_create_collection(
        name=COLLECTION,
        metadata={"hnsw:space": "cosine"},
    )

    # Build all chunks first
    all_ids: list[str] = []
    all_docs: list[str] = []
    all_metas: list[dict] = []

    for path, layer in files:
        content = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(content)
        body = clean_body(body)
        if not body:
            continue
        base_meta = build_metadata(fm, path, layer)

        parents = split_parents(body)
        for p_idx, parent_text in enumerate(parents):
            children = split_children(parent_text)
            for c_idx, child_text in enumerate(children):
                cid = chunk_id(base_meta["source_path"], p_idx, c_idx)
                meta = dict(base_meta)
                meta["parent_idx"] = p_idx
                meta["child_idx"] = c_idx
                meta["parent_text"] = parent_text
                all_ids.append(cid)
                all_docs.append(child_text)
                all_metas.append(meta)

    if args.metadata_only:
        print(f"Refreshing metadata on {len(all_ids)} chunks (no embedding calls)...")
        UPDATE_BATCH = 200
        for start in range(0, len(all_ids), UPDATE_BATCH):
            end = min(start + UPDATE_BATCH, len(all_ids))
            try:
                coll.update(ids=all_ids[start:end], metadatas=all_metas[start:end])
            except Exception as e:
                print(f"  warning: update batch {start}-{end} failed ({e})")
            print(f"  updated {end}/{len(all_ids)}")
        print(f"\n✓ Metadata refreshed. {len(all_ids)} chunks in '{COLLECTION}'")
        return

    # Incremental: skip chunks already indexed (free-tier friendly)
    existing_ids: set[str] = set()
    if not args.force_reembed:
        try:
            existing = coll.get(ids=all_ids)
            existing_ids = set(existing.get("ids") or [])
            if existing_ids:
                print(f"Skipping {len(existing_ids)} chunks already in the index")
        except Exception:
            pass

    todo = [
        (i, d, m) for i, d, m in zip(all_ids, all_docs, all_metas)
        if i not in existing_ids
    ]
    if not todo:
        print("Nothing to embed. Index is up-to-date.")
        return

    todo_ids = [t[0] for t in todo]
    todo_docs = [t[1] for t in todo]
    todo_metas = [t[2] for t in todo]

    total = len(todo)
    eta_min = (total / EMBED_BATCH) * EMBED_SLEEP_SECONDS / 60
    print(f"Embedding {total} new chunks via {EMBED_MODEL}.")
    print(f"Pacing at ~{int(EMBED_BATCH * 60 / EMBED_SLEEP_SECONDS)} items/min "
          f"(free tier safe). ETA ~{eta_min:.1f} min.")

    genai_client = genai.Client(api_key=API_KEY)
    for start in range(0, total, EMBED_BATCH):
        end = min(start + EMBED_BATCH, total)
        embeds = embed_batch(genai_client, todo_docs[start:end])
        coll.upsert(
            ids=todo_ids[start:end],
            documents=todo_docs[start:end],
            embeddings=embeds,
            metadatas=todo_metas[start:end],
        )
        print(f"  upserted {end}/{total}")
        if end < total:
            time.sleep(EMBED_SLEEP_SECONDS)

    manifest = {
        "embed_model": EMBED_MODEL,
        "collection": COLLECTION,
        "db_path": DB_PATH,
        "total_chunks_indexed_now": total,
        "total_files": len(files),
    }
    Path(DB_PATH).mkdir(parents=True, exist_ok=True)
    (Path(DB_PATH) / "build_manifest.json").write_text(json.dumps(manifest, indent=2))
    print(f"\n✓ Index built. Embedded {total} new chunks into '{COLLECTION}' at {DB_PATH}")


if __name__ == "__main__":
    main()
