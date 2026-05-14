# m119-site

Published Quarto course site for **Math 119 — Applied Calculus for Data Analysis** at BYU-Idaho. Renders to `site/_site/` and deploys to GitHub Pages via [`.github/workflows/publish.yml`](.github/workflows/publish.yml).

**Live site:** https://chaz-clark.github.io/m119-site/

## What this repo is

- The student-facing publish side of the Math 119 pipeline. Content authoring lives upstream in the sibling `m119-master` repo.
- A Quarto site — pages are `.qmd` files under [`site/class/`](site/class/), [`site/flex/`](site/flex/), and [`site/definitions/`](site/definitions/).
- Deployed automatically: pushes to `main` trigger a Quarto render + GitHub Pages publish.

## Working in this repo

If you're a faculty maintainer making content edits, start with **[FACULTY.md](FACULTY.md)** — it covers the day-to-day workflow with no programming background assumed.

If you're an agent (or developer) doing non-trivial work in this repo, start with **[AGENTS.md](AGENTS.md)** — it defines the project's structure, working style, and the discipline rules in [`knowledge/behavioral_discipline.md`](knowledge/behavioral_discipline.md).

## Local preview

```bash
cd site
quarto preview      # live-reload preview server
quarto render       # one-shot full build to site/_site/
```

The repo has no Python dependency for typical content edits. The one Python entry point, [`tools/generate_schedule.py`](tools/generate_schedule.py), runs in CI daily to refresh `site/_today.qmd`; you only need it locally if you're editing [`schedule_config.yml`](schedule_config.yml).

## License

See [LICENSE](LICENSE).
