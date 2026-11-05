# Web Enrichment Workflow

Use web search to impute missing data, verify claims, find additional sources, and enhance wiki coverage.

## Trigger

- Lint or review identifies gaps that can't be filled from existing `raw/` sources.
- User asks to find more information on a topic.
- Entity pages are missing publication dates, venues, or citation counts.
- A concept page references work not yet in the wiki.
- User runs a general "enrich from web" pass.

## Prerequisites

- WebSearch and WebFetch tools available.
- Clear understanding of what data is missing (run `/lint` first if unsure).

## Workflow

### Phase 1: Identify Gaps

1. **Read `wiki/index.md`** and recent `wiki/log.md` entries to orient.
2. **Scan for specific gap types**:
   - **Missing metadata**: Source pages without `venue`, `date_published`, `institution`, or `arxiv` fields.
   - **Stale claims**: Results or rankings that may have been superseded.
   - **Thin coverage**: Concept pages that reference papers not yet in the wiki.
   - **Missing connections**: Entity pages that lack collaboration patterns or recent publications.
   - **Open questions**: Items in `wiki/analyses/open-questions.md` that might have recent answers.
3. **Prioritize** by impact: metadata gaps (quick wins) > stale claims (accuracy) > thin coverage (depth) > missing connections (completeness).

### Phase 2: Search and Verify

4. **For each gap**, use WebSearch to find authoritative information:

   **Missing metadata**:
   - Search: `"paper title" site:arxiv.org` or `"paper title" conference YYYY`
   - Extract: venue, date, institution from the paper's landing page.
   - Verify: Cross-check against existing frontmatter — do not overwrite confirmed data.

   **Stale claims**:
   - Search: `"benchmark name" state-of-the-art YYYY` or `"method name" results`
   - Compare: Current SOTA against claims in the wiki.
   - Flag: Note if a wiki claim is outdated; suggest an update with the new data and its source.

   **Thin coverage**:
   - Search: `"concept name" survey OR review` or `"referenced paper title" arxiv`
   - Evaluate: Is the referenced paper worth adding to `raw/`? Does it add genuinely new information?
   - Suggest: New source candidates ranked by relevance and novelty.

   **Missing connections**:
   - Search: `"author name" "institution" recent publications YYYY`
   - Find: New papers by tracked entities that might be relevant.
   - Check: Are there collaborations between entities that the wiki doesn't reflect?

   **Open questions**:
   - Search: `"open question keywords" solution OR approach OR result YYYY`
   - Evaluate: Has the question been answered by recent work?
   - Update: Mark resolved questions and add the resolution source.

5. **Use WebFetch** to read specific pages when WebSearch results need deeper inspection (e.g., reading an arXiv abstract page, a conference proceedings page, or a GitHub README).

### Phase 3: Apply and Report

6. **For metadata fixes**: Update frontmatter directly. These are factual corrections that don't need user approval.

7. **For content changes**: Present a report to the user before applying:
   ```
   ## Web Enrichment Findings

   ### Metadata Fixes (applied)
   - [[source-page]]: Added venue "NeurIPS 2025", date "2025-12-10"

   ### Stale Claims (need review)
   - [[concept-page]]: Claims X is SOTA at 95.4%, but Y achieves 97.1% (source: URL)

   ### New Source Candidates
   - "Paper Title" (arxiv:XXXX.XXXXX) — relevant to [[concept]], fills gap in [[analysis]]
   - "Paper Title 2" — extends [[entity]]'s work on [[concept]]

   ### Open Question Updates
   - Q: "Can latent communication scale to 100+ agents?" — Partial answer in new paper (URL)
   ```

8. **Wait for user approval** before:
   - Updating content claims (stale data).
   - Adding new source candidates to `raw/checklist.md`.
   - Marking open questions as resolved.

9. **Log**: Append to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] web-enrich | Topic/Scope
   Web search pass: N metadata fixes applied, M stale claims flagged, K new source candidates identified.
   ```

## Search Guidelines

- **Prefer authoritative sources**: arxiv.org, Semantic Scholar, ACL Anthology, conference proceedings, official GitHub repos.
- **Date-bound searches**: Always include the current year or recent years to find the latest information.
- **Verify before applying**: Cross-reference at least 2 sources for factual claims. Do not trust a single search result.
- **Respect the wiki's scope**: Only suggest sources that are genuinely relevant to the wiki's research domain. Don't broaden the scope without user intent.
- **Cite web sources**: When adding information from the web, note the URL in a comment or footnote so it can be traced back.

## Integration with Other Workflows

- **After lint**: Lint identifies structural gaps; web-enrich fills information gaps.
- **Before ingest**: Web-enrich can identify candidate papers; ingest processes them into the wiki.
- **During expand**: When expanding a thin page, web-enrich can provide additional context not available in `raw/`.
- **With query**: When a query can't be fully answered from the wiki, web-enrich can supplement.

## Notes

- This workflow uses the LLM's web search capability, not a custom search engine.
- Web data is **supplementary** — it doesn't replace reading and ingesting primary sources.
- If a web-enrichment pass reveals significant new papers, suggest a full ingest rather than summarizing from abstracts.
- All web-sourced additions should be clearly marked so they can be verified when the primary source is later ingested.
