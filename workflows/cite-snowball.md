# Workflow: Citation Snowballing

Use this workflow to systematically expand the paper corpus around a seed paper or topic. Snowballing traces both backward (papers the seed cites) and forward (papers that cite the seed). Use after ingesting a key paper when you want full coverage of its intellectual neighborhood.

---

## Triggers

- "Snowball from [paper/citation_key]"
- "Find all related papers to [topic]"
- "I want full coverage around [paper title]"
- After ingesting a highly relevant paper rated ★★★★+ in Critical Assessment

---

## Inputs

- **Seed paper** — an already-ingested paper in `wiki/sources/papers/`, OR a DOI/arXiv ID
- **Direction** — `backward` (references), `forward` (citing papers), or `both` (default)
- **Depth** — 1 hop (direct refs only) or 2 hops (refs of refs); default is 1
- **Topic filter** — optional keyword to prune off-topic papers (e.g., "inventory", "stochastic")

---

## Procedure

### 1. Identify the Seed

From the seed paper's wiki page, collect:
- DOI or arXiv ID (from frontmatter `doi:` or `arxiv_id:`)
- `citation_key` for log and index references
- The **Related Papers** section — already-ingested neighbors to skip

### 2. Backward Snowball (References)

Pull the seed paper's reference list. Sources:

**Option A — Semantic Scholar API:**
```python
import requests

# Get paper details including references
paper_id = "10.1287/opre.2021.XXXX"  # DOI, or "arXiv:2401.XXXXX"
url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/references"
params = {
    "fields": "title,authors,year,venue,externalIds,abstract,citationCount",
    "limit": 100
}
r = requests.get(url, params=params)
refs = r.json().get("data", [])

for ref in refs:
    p = ref.get("citedPaper", {})
    print(p.get("title"), "|", p.get("year"), "|", p.get("venue"))
```

**Option B — Read the PDF bibliography:**
If you have the PDF locally, scan the reference list directly. Copy DOIs or arXiv IDs for look-up.

**Option C — Google Scholar:**
Search the exact title, click "Cited by N" link to get citing papers (forward snowball).

### 3. Forward Snowball (Citing Papers)

Find papers that cite the seed — these represent the field's response and extensions:

```python
import requests

paper_id = "10.1287/opre.2021.XXXX"
url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations"
params = {
    "fields": "title,authors,year,venue,externalIds,abstract,citationCount",
    "limit": 100
}
r = requests.get(url, params=params)
citing = r.json().get("data", [])

for cite in citing:
    p = cite.get("citingPaper", {})
    print(p.get("title"), "|", p.get("year"), "|", p.get("venue"))
```

### 4. Triage the Candidates

Apply the same 3-tier triage as `workflows/paper-radar.md`:

| Tier | Criteria | Action |
|---|---|---|
| **Must-read** | Directly extends or is extended by seed; top venue; high citation count relative to age | Add to Priority queue; ingest next |
| **Should-read** | Same technical toolkit; adjacent problem; moderate citations | Add to Queue |
| **Skip** | Only tangentially related; no new method; predates the field's current state-of-the-art | Log as skipped |

Additional snowball-specific signals:
- Papers the seed explicitly calls out in its "Related Work" as the closest prior work → **must-read**
- Papers the seed says "we extend X" or "we improve on X" → **must-read** (X is the direct predecessor)
- High citation count papers from the same author group → **should-read**
- Papers in the same venue within ±2 years that the seed doesn't cite (potential rivals) → **worth checking**

### 5. Check Against Existing Wiki

Before queuing any paper for ingest, check if it's already in the wiki:

```bash
# Search by title keywords
grep -r "liu2023" wiki/sources/papers/ --include="*.md" -l
grep -r "newsvendor" wiki/sources/papers/ --include="*.md" -l
```

Or check `wiki/index.md` under the `## Papers` section.

Skip papers already ingested. For papers already ingested, add the seed ↔ neighbor relationship to their **Related Papers** sections.

### 6. Build the Snowball Map

Create or update a section in the seed paper's wiki page under `## Related Papers`:

```markdown
## Related Papers

### Backward (seed cites these)
- [[wiki/sources/papers/bertsimas2004price|Bertsimas & Sim (2004)]] — foundational price of robustness result this paper extends.
- [[wiki/sources/papers/scarf1958minmax|Scarf (1958)]] — original minimax newsvendor; direct ancestor.

### Forward (these cite seed)
- [[wiki/sources/papers/chen2021dro|Chen et al. (2021)]] — applies seed's DRO framework to multi-period setting.
- *(not yet ingested: Goh & Sim 2010 — Distributionally Robust Optimization and Its Tractable Approximations)*
```

Mark not-yet-ingested papers with `*(not yet ingested: ...)*` so they appear on the queue.

### 7. Update the OR MOC Reading Path

If the snowball reveals a cluster of 3+ papers forming a coherent sub-thread, add a **Reading Path** note to `wiki/mocs/operations-research.md`:

```markdown
### Distributionally Robust Newsvendor — Reading Path
1. [[wiki/sources/papers/scarf1958|Scarf (1958)]] — minimax foundation
2. [[wiki/sources/papers/bertsimas2004|Bertsimas & Sim (2004)]] — price of robustness
3. [[wiki/sources/papers/delage2010|Delage & Ye (2010)]] — moment-based ambiguity sets
4. [[wiki/sources/papers/gao2023|Gao et al. (2023)]] — Wasserstein ball formulation
```

### 8. Queue for Ingest

For each must-read and should-read paper not yet in the wiki:
- Add a checkbox entry in today's `wiki/journal/YYYY-MM-DD.md`
- Include arXiv or DOI for handoff to `workflows/ingest-paper.md`

```markdown
## Snowball Queue — [seed_citation_key] — [YYYY-MM-DD]

### Must-read (ingest next)
- [ ] [Scarf 1958](doi:10.2307/2299707) — Minimax newsvendor; direct ancestor of seed method.
- [ ] [Bertsimas & Sim 2004](doi:10.1287/opre.1030.0065) — Price of robustness; seed explicitly extends this.

### Should-read (ingest next sprint)
- [ ] [Delage & Ye 2010](doi:10.1287/opre.1090.0741) — Moment ambiguity sets; parallel approach.
```

### 9. Log

```
## [YYYY-MM-DD] cite-snowball | <seed_citation_key>
Direction: both. Depth: 1. Found: <N backward> refs, <N forward> citing papers.
Triaged: <N must-read>, <N should-read>, <N skipped>.
Already in wiki: <N>. New queue entries: <N>.
MOC updated: yes/no.
```

---

## Two-Hop Snowball (Depth 2)

Use when you need comprehensive topic coverage (e.g., preparing a literature review chapter). After completing the 1-hop snowball:

1. For each must-read paper found in hop 1, repeat steps 2–4.
2. Cap at 3 must-read papers per hop-1 paper to avoid explosion.
3. Total budget: ~20–30 papers per two-hop run.

**Warning**: two-hop snowballing can surface hundreds of papers. Apply strict triage. The goal is coverage of the intellectual core, not completeness.

---

## Snowball Python Script

For fully automated backward+forward collection:

```python
import requests
from collections import defaultdict

def get_paper_neighbors(paper_id, direction="both", limit=50):
    """
    paper_id: DOI like "10.1287/opre.XXX" or arXiv like "arXiv:2401.XXXXX"
    direction: "references", "citations", or "both"
    """
    fields = "title,authors,year,venue,externalIds,abstract,citationCount"
    base = "https://api.semanticscholar.org/graph/v1/paper"
    results = defaultdict(list)

    if direction in ("references", "both"):
        r = requests.get(f"{base}/{paper_id}/references",
                         params={"fields": fields, "limit": limit})
        if r.ok:
            for item in r.json().get("data", []):
                p = item.get("citedPaper", {})
                results["references"].append(p)

    if direction in ("citations", "both"):
        r = requests.get(f"{base}/{paper_id}/citations",
                         params={"fields": fields, "limit": limit})
        if r.ok:
            for item in r.json().get("data", []):
                p = item.get("citingPaper", {})
                results["citations"].append(p)

    return results

def triage(paper, topic_filter=None):
    """Simple triage: returns 'must', 'should', or 'skip'."""
    title = (paper.get("title") or "").lower()
    abstract = (paper.get("abstract") or "").lower()
    venue = (paper.get("venue") or "").lower()
    citations = paper.get("citationCount") or 0
    year = paper.get("year") or 0

    top_venues = {"operations research", "management science", "msom",
                  "mathematics of operations research", "math. oper. res."}

    if topic_filter and topic_filter.lower() not in title + abstract:
        return "skip"
    if any(v in venue for v in top_venues) and citations > 20:
        return "must"
    if year >= 2020 and citations > 5:
        return "should"
    if year >= 2022:  # too new to have many citations
        return "should"
    return "skip"

# Example run
seed_doi = "10.1287/opre.2021.XXXX"
neighbors = get_paper_neighbors(seed_doi)

for direction, papers in neighbors.items():
    print(f"\n### {direction.upper()} ###")
    for p in papers:
        tier = triage(p, topic_filter="inventory")
        if tier != "skip":
            arxiv = (p.get("externalIds") or {}).get("ArXiv", "")
            url = f"https://arxiv.org/abs/{arxiv}" if arxiv else ""
            print(f"[{tier.upper()}] {p.get('title')} ({p.get('year')}) | {p.get('venue')} | cites: {p.get('citationCount')} | {url}")
```

Save to `scripts/cite_snowball.py`. Run: `python scripts/cite_snowball.py`.

---

## When to Use vs. Paper Radar

| Task | Use |
|---|---|
| Staying current with new publications | `paper-radar.md` |
| Deep coverage around one paper/topic | `cite-snowball.md` |
| Preparing a literature review section | `cite-snowball.md` (depth 2) |
| Finding the founding papers of a method | `cite-snowball.md` backward only |
| Finding who responded to a key paper | `cite-snowball.md` forward only |
