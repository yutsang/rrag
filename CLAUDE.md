# LLM Wiki Schema

You are a wiki maintainer for this Obsidian vault. Every interaction follows these rules.

## Language

- All content (headers, body, bullets, tables, code) is written in **English**.
- Every wiki page must begin with a **概述** section: a 2-4 sentence summary in **Traditional Chinese** (繁體中文) explaining what the page covers and why it matters. This is the only Chinese content on the page.
- All section headers after 概述 are in English.

## Directory Structure

```
raw/                                    # Immutable source documents. Never modify these.
raw/assets/                             # Downloaded images referenced by sources.
raw/docs/                               # Documentation files (official docs, guides, READMEs).
raw/articles/                           # Web-clipped articles and blog posts.
raw/courses/                            # University course materials (lecture notes, slides, readings).
raw/papers/                             # Academic papers (PDFs): journal articles, conference papers, preprints.
raw/index.md                            # Asset index mapping files to wiki pages.
workflows/                              # Task-oriented workflow playbooks.
workflows/*.md                          # One file per workflow; authoritative workflow instructions.
wiki/                                   # LLM-generated and LLM-maintained pages. You own this entirely.
wiki/index.md                           # Top-level catalog — links to MOCs + flat concept/entity/analysis lists.
wiki/log.md                             # Chronological activity log — append-only.
wiki/overview.md                        # Narrative synthesis of the knowledge landscape.
wiki/mocs/*.md                          # Maps of Content — thematic navigation with reading paths.
wiki/sources/                           # Source summary pages, organized by theme:
  wiki/sources/claude-code/             #   Claude Code CLI, hooks, skills, harness, settings
  wiki/sources/claude-api/              #   Claude API, Anthropic SDK, tool use, streaming
  wiki/sources/agent-sdk/               #   Claude Agent SDK, multi-agent patterns
  wiki/sources/mcp/                     #   Model Context Protocol (MCP) servers, tools, resources
  wiki/sources/prompting/               #   Prompt engineering, system prompts, best practices
  wiki/sources/ai-general/              #   General AI/ML concepts, architecttic patterns
  wiki/sources/courses/                 #   University course material summaries
  wiki/sources/papers/                  #   Academic paper summaries (OR, ML, stats, finance, etc.)
wiki/concepts/                          # Concept pages (ideas, patterns, techniques)
wiki/entities/                          # Entity pages (people, orgs, products, tools)
wiki/analyses/                          # Analysis pages (syntheses, comparisons)
wiki/journal/                           # Daily thoughts, reflections, ideas — human-written or LLM-assisted.
wiki/journal/YYYY-MM-DD.md             #   One file per day. Freeform. Tagged for cross-referencing.
```

### Journal (Daily Thoughts)

`wiki/journal/` is for daily thoughts, reflections, questions, and ideas. Unlike other wiki pages which are LLM-maintained, journal entries can be human-written or LLM-assisted.

Journal page frontmatter:
```yaml
---
title: "YYYY-MM-DD"
type: journal
tags: [journal, relevant-topics]
created: "YYYY-MM-DD"
confidence: medium
---
```

Journal entries should link to concept/entity pages when mentioning known topics. The LLM can help organize, tag, and cross-reference journal entries during review passes.

### Session Start

At the beginning of each conversation, orient yourself before acting:

1. **`wiki/index.md`** — Read first. Page catalog with directory tree counts, MOC links, and flat listings.
2. **`wiki/log.md`** (last 5-10 entries) — Recent activity. Avoids redoing work.
3. **`wiki/overview.md`** — Read only for synthesis tasks, query answering, or understanding how new content fits. Skip for targeted tasks.
4. **MOCs** — Read the relevant MOC(s) when working on a specific theme.

For targeted tasks (expand one page, fix one link, ingest one source), steps 1-2 suffice. For broad tasks (review, synthesis, MOC gap analysis), read step 3 as well.

### Source Categorization

When placing a new source in `wiki/sources/`, use the source's **primary topic** to pick the subdirectory:

| Subdirectory | Place here when the source is primarily about… |
|---|---|
| `claude-code/` | Claude Code CLI tool: hooks, skills, slash commands, settings, harness, permissions, IDE integration, worktrees |
| `claude-api/` | Claude API: Anthropic SDK, tool use, streaming, messages API, embeddings, batch API, prompt caching |
| `agent-sdk/` | Claude Agent SDK: building custom agents, multi-agent orchestration, agent loops |
| `mcp/` | Model Context Protocol: MCP servers, tools, resources, transports, server development |
| `prompting/` | Prompt engineering: system prompts, few-shot, chain-of-thought, best practices, eval |
| `ai-general/` | General AI/ML topics that inform the above but aren't specific to Claude/Anthropic |
| `courses/` | University course materials: lecture summaries, reading notes, assignment analyses |
| `papers/` | Academic papers: peer-reviewed journal articles, conference papers, preprints (arXiv, SSRN). See `workflows/ingest-paper.md` for the paper-specific workflow |

**When ambiguous**: Choose the category that best describes *the primary contribution*. A blog post about using MCP servers inside Claude Code belongs in `mcp/` if the novelty is the MCP server, or `claude-code/` if the novelty is the integration pattern.

### Adding New Source Subdirectories

Create a new subdirectory under `wiki/sources/` when:
- 3+ sources share a coherent theme that doesn't fit existing categories.
- The theme represents a genuinely distinct area, not just a variation.

When creating one: add it to the directory tree above, update `wiki/index.md`, and document it in the categorization table.

## Page Types

Wiki pages use YAML frontmatter. Every page MUST have these fields: `title`, `type`, `tags`, `created`, `confidence`.

The `updated` field records the date of the last **substantive content change** — new claims, revised analysis, added sources. Bump it when information changes, not for typo fixes or formatting.

The `confidence` field indicates how well-supported the page content is:
- `high` — Based on official documentation, verified code, or authoritative primary sources.
- `medium` — Based on reliable secondary sources (blog posts, tutorials, community docs) or partially verified.
- `low` — Based on inference, single unverified sources, or rapidly changing information that may be outdated.

### Source Summary
```yaml
---
title: "Article or Document Title"
full_name: "Full Name with Abbreviation (ABBR)"  # e.g., "Model Context Protocol (MCP)"
type: source
tags: []
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
source: "URL or file path to original"
confidence: high|medium|low
author: "Author Name(s)"
date_published: "YYYY-MM-DD"
---
```
One per ingested source. Summarizes key claims, data, and takeaways. Links to entity/concept pages.

For raw file sources, use `source:` to reference the file path (e.g., `"raw/docs/claude-code-hooks.md"`). For web sources, use the URL.

#### Course Source Pages — Tag and Title Rules

For university course source pages in `wiki/sources/courses/`:

- **Course code goes in `tags` only** — e.g., `tags: [courses, ieda, undergraduate, ieda3010]`. The course code does **not** need to appear in `title` or `full_name`.
- **`title`** should be the plain course name without the code: e.g., `"Operations Research I"` not `"IEDA3010 Operations Research I"`.
- **`full_name`** may include the code if disambiguation is needed: e.g., `"IEDA3010 Operations Research I"`. Otherwise omit it or use just the name.
- Tag the lowercase course code exactly as written (e.g., `ieda3010`, `comp4211`, `math2411`).
- Also tag the department in lowercase (e.g., `ieda`, `comp`, `math`, `fina`), the level (`undergraduate` or `graduate`), and 1-3 topic tags.

Example:
```yaml
tags: [courses, ieda, undergraduate, ieda3010, operations-research, linear-programming]
```

**Why**: Obsidian graph nodes are named by `title`. Keeping the title clean (no code prefix) makes graph nodes readable. The course code is searchable via tags.

### Academic Paper (extends Source Summary)

Papers use the same `type: source` but add paper-specific fields. Use this for anything peer-reviewed, conference proceedings, or preprints (arXiv, SSRN, OR-specific venues like Operations Research, MSOM, M&SOM, POM):

```yaml
---
title: "Paper Title as Written"
full_name: ""
type: source
tags: [paper, or, <subtopic>]             # always include 'paper'; add OR subtopic
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
source: "DOI URL or arXiv URL"
confidence: high
author: "Lastname1, F.; Lastname2, F."    # semicolon-separated, first-initial style
date_published: "YYYY-MM-DD"
venue: "Operations Research"              # journal or conference name
doi: "10.1287/opre.xxxx.xxxx"            # if peer-reviewed
arxiv_id: "2401.xxxxx"                    # if preprint
citation_key: "lastname2024shortitle"     # lowercase author + year + 1-2 word slug
---
```

The body of an academic paper page has a fixed structure — see `workflows/ingest-paper.md` for the full template (Contribution, Setting, Method, Results, Limitations, My Notes, Related Work).

### Entity Page
```yaml
---
title: "Entity Name"
full_name: "Full Official Name (Abbreviation)"  # e.g., "Anthropic (ANTH)"
type: entity
tags: []
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
source: "Primary reference URL"
confidence: high|medium|low
aliases: []
---
```
A person, organization, product, tool, or other named thing. Accumulates information across sources. Each claim cites its source summary.

### Concept Page
```yaml
---
title: "Concept Name"
full_name: "Full Descriptive Name (Abbreviation)"  # if applicable
type: concept
tags: []
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
source: "Primary reference URL or source page"
confidence: high|medium|low
---
```
An idea, technique, pattern, or framework. Cross-references related concepts and entities. Evolves as new sources add nuance.

### Analysis Page
```yaml
---
title: "Analysis Title"
full_name: ""  # if applicable
type: analysis
tags: []
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
source: "Derived from wiki content"
confidence: high|medium|low
---
```
Comparisons, syntheses, arguments, or explorations generated from queries. Filed back into the wiki when valuable.

### Overview / Map of Content (MOC) Page
```yaml
---
title: "MOC Title"
full_name: ""
type: overview
tags: [moc]
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
source: ""
confidence: high
---
```
Curated navigation pages that organize related wiki pages around a theme. MOCs provide **guided reading paths** with narrative context. A page can appear in multiple MOCs. Create a new MOC when 5+ pages form a coherent theme. MOCs live at `wiki/mocs/*.md`.

Current MOCs: *(none yet — will be created as the wiki grows)*

## Page Structure Template

Every wiki page follows this structure:

```markdown
---
(frontmatter)
---

## 概述
2-4 sentence summary in Traditional Chinese. This is the only Chinese section.

## Core Mechanism
(or Architecture, Configuration, Usage — whichever fits the page type)
English body content...

## Key Findings
Key findings, results, or takeaways...

## Related Concepts
- [[Concept 1]]
- [[Concept 2]]

## Source Materials
- [[raw/docs/source-file|Source Title]]
```

## Linking Conventions

- Use Obsidian wiki-links: `[[Page Name]]` or `[[Page Name|display text]]`.
- Link liberally. Every mention of an entity or concept that has its own page should be linked.
- When creating a new page, scan existing pages for mentions of the new topic and add backlinks.
- Use `[[raw/filename|Source: Title]]` to cite raw sources from wiki pages.

## Source Materials Footer

Every source page ends with a `## Source Materials` section containing direct links to the raw source:
```markdown
## Source Materials

- [[raw/docs/source-file.md|Original Document]]
- [External URL](https://example.com/article)
```

## Workflows

Detailed workflow instructions live in `workflows/*.md`. Do not improvise workflow steps from memory when a workflow file exists.

### Workflow Selection

Before acting:

1. Identify exactly one **primary workflow** that best matches the user's request.
2. Choose the **narrowest** workflow that fully covers the task.
3. Read the primary workflow file first. Read secondary workflow files only when explicitly called for.
4. Prefer explicit trigger matches over vague similarity:
   - 3+ new sources or explicit parallel ingest -> `workflows/batch-ingest.md`
   - Any parallel subagent output that needs QA -> `workflows/verification.md`
   - Whole-vault once-over -> `workflows/review.md`
   - Enrichment gap-finding plus prioritization -> `workflows/enrichment-audit.md`
   - Academic paper onboarding (journal, conference, arXiv, SSRN) -> `workflows/ingest-paper.md`
   - New source onboarding (non-paper) -> `workflows/ingest.md`
   - Question answering without wiki maintenance -> `workflows/query.md`
   - Slide deck or presentation request -> `workflows/slides.md`
   - Chart, plot, or data visualization -> `workflows/visualize.md`
   - Missing metadata, stale claims, or "find more on this" -> `workflows/web-enrich.md`
   - Weekly new paper scan across venues and arXiv -> `workflows/paper-radar.md`
   - Citation graph expansion around a seed paper -> `workflows/cite-snowball.md`
5. Respect workflow boundaries:
   - Shared files (`wiki/index.md`, `wiki/log.md`, MOCs, `wiki/overview.md`, `CLAUDE.md`) stay coordinator-owned unless the workflow explicitly says otherwise.
   - If a workflow says to get user approval before applying fixes, stop and ask before editing.
6. When no single workflow fits exactly, combine the minimum number needed and state which workflow is primary.

### Overview Update Triggers

`wiki/overview.md` is the entry point for newcomers. Update it when:

- **3+ sources ingested** in a batch — the landscape narrative may have shifted.
- **A new topic area emerges** that doesn't fit existing sections.
- **New MOCs are created** — add them to the overview's navigation references.
- **Major tool/API changes** — significant version updates to tracked tools.

Do NOT update for minor ingests (1-2 sources that fit cleanly into existing themes) or structural changes.

### Entity Page Scope

- **One entity, one page**: Default. Create a separate page for each tool, product, or organization.
- **Aliases**: Use the `aliases` frontmatter field for alternative names (e.g., `aliases: ["CC", "claude-code"]`).

### Diagram Maintenance

When creating or updating pages with architecture pipelines, data flows, or relationship graphs:

1. Use **Mermaid** code blocks (` ```mermaid `) — these render natively in Obsidian.
2. Use `graph LR` for pipelines/flows, `graph TD` for hierarchies.
3. Use `subgraph` with `style` directives for color-coded groupings. Standard palette:
   - Blue (`fill:#dae8fc,stroke:#6c8ebf`) — input/processing
   - Yellow (`fill:#fff2cc,stroke:#d6b656`) — intermediate
   - Green (`fill:#d5e8d4,stroke:#82b366`) — output/result
   - Orange (`fill:#ffe6cc,stroke:#d79b00`) — configuration
   - Purple (`fill:#e1d5e7,stroke:#9673a6`) — external/integration
4. Do NOT use Draw.io/`.drawio` files.
5. **Line breaks in node labels**: Use `<br>` (not `\n`).
6. Rule of thumb: if a page describes a flow with 3+ stages or a hierarchy with 3+ branches, add a Mermaid diagram.

### Pandoc Export Readiness

All pages must include a `title:` field in YAML frontmatter for clean PDF/DOCX export via the Pandoc plugin.

### Workflow Index

These files are authoritative. Keep this list in sync when adding, renaming, or removing workflows.

- `workflows/ingest.md` — Add a new source and propagate updates across source pages, entities, concepts, indexes, MOCs, and logs.
- `workflows/ingest-paper.md` — Ingest an academic paper (journal, conference, preprint) into `wiki/sources/papers/` with the paper-specific frontmatter and structured body template.
- `workflows/query.md` — Answer a user question from the wiki with targeted reading and `[[wiki-links]]` citations.
- `workflows/lint.md` — Run a health check for content integrity, structural drift, stale paths, and missing cross-references.
- `workflows/batch-ingest.md` — Ingest 3+ sources in parallel, then consolidate shared files and run verification.
- `workflows/moc-gap-analysis.md` — Audit MOC coverage, propose new MOCs, and coordinate creation.
- `workflows/verification.md` — Quality-check parallel subagent output before merge.
- `workflows/enrich.md` — Improve navigation, backlinks, asset linking, index sync, and discoverability.
- `workflows/expand.md` — Deepen thin source, concept, and entity pages to meet the depth standard.
- `workflows/synthesize.md` — Create cross-cutting analysis pages that connect multiple sources and concepts.
- `workflows/review.md` — Run a full wiki once-over combining lint, enrich, depth checks, and schema consistency.
- `workflows/enrichment-audit.md` — Systematically find, prioritize, and execute enrichment workstreams.
- `workflows/plugin-audit.md` — Audit Obsidian plugin configuration and page compliance.
- `workflows/readme-github-maintenance.md` — Update `README.md` and GitHub-facing metadata.
- `workflows/schema-self-audit.md` — Verify that `CLAUDE.md` matches the real vault layout.
- `workflows/slides.md` — Generate Marp-format slide presentations from wiki content.
- `workflows/visualize.md` — Generate matplotlib charts and data visualizations from wiki data.
- `workflows/web-enrich.md` — Use web search to impute missing metadata, verify stale claims, find new sources.
- `workflows/paper-radar.md` — Weekly scan of arXiv, Semantic Scholar, and journal TOCs for new OR papers; outputs a triage candidate list.
- `workflows/cite-snowball.md` — Backward and forward citation snowballing from a seed paper; builds a reading queue and updates Related Papers sections.

## Depth Standard

All pages must be written with **practical depth** as the default:

- **Source summaries**: Not just "what it says" but detailed explanations of how things work, configuration examples, concrete use cases, gotchas, and connections to the broader wiki. Typical length: 400-1200 words.
- **Concept pages**: Must include what it is, why it matters, how it works, practical examples, comparison with alternatives, trade-offs, and connections to adjacent concepts. Typical length: 600-1500+ words.
- **Entity pages**: Accumulate facts with citations, track capabilities and limitations, note version changes. Include key features table, relationship to other entities. Typical length: 200-500 words.

The goal is that someone reading only the wiki gets a thorough, practical understanding — enough to actually use the tools and concepts described.

## Formatting Rules

- Write in clear, concise prose. No filler.
- Use English headers (##, ###) to organize sections. Only the 概述 section is in Chinese.
- Use bullet points for lists of claims or facts; each bullet should cite its source.
- Bold key terms on first mention within a page.
- Tables for structured comparisons.
- Code blocks with language tags for configuration and code examples.

## File Naming

- Lowercase, hyphenated. The folder provides the type — **do not add type prefixes** to filenames.
- Source summaries: `wiki/sources/<theme>/short-title.md`
- Concepts: `wiki/concepts/descriptive-name.md`
- Entities: `wiki/entities/entity-name.md`
- Analyses: `wiki/analyses/topic.md`
- MOCs: `wiki/mocs/theme-name.md`

## Log Format

Each entry in `wiki/log.md` follows this format:
```
## [YYYY-MM-DD] action | Title
Brief description of what was done. Pages created/updated listed.
```

Actions: `ingest`, `batch-ingest`, `query`, `analysis`, `lint`, `update`, `review`, `enrich`, `expand`, `verify`, `moc-gap`, `enrichment-audit`, `plugin-audit`, `schema-audit`, `readme-update`, `slides`, `visualize`, `web-enrich`.
