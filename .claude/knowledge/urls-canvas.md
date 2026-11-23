# Canvas → Projects site URLs

**When to read:** editing Canvas project links, Module items, assignment descriptions, or adding new links from Canvas into this site.

All Canvas references to the project pages point at this site: `https://byuidatascience.github.io/m119-site/projects/`. The old hosts (`chaz-clark.github.io/M119` and `byuistats.github.io/M119`) are dead and return 404s. Don't link to them.

Scope (course 425166, FA26): 13 pages (the 12 "Project N Task N / Final Links" pages plus Math 119 Weekly Rhythm), 12 assignment descriptions, and 11 module external-URL items (Project 1/2/3 Instructions plus 8 Additional Resources). m119-master's `tools/url_swap_log_2026-11-23.md` lists every location.

## Mapping applied (2026-11-23)

| Old (dead) | Current |
|---|---|
| `chaz-clark.github.io/M119/Projects/unitN.html` | `byuidatascience.github.io/m119-site/projects/unitN.html` |
| `chaz-clark.github.io/M119/Projects/index.html` | `byuidatascience.github.io/m119-site/projects/index.html` |
| `chaz-clark.github.io/M119/Projects/specs_detail.html` | `byuidatascience.github.io/m119-site/projects/specs_detail.html` |
| `chaz-clark.github.io/M119/Projects/m119-docs/FILE.html` | `byuidatascience.github.io/m119-site/projects/m119-docs/FILE.html` |

It's a prefix swap. `Projects` became lowercase `projects`, and `#anchors` carried over unchanged.

## Gotchas

- **Canvas links to `m119-docs/*.html` pages that no site page links to** (e.g. `GreekLetters.html`, `ExampleProject_Task2.html`). Quarto only publishes static HTML that a rendered page links to, unless it's in `resources`. `_quarto.yml` lists `projects/m119-docs/**/*.html` under `resources` for this reason (PR #29). Don't remove it.
- **Renaming a project heading changes its anchor** and breaks the Canvas deep links (e.g. `unit3.html#task-1-data-and-general-models`). After a heading change, repoint Canvas through m119-master.
- **Canvas writes belong to m119-master.** Send link changes there as a handoff. Its `tools/swap_pages_url.py` updates only the matching items (dry run by default). Avoid a full `canvas_sync --push`, which sends every locally changed file.
