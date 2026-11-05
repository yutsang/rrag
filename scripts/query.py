#!/usr/bin/env python3
"""
Query the local RAG index.

Retrieves top-k child chunks, deduplicates them by parent section,
then asks Gemini to answer using the parent text as context.

Usage:
    python scripts/query.py "What is the newsvendor critical ratio?"
    python scripts/query.py "解釋收益管理" --k 8
    python scripts/query.py "A/B testing" --filter page_type=concept
    python scripts/query.py "Little's Law" --filter layer=wiki --no-llm
    python scripts/query.py --interactive

Filters use Chroma's metadata `where` clause. Pass key=value pairs,
comma-separated if you need multiple: --filter page_type=concept,confidence=high
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

try:
    import chromadb
    from dotenv import load_dotenv
    from google import genai
    from google.genai import types as genai_types
except ImportError as e:
    sys.exit(f"Missing dependency ({e}). Run: pip install -r scripts/requirements.txt")

REPO_ROOT = Path(__file__).parent.parent
load_dotenv(REPO_ROOT / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")
EMBED_MODEL = os.getenv("GEMINI_EMBED_MODEL", "gemini-embedding-001")
CHAT_MODEL = os.getenv("GEMINI_CHAT_MODEL", "gemini-2.5-flash")
DB_PATH = os.getenv("CHROMA_DB_PATH", str(REPO_ROOT / "chroma_db"))
COLLECTION = os.getenv("CHROMA_COLLECTION", "rrag-wiki")

if not API_KEY:
    sys.exit("GEMINI_API_KEY is not set. Copy .env.example to .env and add your key.")

SYSTEM_PROMPT = """You are a study assistant for a knowledge wiki covering
course topics (statistics, operations, finance, marketing, blockchain) and AI tooling.

Answer using ONLY the retrieved context below. Cite source page titles when
making claims. If the context does not cover the question, say so clearly
instead of guessing. Prefer concrete formulas and examples from the wiki.

When the user asks in Chinese, answer in Traditional Chinese; otherwise
answer in English.
"""


def parse_filter(expr: str | None) -> dict | None:
    if not expr:
        return None
    clauses = {}
    for part in expr.split(","):
        if "=" not in part:
            continue
        k, v = part.split("=", 1)
        clauses[k.strip()] = v.strip()
    if not clauses:
        return None
    if len(clauses) == 1:
        return clauses  # Chroma accepts {"key": "value"}
    return {"$and": [{k: v} for k, v in clauses.items()]}


def embed_query(client: genai.Client, text: str) -> list[float]:
    resp = client.models.embed_content(
        model=EMBED_MODEL,
        contents=[text],
        config=genai_types.EmbedContentConfig(task_type="RETRIEVAL_QUERY"),
    )
    return resp.embeddings[0].values


def retrieve(coll, client, query: str, k: int, where: dict | None):
    qvec = embed_query(client, query)
    results = coll.query(
        query_embeddings=[qvec],
        n_results=k * 3,  # overfetch, then dedupe by parent
        where=where,
    )
    metas = results["metadatas"][0]
    docs = results["documents"][0]
    dists = results["distances"][0]

    # Dedupe by (source_path, parent_idx); keep best-scoring hit
    seen: dict[tuple, dict] = {}
    for meta, doc, dist in zip(metas, docs, dists):
        key = (meta.get("source_path"), meta.get("parent_idx"))
        if key in seen and seen[key]["distance"] <= dist:
            continue
        seen[key] = {
            "title": meta.get("title") or meta.get("source_path"),
            "source_path": meta.get("source_path"),
            "page_type": meta.get("page_type", ""),
            "layer": meta.get("layer", ""),
            "parent_text": meta.get("parent_text", doc),
            "distance": dist,
        }
    # Sort by distance (lower = better for cosine)
    ranked = sorted(seen.values(), key=lambda x: x["distance"])[:k]
    return ranked


def format_context(hits: list[dict]) -> str:
    blocks = []
    for i, h in enumerate(hits, 1):
        header = f"[{i}] {h['title']}  ({h['source_path']}, layer={h['layer']})"
        blocks.append(f"{header}\n{h['parent_text']}")
    return "\n\n---\n\n".join(blocks)


def generate(client: genai.Client, query: str, context: str) -> str:
    prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"=== Retrieved context ===\n{context}\n\n"
        f"=== User question ===\n{query}\n\n"
        f"Answer:"
    )
    resp = client.models.generate_content(
        model=CHAT_MODEL,
        contents=prompt,
    )
    return resp.text or "(empty response)"


def run_query(coll, client, query: str, k: int, where: dict | None, no_llm: bool):
    hits = retrieve(coll, client, query, k, where)
    if not hits:
        print("(no results)")
        return

    print(f"\n=== Top {len(hits)} sources ===")
    for i, h in enumerate(hits, 1):
        print(f"  [{i}] {h['title']}  —  {h['source_path']}  (dist={h['distance']:.3f})")

    if no_llm:
        print("\n--- Context preview ---")
        print(format_context(hits)[:3000])
        return

    print(f"\n=== Answer ({CHAT_MODEL}) ===")
    answer = generate(client, query, format_context(hits))
    print(answer)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", help="Your question")
    ap.add_argument("--k", type=int, default=5, help="Number of parents to return (default 5)")
    ap.add_argument("--filter", default=None,
                    help="Metadata filter, e.g. 'page_type=concept,layer=wiki'")
    ap.add_argument("--no-llm", action="store_true",
                    help="Only retrieve, skip generation (cheap sanity checks)")
    ap.add_argument("--interactive", "-i", action="store_true", help="Interactive REPL")
    args = ap.parse_args()

    chroma = chromadb.PersistentClient(path=DB_PATH)
    try:
        coll = chroma.get_collection(COLLECTION)
    except Exception:
        sys.exit(f"Collection '{COLLECTION}' not found. Run scripts/build_index.py first.")

    client = genai.Client(api_key=API_KEY)
    where = parse_filter(args.filter)

    if args.interactive:
        print(f"rrag> interactive mode (collection: {COLLECTION}). Ctrl-C to exit.")
        while True:
            try:
                q = input("\nrrag> ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not q:
                continue
            run_query(coll, client, q, args.k, where, args.no_llm)
    else:
        if not args.query:
            ap.error("provide a query or use --interactive")
        run_query(coll, client, args.query, args.k, where, args.no_llm)


if __name__ == "__main__":
    main()
