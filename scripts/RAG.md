# RAG Pipeline

A self-contained, local, free RAG pipeline over `wiki/`. Three Python scripts,
one local SQLite-backed vector store, and the free Google Gemini API.
No external services. No staging directories. Your API key never leaves the
machine.

---

## Architecture

```
wiki/**/*.md  ──────────────────┐
                                 │
raw/**/*.{pdf,pptx,docx}         │
   │                             │
   └─convert_raw.py (markitdown)─┤
                                 │
       raw_converted/**/*.md ────┤
                                 │
                                 ▼
                        build_index.py
                  ┌──────────────┴──────────────┐
                  │  1. Parse YAML frontmatter  │
                  │  2. Resolve [[wiki-links]]  │
                  │  3. Parent-Child chunking   │
                  │  4. Gemini embedding        │
                  └──────────────┬──────────────┘
                                 ▼
                       ChromaDB (chroma_db/)
                                 │
                                 ▼
                            query.py
                                 │
                                 ▼
                       Gemini 2.5 Flash answer
```

Three scripts, three responsibilities:

| Script | Role |
|---|---|
| `convert_raw.py` | (Optional) PDF/PPTX/DOCX → markdown via Microsoft markitdown |
| `build_index.py` | Walk `wiki/` directly, chunk, embed, store in ChromaDB |
| `query.py` | Retrieve + generate answer with citations |

There is no intermediate "export" or "staging" directory. The build script
reads `wiki/concepts/`, `wiki/sources/`, `wiki/entities/`, `wiki/analyses/`,
`wiki/mocs/`, and `wiki/overview.md` directly. Frontmatter is the source of
truth for metadata. `[[wiki-links]]` are resolved inline before embedding.

---

## Why markitdown is here

Microsoft's [markitdown](https://github.com/microsoft/markitdown) converts
PDF / PPTX / DOCX / XLSX / HTML / EPUB into LLM-friendly markdown. Two uses
in this repo:

1. **Bootstrapping wiki pages.** When ingesting a new lecture deck, run
   `convert_raw.py` first so the authoring agent reads clean markdown
   instead of parsing raw PDF text. Faster and more accurate, especially
   for slides where bullets and tables matter.
2. **Deep-layer RAG grounding.** When you ask a question the wiki summarizes
   but doesn't quote verbatim, run `build_index.py --include-raw` to also
   index `raw_converted/`. Use `--filter layer=raw` at query time to pull
   directly from the converted slides.

Caveats: markitdown's PDF extraction can mangle math-heavy slides. Manual
review is sometimes needed for time-series and statistics decks.

---

## One-time setup

### 1. Install dependencies

```bash
pip install -r scripts/requirements.txt
```

Installs `markitdown[all]`, `google-genai`, `chromadb`, `python-dotenv`,
`pyyaml`.

### 2. Get a free Gemini API key

<https://aistudio.google.com/apikey> — free tier covers this corpus easily.

### 3. Store the key locally

```bash
cp .env.example .env
# Edit .env, paste your key into GEMINI_API_KEY
```

`.env` is gitignored. The scripts load it from the repo root via
`python-dotenv`. The key never leaves your machine — Gemini API calls go
directly from your laptop to `generativelanguage.googleapis.com`.

---

## Running the pipeline

### Stage 1 — (Optional) Convert raw sources

```bash
python scripts/convert_raw.py                    # all of raw/
python scripts/convert_raw.py --dir raw/courses  # just one subdir
python scripts/convert_raw.py --force            # re-convert everything
```

Skips files whose output is newer than the source. Mirrors the `raw/` tree
under `raw_converted/`. Skip this stage if you only want to index the
curated wiki.

### Stage 2 — Build the vector index

```bash
python scripts/build_index.py                  # incremental, wiki only
python scripts/build_index.py --include-raw    # also raw_converted/
python scripts/build_index.py --reset          # wipe collection first
python scripts/build_index.py --metadata-only  # update metadata, no API spend
python scripts/build_index.py --force-reembed  # ignore existing chunks
```

What it does:

1. Walks `wiki/{concepts,sources,entities,analyses,mocs}/**/*.md` plus
   `wiki/overview.md`. Skips `index.md` and `log.md` (navigation only).
2. Parses YAML frontmatter for each file → `title`, `page_type`, `tags`,
   `confidence`, `category`, `source_type` metadata.
3. Resolves `[[target|display]]` and `[[bare-link]]` inline so embeddings
   see clean prose.
4. **Parent chunks** at `##` headings, ≤2500 chars (oversized sections
   greedy-pack by paragraph).
5. **Child chunks** by paragraph, ≤1200 chars, drop fragments under 150 chars.
6. Embeds each child via `gemini-embedding-001` with
   `task_type=RETRIEVAL_DOCUMENT`.
7. Upserts to ChromaDB at `./chroma_db/`. Each chunk's metadata holds the
   full **parent text** so query results return whole sections, not
   fragments.

**Stable IDs**: chunk ID = `sha1(wiki_path:parent_idx:child_idx)`. Re-running
the build only embeds chunks that don't already exist — incremental updates
are nearly free.

### Stage 3 — Query

```bash
# One-shot
python scripts/query.py "Explain the newsvendor critical ratio"

# Interactive REPL
python scripts/query.py --interactive

# Metadata-filtered
python scripts/query.py "A/B testing" --filter page_type=concept
python scripts/query.py "bitcoin"     --filter source_type=courses
python scripts/query.py "Little's Law" --filter category=concepts,confidence=high

# Retrieval only, no LLM call
python scripts/query.py "queueing theory" --no-llm

# Traditional Chinese works — embeddings are multilingual
python scripts/query.py "收益管理如何用報童模型計算保護座位?"
```

### How retrieval works

1. The query is embedded with `task_type=RETRIEVAL_QUERY` (asymmetric to
   document embeddings — the right call for retrieval).
2. Chroma returns top `k * 3` child chunks ranked by cosine distance.
3. We **deduplicate by parent section** — three matching children from the
   same wiki section collapse to one parent.
4. The top-k parents become the LLM context. Gemini 2.5 Flash answers with
   page-title citations, refusing when context doesn't cover the question,
   and matches the language of the question.

---

## Free tier — what to expect

Gemini free tier (2026):

| Model | Free quota | This corpus |
|---|---|---|
| `gemini-embedding-001` | 100 RPM, 1000 RPD | 628 chunks → 1 full rebuild/day |
| `gemini-2.5-flash` | 10 RPM, 250 RPD | Plenty for interactive use |

The build script paces embeddings at ~70 items/min, well below the 100 RPM
cap, and parses `retryDelay` from any 429 to wait the right amount.
Incremental rebuilds (after the first) typically embed only the handful of
chunks you've changed — usually free of any noticeable quota spend.

ChromaDB is local SQLite. Zero cost, zero ops, zero external state.

---

## Key management — fully local

| Thing | Where | Committed? |
|---|---|---|
| `GEMINI_API_KEY` | `.env` | ❌ gitignored (`.env`, `*.key`) |
| `.env.example` | repo root | ✅ safe template |
| `chroma_db/` | repo root | ❌ gitignored |
| `raw_converted/` | repo root | ❌ gitignored |

To rotate the key: regenerate at <https://aistudio.google.com/apikey>,
update `.env`, done. No redeploy, no remote env vars.

---

## Troubleshooting

- **`GEMINI_API_KEY is not set`** — copy `.env.example` to `.env` and add
  your key.
- **`Collection 'rrag-wiki' not found`** — run `build_index.py` first.
- **`429 RESOURCE_EXHAUSTED`** — daily embedding quota hit. The retry
  handler will sleep based on `retryDelay`; if you've burned the daily
  budget, wait until the quota resets (midnight Pacific).
- **Bad answers on a topic** — run with `--no-llm` to inspect retrieval. If
  the right chunks aren't coming back, the wiki page probably needs
  expansion (see `workflows/expand.md`).
- **Chinese queries return English chunks** — normal. `gemini-embedding-001`
  is multilingual; the wiki body is mostly English but the embedding model
  bridges across languages. The LLM will still answer in Traditional
  Chinese per the system prompt.
