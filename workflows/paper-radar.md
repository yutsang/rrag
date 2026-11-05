# Workflow: Paper Radar (Weekly Scan)

Use this workflow to systematically find new papers relevant to your OR research direction. Run weekly or before a new research sprint. For ingesting papers found here, hand off to `workflows/ingest-paper.md`.

---

## Triggers

- "Run paper radar"
- "What's new in [topic] this week?"
- "Find recent papers on [topic]"
- Weekly research maintenance session

---

## Inputs

- **Research focus areas** — from `wiki/mocs/operations-research.md` and your active research direction
- **Lookback window** — default: last 14 days (adjust per run frequency)
- **Target venues** — see Venue List below

---

## Procedure

### 1. Define Search Terms

Pull active research focus areas from the OR MOC and user's stated research direction. Translate into search queries:

| Focus Area | Primary Query | Alternative Terms |
|---|---|---|
| Stochastic inventory | "newsvendor" OR "inventory control" OR "stochastic lot sizing" | "base stock", "periodic review" |
| Queueing / service ops | "queueing network" OR "service operations" | "waiting time", "staffing" |
| Revenue management | "dynamic pricing" OR "revenue management" | "capacity control", "overbooking" |
| Distributionally robust | "distributionally robust" OR "ambiguity set" | "Wasserstein", "moment uncertainty" |
| Reinforcement learning for OR | "reinforcement learning" AND ("inventory" OR "scheduling" OR "routing") | "deep RL", "approximate DP" |
| Data-driven optimization | "data-driven" AND ("optimization" OR "stochastic") | "sample average approximation", "SAA" |

Adjust this table based on the user's current thesis chapter or reading list.

### 2. Search Semantic Scholar

```bash
# Semantic Scholar API — no key required for basic queries
# Base URL: https://api.semanticscholar.org/graph/v1/paper/search

# Example: papers on distributionally robust newsvendor, last 2 years
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=distributionally+robust+newsvendor&fields=title,authors,year,venue,externalIds,abstract,citationCount&limit=10&publicationDateOrYear=2024-2025"
```

For each focus area, run a query and collect:
- Title, authors, year, venue
- arXiv ID or DOI
- Abstract (for quick relevance triage)
- Citation count (proxy for impact)

### 3. Search arXiv

Target categories for OR:
- `math.OC` — Optimization and Control
- `cs.LG` — Machine Learning (for ML-for-OR papers)
- `econ.GN` — General Economics (for OR/Economics crossover)
- `q-fin.PM` — Portfolio Management / Financial OR

```bash
# arXiv API — free, no key
# Recent papers in math.OC + cs.LG, last 14 days
curl "http://export.arxiv.org/api/query?search_query=cat:math.OC+AND+all:newsvendor&sortBy=submittedDate&sortOrder=descending&max_results=10"
```

### 4. Check Target Journals

Manually or via RSS check the TOC of:

| Venue | URL | Frequency |
|---|---|---|
| Operations Research | INFORMS (informs.org/pub/opre) | Monthly |
| Management Science | INFORMS | Monthly |
| Manufacturing & Service Operations Mgmt (MSOM) | INFORMS | Quarterly |
| Production and Operations Mgmt (POM) | Wiley | Monthly |
| European Journal of Operational Research (EJOR) | Elsevier | Biweekly |
| Mathematics of Operations Research (MOR) | INFORMS | Quarterly |
| INFORMS Journal on Computing (IJOC) | INFORMS | Quarterly |
| EC (Economics and Computation) | ACM | Annual conference |
| NeurIPS / ICML / ICLR | — | Annual conferences |

### 5. Triage and Score

For each candidate paper, apply a quick triage:

**Include (score 3/3):**
- Directly addresses a method or problem you are working on
- In a top-4 OR venue (OR, MS, MSOM, MOR) with novel theoretical result
- Cited 10+ times if not brand-new

**Worth reading (score 2/3):**
- Adjacent topic (e.g., scheduling instead of inventory, but same technical tools)
- Applied ML paper with relevance to OR problem structure
- Strong arXiv preprint from known research group

**Skip for now (score 1/3):**
- Incremental extension of a problem you already understand well
- Application paper with no new method
- Out of scope venues (marketing, healthcare only, etc.)

### 6. Build the Candidate List

Create or append to `wiki/journal/YYYY-MM-DD.md` (today's date):

```markdown
## Paper Radar — [YYYY-MM-DD]

### Priority (ingest immediately)
- [ ] [Title](URL) — Authors, Venue Year. *Why:* one sentence relevance note.

### Queue (ingest next sprint)
- [ ] [Title](URL) — Authors, Venue Year. *Why:* one sentence.

### Skipped
- [Title] — Authors, Year. *Why skipped:* one sentence.
```

### 7. Handoff to Ingest

For any paper marked Priority, trigger `workflows/ingest-paper.md`:
- "Ingest this paper: [URL]"
- Drop the PDF into `raw/papers/` and say "I put a paper in raw/papers/"

---

## Venue RSS Feeds

Add these to your RSS reader for passive monitoring:

```
Operations Research:        https://pubsonline.informs.org/action/showFeed?type=etoc&feed=rss&jc=opre
Management Science:         https://pubsonline.informs.org/action/showFeed?type=etoc&feed=rss&jc=mnsc
MSOM:                       https://pubsonline.informs.org/action/showFeed?type=etoc&feed=rss&jc=msom
arXiv math.OC:              https://arxiv.org/rss/math.OC
arXiv cs.LG:                https://arxiv.org/rss/cs.LG
```

---

## Semantic Scholar Python Script

For structured multi-query runs, use this script:

```python
import requests
import json
from datetime import datetime, timedelta

BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
FIELDS = "title,authors,year,venue,externalIds,abstract,citationCount,publicationDate"

QUERIES = [
    "distributionally robust newsvendor",
    "data-driven inventory optimization",
    "reinforcement learning queueing",
    "stochastic lot sizing approximation",
    "dynamic pricing revenue management",
    "sample average approximation stochastic program",
]

cutoff_year = datetime.now().year - 1  # include current and prior year

results = []
for query in QUERIES:
    params = {
        "query": query,
        "fields": FIELDS,
        "limit": 5,
        "publicationDateOrYear": f"{cutoff_year}-{datetime.now().year}",
    }
    r = requests.get(BASE_URL, params=params)
    if r.ok:
        data = r.json().get("data", [])
        for p in data:
            results.append({
                "title": p.get("title"),
                "authors": [a["name"] for a in p.get("authors", [])[:3]],
                "year": p.get("year"),
                "venue": p.get("venue"),
                "citations": p.get("citationCount"),
                "arxiv": p.get("externalIds", {}).get("ArXiv"),
                "doi": p.get("externalIds", {}).get("DOI"),
                "abstract": (p.get("abstract") or "")[:200],
                "query": query,
            })

# Deduplicate by title
seen = set()
unique = []
for p in results:
    if p["title"] not in seen:
        seen.add(p["title"])
        unique.append(p)

# Print markdown table
print("| Title | Authors | Year | Venue | Citations | arXiv |")
print("|---|---|---|---|---|---|")
for p in unique:
    authors = ", ".join(p["authors"])
    arxiv = p["arxiv"] or "—"
    arxiv_link = f"[{arxiv}](https://arxiv.org/abs/{arxiv})" if p["arxiv"] else "—"
    print(f"| {p['title']} | {authors} | {p['year']} | {p['venue'] or '—'} | {p['citations']} | {arxiv_link} |")
```

Run with: `python scripts/paper_radar.py` (save the script to `scripts/`).

---

## Log Entry

After each radar run, append to `wiki/log.md`:

```
## [YYYY-MM-DD] paper-radar | Weekly scan
Queries: <list topics searched>. Found: <N> candidates. Priority: <N>. Queued: <N>. Ingested today: <N>.
```

---

## Depth Calibration

This workflow is deliberately **shallow** — it surfaces candidates, not deep reads. The goal is a 10-15 minute weekly sweep that feeds `workflows/ingest-paper.md`. Do not summarize papers here; triage only.
