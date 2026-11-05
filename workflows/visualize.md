# Visualize Workflow

Generate charts, diagrams, and data visualizations from wiki content using matplotlib or other Python visualization libraries.

## Trigger

- User asks for a chart, plot, visualization, or data view.
- User wants to see quantitative data from the wiki in graphical form.
- A wiki page would benefit from an embedded chart (benchmark comparisons, timelines, distributions).

## Prerequisites

- Python 3 with matplotlib available.
- `wiki/assets/` directory exists (create if missing).
- `wiki/scripts/` directory exists for reusable generation scripts (create if missing).

## Workflow

### Phase 1: Identify Data

1. **Read relevant wiki pages** to extract quantitative data:
   - Benchmark results from source pages (accuracy, speedup, compression ratios).
   - Timeline data from `wiki/analyses/paper-timeline.md`.
   - Comparison tables from `wiki/analyses/method-comparison.md`.
   - Distribution data from concept or analysis pages.

2. **Propose the visualization** to the user:
   - Chart type (bar, line, scatter, heatmap, radar, timeline).
   - Data to include and data to exclude.
   - Dimensions and grouping (what goes on each axis).

### Phase 2: Generate

3. **Write a Python script** to `wiki/scripts/<chart-name>.py`:
   - Use matplotlib with a clean style (`plt.style.use('seaborn-v0_8-whitegrid')` or similar).
   - Embed the data directly in the script (no external file dependencies).
   - Save output to `wiki/assets/<chart-name>.png` at 300 DPI.
   - Include a comment header citing the wiki pages the data came from.
   - Make the script re-runnable: running it again overwrites the previous output.

```python
#!/usr/bin/env python3
"""
Chart: <description>
Data sources: [[page1]], [[page2]], ...
Generated: YYYY-MM-DD
"""
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend

# ... data and chart code ...

plt.tight_layout()
plt.savefig('wiki/assets/<chart-name>.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved wiki/assets/<chart-name>.png")
```

4. **Run the script** to generate the image:
   ```bash
   python3 wiki/scripts/<chart-name>.py
   ```

5. **Verify the output**: Read the generated image to confirm it looks correct.

### Phase 3: Embed and Log

6. **Embed in the relevant wiki page**:
   ```markdown
   ![[wiki/assets/<chart-name>.png]]
   *Figure: Description. Generated from [[source-page-1]], [[source-page-2]].*
   ```

7. **Update `wiki/index.md`** if a new analysis or asset section is needed.

8. **Log**: Append to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] visualize | Chart Title
   Generated <chart-type> from <data sources>. Output: wiki/assets/<chart-name>.png. Embedded in [[page]].
   ```

## Visualization Types

| Type | Use When | Example |
|------|----------|---------|
| **Bar chart** | Comparing discrete methods on a metric | Benchmark accuracy across 5 methods |
| **Grouped bar** | Comparing methods across multiple metrics | Accuracy + speedup + compression for each method |
| **Line chart** | Showing trends over time | Paper publication timeline, performance evolution |
| **Scatter plot** | Showing trade-offs between two dimensions | Accuracy vs. compression ratio |
| **Heatmap** | Showing coverage or overlap | Benchmark overlap matrix |
| **Radar/spider** | Comparing methods across many dimensions | Multi-criteria method comparison |
| **Timeline** | Chronological events | Paper lineage and influence chains |
| **Sankey/flow** | Showing information flow or category transitions | Communication depth spectrum |

## Design Rules

- **Title**: Always include a descriptive title.
- **Labels**: All axes labeled with units. Legend when comparing multiple series.
- **Colors**: Use a colorblind-friendly palette (e.g., `tab10` or `Set2`).
- **Annotations**: Annotate notable data points (best result, outliers).
- **Size**: Default `figsize=(10, 6)`. Adjust for the content.
- **Font size**: Minimum 10pt for readability when embedded in Obsidian.

## Notes

- Scripts are **reproducible**: re-running generates the same chart (unless wiki data has changed).
- Charts are **derived views** — do not add data that isn't in the wiki.
- If data is missing or inconsistent, note it in the chart caption and suggest a `/lint` or `/expand` pass.
- For complex interactive visualizations, consider generating HTML files viewable in a browser instead.
