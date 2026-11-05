# Slides Workflow

Generate Marp-format slide presentations from wiki content.

## Trigger

- User asks for a presentation, slide deck, or talk outline on a topic.
- User runs `/slides <topic or MOC name>`.

## Prerequisites

- The wiki has sufficient content on the topic (at least 3 related pages).
- `wiki/slides/` directory exists (create if missing).

## Workflow

### Phase 1: Scope and Outline

1. **Identify source material**: Read `wiki/index.md` to find relevant pages. If the user specifies a MOC, read that MOC — its reading path becomes the slide order.
2. **Read source pages**: Read all relevant source, concept, analysis, and entity pages.
3. **Propose outline**: Present a slide outline to the user for approval:
   - Title slide
   - Overview / agenda (2-3 bullets)
   - Content slides (one per major concept or finding)
   - Comparison / analysis slides (from analysis pages)
   - Open questions / frontier slides
   - References slide

### Phase 2: Generate Slides

4. **Create the Marp file** at `wiki/slides/<topic>.md` with this structure:

```markdown
---
marp: true
theme: default
paginate: true
header: "Wiki Title"
footer: "Generated from wiki — YYYY-MM-DD"
---

# Slide Title

Subtitle or context

---

## Section Title

- Key point with [[wiki-link]] citation
- Key point
- Key point

<!-- Speaker notes go here -->

---
```

5. **Content rules for slides**:
   - **One idea per slide**. If a concept needs more space, split into multiple slides.
   - **Bullet points, not paragraphs**. Max 5 bullets per slide, each under 15 words.
   - **Cite sources** using `[[wiki-link]]` notation so links resolve in Obsidian.
   - **Include Mermaid diagrams** from source pages where they exist — Marp renders Mermaid natively.
   - **Include math** using `$...$` notation — Marp supports KaTeX.
   - **Use comparison tables** from analysis pages as-is.
   - **Key numbers and results**: Pull specific experimental results from source pages (e.g., "97.0% on planning tasks" not "high accuracy").

6. **Slide types by wiki page type**:
   - **Source page** -> 1-3 slides: core mechanism, key result, connection to theme.
   - **Concept page** -> 1-2 slides: definition + taxonomy/spectrum, key evidence.
   - **Analysis page** -> 1-2 slides: comparison table, key finding.
   - **Entity page** -> Skip unless the presentation is about the research landscape.
   - **MOC** -> Becomes the slide order; MOC narrative becomes speaker notes.

### Phase 3: Polish and Log

7. **Review the deck**: Verify all wiki-links resolve, math renders correctly, slide count is reasonable (15-30 for a standard talk).
8. **Update `wiki/index.md`**: Add the new slides file to the Analyses or a new Slides section.
9. **Log**: Append to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] slides | Topic Title
   Generated N-slide Marp presentation from [MOC/pages]. Output: wiki/slides/topic.md
   ```

## Output Format

- **File**: `wiki/slides/<topic>.md`
- **Format**: Marp-compatible markdown (view with Marp for Obsidian plugin, or export to PDF/PPTX via Marp CLI: `marp wiki/slides/topic.md --pdf`)
- **Length**: 15-30 slides for a standard talk, 5-10 for a lightning talk.

## Notes

- Slides are a **derived view** of wiki content, not new information. Do not add claims that aren't in the wiki.
- If the wiki lacks depth on a subtopic, note it in speaker notes and suggest an `/expand` pass.
- Slides can be regenerated as the wiki evolves — treat them as ephemeral outputs, not permanent artifacts.
