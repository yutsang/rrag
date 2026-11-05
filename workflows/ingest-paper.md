# Workflow: Ingest an Academic Paper

Use this workflow when the user gives you a journal article, conference paper, or preprint (arXiv, SSRN, NBER) — anything peer-reviewed or pre-publication. For non-academic sources use `workflows/ingest.md`.

This workflow is tuned for the Operations Research PhD reading pipeline. The goal is not just to summarize the paper but to build an accumulating, cross-linked research corpus the user can navigate when writing their own work. Every paper page must be independently valuable as a research note — dense enough that the user never needs to re-read the paper just to recall what it said.

---

## Triggers

- "Ingest this paper: \<URL/DOI/arXiv\>"
- "I put a paper in `raw/papers/`"
- "Add this paper: \<citation\>"
- Any file dropped in `raw/papers/` at session start

---

## Inputs

- **PDF file** — typically at `raw/papers/<paper-slug>.pdf`, OR
- **URL** — arXiv, DOI, SSRN, journal page, author homepage

---

## Procedure

### 1. Fetch and convert

If the paper is a URL and not yet on disk:
- **arXiv**: download from `https://arxiv.org/pdf/<id>.pdf` to `raw/papers/<citation_key>.pdf`
- **DOI**: if the publisher allows direct PDF download, save to `raw/papers/`; otherwise read from the URL and record the DOI in frontmatter
- **SSRN/NBER**: download to `raw/papers/<citation_key>.pdf`

Convert to markdown:
```bash
python scripts/convert_raw.py --dir raw/papers
```

### 2. Extract bibliographic metadata

From the title page or first page, pull:

- **Title** (exact, as written)
- **Authors** — format `Lastname1, F.; Lastname2, F.`
- **Venue** — journal name or conference
- **Date published** — ISO `YYYY-MM-DD`; for preprints use submission date
- **DOI** — `10.xxxx/yyyy.zzzz` (no `https://doi.org/` prefix)
- **arXiv ID** — if applicable, `2401.xxxxx`
- **Citation key** — lowercase `<firstauthor><year><slug>` e.g., `liu2023newsvendor`

### 3. Read the paper deeply

Do NOT skim. Read in this order, taking notes:

1. **Abstract** — orientation only.
2. **Introduction** — what problem, what's new, what's the contribution? Pay attention to the pain-point paragraph (usually first 2-3 pages). What do the authors say is wrong with existing approaches?
3. **Related work** — what does this build on? What papers do they explicitly criticise or extend?
4. **Model/Setting** — the formal problem statement. Extract notation, assumptions, decision variables.
5. **Main results / theorems** — the load-bearing statements. Understand the proof idea, not just the conclusion.
6. **Algorithm / Method details** — step-by-step how it works. Complexity?
7. **Experiments / numerical results** — what did they test, what baselines, what headline numbers?
8. **Limitations / future work** — often in the final section.

Minimum reading time before writing: read the full paper at least once end-to-end.

### 4. Choose a subdirectory

Place the source page at `wiki/sources/papers/<citation_key>.md`. Themed subdirectories when 3+ papers share a theme:

- `wiki/sources/papers/queueing/`
- `wiki/sources/papers/inventory/`
- `wiki/sources/papers/revenue-mgmt/`
- `wiki/sources/papers/scheduling/`
- `wiki/sources/papers/stochastic-opt/`
- `wiki/sources/papers/ml-for-or/`
- `wiki/sources/papers/simulation/`
- `wiki/sources/papers/network-flows/`
- `wiki/sources/papers/financial-engineering/`

### 5. Write the source page

Every section is **mandatory**. Mark `*(not covered in paper)*` rather than deleting any section. Target 1500–2500 words in the body.

```markdown
---
title: "<Exact paper title>"
full_name: ""
type: source
tags: [paper, or, <subtopic>, <method-tag>]
created: "<YYYY-MM-DD>"
updated: "<YYYY-MM-DD>"
source: "<DOI URL or arXiv URL — full clickable URL>"
confidence: high
author: "<Lastname1, F.; Lastname2, F.>"
date_published: "<YYYY-MM-DD>"
venue: "<Journal or Conference>"
doi: "<10.xxxx/yyyy>"
arxiv_id: "<2401.xxxxx>"
citation_key: "<lastname2024slug>"
---

## 概述

<5–7 sentences in Traditional Chinese. Cover: (1) the specific problem being solved, (2) why existing approaches fail at it, (3) the paper's core method or idea, (4) the main result or contribution, (5) why this matters for the user's OR research direction. This is the only Chinese section.>

## Original Source

> **Paper link:** [<Title>](<full DOI or arXiv URL>)
> **Authors:** <Author list>
> **Venue:** <Journal/Conference>, <Year>
> **Citation:** `<citation_key>`

---

## Pain Point

What specific, concrete problem does this paper solve? Answer these:

1. **What was broken?** — what did prior methods get wrong or fail to handle? Quote or closely paraphrase the authors' own characterisation of the gap.
2. **Who feels this pain?** — practitioners, theoreticians, algorithm designers?
3. **Why couldn't you just use [existing method X]?** — state the fundamental obstacle.
4. **What is lost without this paper?** — what decisions would be suboptimal, or what theoretical gap remains, if this paper didn't exist?

Be specific. "The method scales poorly" is not specific enough — state the computational bottleneck (e.g., "solving a stochastic LP with $O(S^2)$ constraints for $S$ scenarios"). 

---

## Knowledge Points Covered

Inventory every concept, method, or theory this paper touches — whether it introduces them, assumes them, or applies them. Group by type:

**Foundations assumed (reader must know):**
- Bullet each prerequisite concept with a brief gloss and a wiki cross-link if available

**Methods introduced or significantly extended:**
- Bullet each new technique with a 1-sentence description

**Results and tools cited from prior work:**
- Bullet 3–5 foundational prior results that this paper builds on

Cross-link every item that has a wiki concept page using `[[wiki/concepts/page-name|Display Name]]`.

---

## Extended Summary

This is the comprehensive content section. Cover as much of the paper as possible. Subsections below are guides — add or remove based on what the paper contains. Aim for 800–1200 words here.

### Problem Formulation

State the mathematical setting precisely:
- Decision variables (with LaTeX notation)
- Objective: `$$\min / \max_x \; \mathbb{E}[\ldots]$$`
- Constraints (key ones, not exhaustive)
- Parameter space and what each parameter means
- Distributional or structural assumptions (stationarity? convexity? known demand distribution?)
- Information structure: what does the decision-maker observe and when?

### Core Idea / Technical Novelty

What is the central insight that makes this paper work? This should be expressible in 2-3 sentences without any equations. If you cannot do this, re-read the introduction.

Then explain the technical machinery: what mathematical tool (dual decomposition, LP relaxation, martingale argument, neural network approximation, etc.) enables the result?

### Algorithm / Method

Step-by-step description of the proposed method (pseudocode if short, bullets if long):
- Input, output, key subroutines
- Time and space complexity
- Any hyperparameters and how they're set
- How it differs from the closest prior algorithm

### Main Theoretical Results

For each key theorem/lemma/proposition, state:
- What it claims (paraphrased, not copy-pasted)
- What the key assumption is that makes it hold
- What breaks if that assumption is violated
- Proof technique in 1-2 sentences (e.g., "follows from Bellman's principle + uniform convergence argument")

### Empirical / Numerical Results

- Dataset(s) used (synthetic? real? which industries?)
- Baselines compared against
- Headline numbers (e.g., "15% cost reduction vs. SAA baseline on 10,000-scenario instances")
- Any surprising or counterintuitive results
- Limitations of the experimental design

### Limitations and Assumptions

List the paper's own stated limitations plus any you noticed:
- Assumptions that may not hold in practice
- Computational regime where the method breaks down
- What the paper does NOT show that a naive reader might assume it shows

---

## New Methods and Their Contribution

| Method / Concept introduced | Pain point it solves | Prior state-of-the-art it replaces |
|---|---|---|
| \<name\> | \<what was impossible/hard before\> | \<what people used to do\> |

If the paper introduces multiple methods or sub-results, give a row for each.

---

## Critical Assessment

**This section is the LLM's honest judgment.** Be direct. Grade each dimension:

| Dimension | Rating | Comment |
|---|---|---|
| Novelty | ★★★☆☆ | \<Is the core idea genuinely new, or is it a known technique applied to a new setting?\> |
| Technical soundness | ★★★★☆ | \<Are the proofs tight? Are the assumptions realistic? Any gaps?\> |
| Practical relevance | ★★★☆☆ | \<Would an operations manager or engineer actually use this? What's the implementation barrier?\> |
| Experimental rigour | ★★☆☆☆ | \<Are the baselines fair? Is the dataset representative? Are confidence intervals reported?\> |
| Clarity | ★★★★☆ | \<Is the paper well-written and reproducible?\> |

**Overall verdict:** \<1-3 sentences. Does this paper make a real contribution? Should the user read it deeply, skim it, or skip it? Does the claimed contribution hold up under scrutiny?\>

**Red flags (if any):**
- [ ] Proofs deferred entirely to appendix with no sketch
- [ ] Baseline comparisons use outdated or weak methods
- [ ] Scalability claims not backed by empirical evidence
- [ ] Key assumption (e.g., known distribution, convexity) is unrealistic for stated application
- [ ] Results hold only in a narrow parameter regime

---

## My Notes

User-facing scratch space. Leave as `*(none yet)*` until the user adds their own reflections:
- Questions for the author
- Connections to the user's own research direction
- Ideas for extensions
- Critiques

---

## Related Concepts

Cross-link every wiki concept page this paper touches:

- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]]
- [[wiki/concepts/optimization|Optimization]]
- *(add all that apply)*

---

## Related Papers

Papers already in the wiki that this paper cites, extends, or is extended by:

- [[wiki/sources/papers/\<key\>|\<Short Title (Author Year)\>]] — one-line relationship

*(none yet if first paper ingested)*

---

## Source Materials

- [Full paper](<full DOI or arXiv URL>)
- DOI: `<doi>`
- arXiv: `<arxiv_id>`
```

---

### 6. Propagate cross-links

After writing the source page:

1. **Concept pages** — for each concept in "Related Concepts", add a `## Recent Literature` section (create if missing) with a one-line entry linking back:
   ```markdown
   ## Recent Literature
   - [[wiki/sources/papers/liu2023newsvendor|Robust Newsvendor (Liu 2023)]] — extends critical-ratio result to distributionally robust formulations.
   ```

2. **Other cited papers** — if those papers are in the wiki, add a "Cited by" note in their Related Papers section.

3. **OR MOC** — add the paper to `wiki/mocs/operations-research.md` under the appropriate reading path sub-section.

4. **Financial Engineering MOC** — if paper is in that domain, add to `wiki/mocs/financial-engineering.md`.

5. **CS/Data Science MOC** — if paper is ML/algorithms-focused, add to `wiki/mocs/cs-data-science.md`.

6. **Index** — add a row to `wiki/index.md` under a `## Papers` section (create if missing).

7. **Log**:
   ```
   ## [YYYY-MM-DD] ingest | <Short Title> (<author> <year>)
   Ingested <citation_key>. Venue: <venue>. Pain point: <one-line>. Key method: <one-line>. Cross-linked: <concept list>.
   ```

---

### 7. Re-embed

```bash
python scripts/build_index.py
```

---

## Depth standard

- **Minimum**: 1200 words in the body (excluding frontmatter and code blocks).
- **Target**: 1500–2500 words. This is a research note, not an abstract.
- **Exception**: workshop papers or extended abstracts — 800+ words acceptable.

## What NOT to do

- **Do not copy the abstract.** The 概述 must be in the user's own framing, in Traditional Chinese, with the pain point and OR relevance front and centre.
- **Do not skip the Critical Assessment.** A paper page without honest judgment is just a summary. The value is knowing whether to trust and cite it.
- **Do not skip the Pain Point section.** Every paper claims to solve a problem. Verify the claim against the prior literature it cites — does the gap actually exist?
- **Do not ingest without cross-linking.** A paper sitting unlinked is dead weight.
- **Do not invent results.** If uncertain about a theorem or number, re-read or mark `(to verify)`.
- **Do not skip concept-page updates.** Each new paper should deepen the concept pages it touches.

## When multiple papers are dropped at once

Use `workflows/batch-ingest.md` as the coordinator. One subagent per paper. Shared files (`wiki/index.md`, `wiki/log.md`, MOC pages) stay coordinator-owned.
