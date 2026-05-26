**Date:** 2026-05-26
**Author:** Claude (agent) + m119-site
**Direction:** request
**Status:** draft — **DEFERRED**
**Trigger:** after the SP26 semester ends (term end `2026-07-22` per `schedule_config.yml`). Revisit **August 2026**. Do not act mid-semester — URL changes would break live Canvas links during the term.
**Origin:** Student-UX review — class pages link out to a separate Projects site (`chaz-clark.github.io/M119/Projects/`), forcing students to bounce between two sites.
**Origin-Commit:** dbd07b4
**Topic:** merge-projects-site
**Sensitivity:** standard. Both repos are public; no secrets or PII.
**Producer (target repo):** `chaz-clark/M119` (the Projects repo) — it becomes the unified site, so the merge work happens there.
**Companions:**
- `.claude/knowledge/quarto.md` (m119-site) — Quarto/Pandoc gotchas that apply to the merged build.
- `tools/swap_pages_url.py` — the existing Canvas URL-swap tool to repoint external references (lives in m119_master).
- m119_master — upstream generator of the course `.qmd` (class/flex/definitions). It is *not* the producer of this handoff, but the course content originates there; see the open question about the future editing model.

---

# Feature request: unify the course site and the Projects site into one Quarto site

## Decision: merge **course content → Projects foundation** (not the reverse)

The earlier framing ("pull Projects into m119-site") was backwards. Analysis on
2026-05-26 settled the direction:

- **m119-site** is **markdown-only** — class/flex/definition pages just display
  ```r``` blocks; nothing executes. Its CI ([publish.yml]) has no R.
- **M119/Projects** is an **R-rendering Quarto site**. Its pages run real R —
  `probability.qmd` alone has 42 executable `{r}` chunks; unit1–3 +
  project1_practice + RCommands add ~48 more. Its `publish.yml` already does the
  full stack: `quarto setup` + `r-lib/actions/setup-r@v2` (R 4.5.2) +
  `setup-pandoc` + apt system deps (libcurl/ssl/xml2/fontconfig/harfbuzz/…) +
  `setup-renv@v2` (restores `renv.lock`) + render-and-publish to `gh-pages`.

The asymmetry is decisive: **an R-capable site hosts markdown pages for free;
a markdown-only site cannot host R pages without recreating the entire
R + renv + system-deps + freeze stack.** So the unified site must be built on
the **M119/Projects foundation**, and the course content moves into it — not
the other way around.

End state: **M119/Projects becomes the single published site** (course content
+ projects), m119-site retires, and Canvas/external URLs repoint next semester.

## Why this lives in the M119/Projects repo (the producer)

The unified site is built on the **M119/Projects foundation** (it has the R
pipeline), so the merge work — adopting course sections, merging `_quarto.yml`,
moving the schedule machinery, wiring the navbar — happens **in the M119 repo**.
That makes `chaz-clark/M119` the producer; this handoff drops there.

The one upstream dependency: the class/flex/definition pages originate as
**generated** content (m119_master → PMWiki converter). But the conversion is
effectively **one-and-done** as of 2026-05-26 — the maintainer now edits the
`.qmd` directly and pages don't get re-converted. So bringing course content
into M119 is likely a **one-time copy** of the current `.qmd` set, after which
the open question (below) is simply where future edits live. The heavy
"retarget the converter pipeline" framing is probably unnecessary.

## Suggested shape (when revisited post-semester)

1. **Adopt M119/Projects as the base** Quarto project (keep its R pipeline,
   `renv.lock`, `_freeze/`, R-rendering `publish.yml`).
2. **Bring the course content in** as new sections: `class/`, `flex/`,
   `definitions/` (markdown — renders for free under the existing pipeline).
3. **Merge the m119-site-only config pieces** into M119's `_quarto.yml`:
   - MathJax macros `\ds` and `\diff` (in m119-site's `include-in-header`).
   - The **Class Sessions** sidebar + `page-navigation: true` (bottom prev/next).
   - Navbar: combine Home / Definitions / Schedule with the existing
     Projects / Resources menus.
4. **Move the schedule machinery**: `tools/generate_schedule.py`,
   `schedule_config.yml`, `_today.qmd`, and the **Daily Schedule Update**
   workflow.
5. **Rewrite cross-links** from absolute `https://chaz-clark.github.io/M119/Projects/…`
   to relative internal links (grep `site/class/*.qmd` + `site/flex/*.qmd`).
6. **Repoint external references** (Canvas etc.) to the new base URL via
   `tools/swap_pages_url.py` — **next semester only**.
7. **Retire m119-site** (archive or redirect stub) once the unified site is live.

## What's been ruled out

- **Projects → m119-site** — would recreate the entire R/renv/system-deps/freeze
  stack in the bare markdown site. Rejected: rebuilding what already exists.
- **Two sites with cross-links** — doesn't achieve "one site"; students still
  bounce. Rejected per the goal.
- **Static-HTML snapshot of Projects** — loses the live `.qmd`/R source. Rejected.
- **Doing any of this mid-semester** — URL changes break live Canvas links.
  Deferred to post-term (see Trigger).

## Open questions to resolve at execution

- Confirm M119/Projects `_quarto.yml` render list + navbar structure and where
  course sections slot in.
- Decide the future editing model: does m119_master still generate course
  `.qmd` into the unified repo, or does editing move into M119/Projects directly
  (given conversion is one-and-done)?
- Full external-link inventory for `swap_pages_url.py`.
- Confirm the new base URL (`chaz-clark.github.io/M119/…`) and whether the
  eventual `byui-math-dept` org host migration (see `publishing.md`) changes it.

## Acceptance check

- One published Quarto site serves course content **and** projects; every former
  `/M119/Projects/` and `/m119-site/` page is reachable.
- Project pages still render their R output (cache or fresh execution) under the
  R pipeline; course pages render with `\ds`/`\diff` macros + sidebar prev/next.
- No `chaz-clark.github.io/M119/Projects/` or `/m119-site/` absolute links remain
  in the course `.qmd` (grep returns nothing).
- Canvas/external references repointed (swap log updated); old site redirects or
  is archived; no live 404s.

---

## Lifecycle

- **Authored:** 2026-05-26 in m119-site `handoffs/` (Status: draft, **deferred**).
- **Deferred until:** after term end `2026-07-22`; revisit August 2026.
- **Next step (drop), post-semester:** copy into the **M119 (Projects) repo**
  root as `M119-SITE_HANDOFF_merge-projects-site.md`, set Status: delivered.
- **Apply:** M119/Projects maintainer executes the unify-on-Projects-foundation
  plan in that repo, commits, sets Status: applying → applied.
- **Archive:** producer (M119) deletes the dropped copy; this canonical copy
  stays in m119-site `handoffs/` with Status: archived.
