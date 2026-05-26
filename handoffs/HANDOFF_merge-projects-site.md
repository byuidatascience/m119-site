**Date:** 2026-05-26
**Author:** Claude (agent) + m119-site
**Direction:** request
**Status:** draft
**Origin:** Student-UX review — class pages link out to a separate Projects site (`chaz-clark.github.io/M119/Projects/`), forcing students to bounce between two sites. Both are Quarto, so consolidation is a project merge, not a rewrite.
**Origin-Commit:** dbd07b4
**Topic:** merge-projects-site
**Sensitivity:** standard. Both repos are public; no secrets or PII.
**Companions:**
- `.claude/knowledge/quarto.md` (m119-site) — Quarto/Pandoc gotchas that apply to the merged build.
- `tools/swap_pages_url.py` (m119_master) — the existing Canvas URL-swap tool to repoint external references.
- The schedule-ownership rule in `AGENTS.md` / `.claude/knowledge/converter.md` — same principle: source-of-truth changes happen in m119_master, not m119-site.

---

# Feature request: merge the M119/Projects Quarto site into the course site as a "Projects" tab

## What feature

Consolidate the standalone Projects site (`chaz-clark/M119`, served at
`chaz-clark.github.io/M119/Projects/`) into the main course site as a new
**"Projects" navbar tab**, so students use one site instead of two. Execute in
**m119_master** (the source of truth that feeds m119-site), targeting **next
semester** — not mid-term.

Both sites are Quarto, so this is a **project consolidation** (combine `.qmd`
sources, navbar, assets, one `_quarto.yml`, one build/deploy), not a format
conversion.

## Why this lives in the producer's repo (m119_master)

Per the established pipeline rule, m119_master is the authoring source of truth;
content flows m119_master → m119-site. Editing the merged structure directly in
m119-site would be the same drift-creating workflow violation we've been
flagging for schedule edits. The merge — new `projects/` sources, navbar config,
asset moves, and the cross-site link rewrites — must be authored in m119_master
and flow downstream.

## How the merged site would work

- A **Projects** entry in the navbar (likely a dropdown: Unit 1, Unit 2, …,
  Reference Sheet, practice docs) alongside Home / Definitions / Schedule.
- Project pages live under `site/projects/` as native `.qmd`.
- Project assets (PDFs, reference sheet, images) move into `site/assets/`
  (or `site/assets/projects/`).
- Class/flex pages link to projects with **relative internal links**
  (`projects/unit1.html`) instead of the absolute `https://chaz-clark.github.io/M119/Projects/…`
  URLs they use today (seen in class-15, class-18, etc.).
- One Quarto build, one deploy, one search index covering projects too.

## Suggested shape (single Quarto project)

1. **Bring in the sources.** Copy the M119/Projects `.qmd` files into
   `m119_master` under `site/projects/`. Preserve their internal structure.
2. **Reconcile `_quarto.yml`.** Merge the Projects site's config into the main
   `site/_quarto.yml`:
   - Add the **Projects** navbar item (dropdown of project pages).
   - Confirm the **MathJax macros** (`\ds`, `\diff`) and `html-math-method`
     cover the project pages (they rely on the project-level
     `include-in-header` — see `.claude/knowledge/quarto.md`).
   - Reconcile **theme** (main site uses `flatly`/`darkly`) — match or adopt.
   - Watch **freeze** and any conflicting project-level settings.
3. **Move assets.** Relocate `m119-docs` PDFs, the reference sheet, and images
   into the main site's asset tree; update `resources:` globs in `_quarto.yml`
   and fix any in-page asset paths.
4. **Rewrite internal links.** Convert every `https://chaz-clark.github.io/M119/Projects/…`
   reference inside `site/class/*.qmd` and `site/flex/*.qmd` to the new
   relative path. (Grep the class/flex sources for `M119/Projects` to inventory.)
5. **Rewrite external references — next semester only.** Use
   `tools/swap_pages_url.py` (set `OLD`/`NEW`, run `--apply`) to repoint Canvas
   and other external links from `/M119/Projects/…` to the new
   `/m119-site/projects/…` location. The swap log lists every Canvas location.
6. **Retire / stub the old Projects site.** Once references move, sunset
   `chaz-clark/M119` Projects (archive, or leave a redirect stub) so old links
   don't 404 during the transition.

## What I've ruled out

- **Keeping two separate Quarto projects and just cross-linking** — doesn't
  achieve "one site"; students still bounce. Rejected per the stated goal.
- **Embedding the rendered Projects HTML as static files** — unnecessary since
  the source is Quarto; native `.qmd` gives unified search, theme, and nav.
- **Doing the merge in m119-site directly** — violates the source-of-truth
  pipeline; would be overwritten / cause drift.
- **Mid-semester cutover** — URL changes would break live Canvas links during
  the term. Scoped to next-semester per maintainer.

## Open questions to resolve at execution (need the M119 + m119_master repos open)

These couldn't be verified from m119-site (the M119/Projects source isn't cloned
here, and m119_master access was out of scope this session):

- **M119/Projects structure** — exact location of its `.qmd`, `_quarto.yml`, and
  assets; how many project pages; desired Projects-tab nav structure
  (flat links vs dropdown vs sub-sections).
- **Authoring model** — are the Projects pages hand-authored `.qmd`, or
  generated by a pipeline (like class pages from PMWiki)? If generated, the
  generation step has to move too, not just the output.
- **`_quarto.yml` deltas** — theme, math method, freeze, filters, any Projects-
  specific extensions that must merge cleanly.
- **Full external-link inventory** — every Canvas/syllabus location pointing at
  `/M119/Projects/…` (feed `swap_pages_url.py`).
- **URL scheme** — confirm the new base (`chaz-clark.github.io/m119-site/projects/…`)
  and whether the eventual org-level host migration (`byui-math-dept`, see
  `publishing.md`) changes the target.

## Acceptance check

- The published course site has a working **Projects** navbar tab; every former
  `/M119/Projects/` page is reachable from it.
- No `https://chaz-clark.github.io/M119/Projects/` absolute links remain in
  `site/class/*.qmd` or `site/flex/*.qmd` (grep returns nothing).
- Project pages render with correct math (`\ds`/`\diff` macros resolve) and theme.
- Canvas/external references point to the new location (swap log updated).
- The old Projects site redirects or is archived; no live 404s.
- One `quarto render` builds the whole site; one deploy.

---

## Lifecycle

- **Authored:** 2026-05-26 in m119-site `handoffs/` (Status: draft).
- **Next step (drop):** copy into m119_master's root as
  `M119-SITE_HANDOFF_merge-projects-site.md` and set Status: delivered when
  ready to act on it for next semester.
- **Apply:** m119_master maintainer executes the merge there, commits, sets
  Status: applying → applied.
- **Archive:** producer deletes the dropped copy; this canonical copy stays in
  m119-site `handoffs/` with Status: archived.
