**Date:** 2026-05-26
**Author:** Claude (agent) + m119-site
**Direction:** request
**Status:** draft — **DEFERRED**
**Trigger:** after the SP26 semester ends (term end `2026-07-22` per `schedule_config.yml`). Revisit **August 2026**. Do not act mid-semester — URL changes would break live Canvas links during the term.
**Origin:** Student-UX review — class pages link out to a separate Projects site (`chaz-clark.github.io/M119/Projects/`), forcing students to bounce between two sites.
**Origin-Commit:** dbd07b4
**Topic:** merge-projects-site
**Sensitivity:** standard. Both repos are public; no secrets or PII.
**Producer (target repo):** `chaz-clark/M119` (the Projects repo) — it becomes the unified site, so the **site-build** work happens there.
**Companions:**
- `.claude/knowledge/quarto.md` (m119-site) — Quarto/Pandoc gotchas that apply to the merged build.
- **Companion handoff (to m119_master), fired after the M119 build lands:** m119_master owns the **link updates** — rewriting course cross-links to relative internal links, and repointing external Canvas references via its `tools/swap_pages_url.py`. The course `.qmd` are generated/owned by m119_master, so link edits must happen in the source of truth, not the published output. See "Responsibility split" below.

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

End state: **M119/Projects becomes the new master (canonical published) site** —
course content + projects in one place — and **m119-site retires**. This also
fits the note in `publishing.md` that m119-site was always a *temporary* host;
M119 becoming the master site supersedes it. Canvas/external URLs repoint next
semester (m119_master's job — see Responsibility split).

(There is no literal open GitHub PR to close — m119-site, m119_master, and M119
all have zero open PRs as of 2026-05-26. "Closing the PR" here means winding
down m119-site as a standalone site once M119 is the master.)

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
5. **Link updates are m119_master's responsibility** (see split below) — both
   the in-page course cross-links and the external Canvas repointing.
6. **Retire m119-site** once the unified site is live — archive the repo or
   leave a redirect stub to the M119 master site. m119-site stops being a
   standalone published site.

## Responsibility split (who owns what)

The build and the links are owned by different repos, because the course `.qmd`
are owned by m119_master:

| Work | Owner | Why |
|---|---|---|
| Adopt Projects as base, merge `_quarto.yml`, move schedule machinery, wire navbar, host course sections | **M119/Projects** (producer) | The unified site is built here (R pipeline lives here). |
| Rewrite course cross-links from `https://chaz-clark.github.io/M119/Projects/…` → relative internal links | **m119_master** | The class/flex/definition `.qmd` are owned/generated by m119_master; hand-patching them in M119 would drift / be overwritten. |
| Repoint external references (Canvas, syllabus) to the new base URL | **m119_master** | `tools/swap_pages_url.py` and the URL-swap logs live in m119_master. **Next semester only.** |

This implies a **companion handoff to m119_master** for the link work, fired once
the M119 unify lands — so the cross-link rewrite and Canvas swap happen in the
source of truth, not the published output. The M119 build (this handoff) and the
m119_master link updates are sequenced: build first, then links.

## What's been ruled out

- **Projects → m119-site** — would recreate the entire R/renv/system-deps/freeze
  stack in the bare markdown site. Rejected: rebuilding what already exists.
- **Two sites with cross-links** — doesn't achieve "one site"; students still
  bounce. Rejected per the goal.
- **Static-HTML snapshot of Projects** — loses the live `.qmd`/R source. Rejected.
- **Doing any of this mid-semester** — URL changes break live Canvas links.
  Deferred to post-term (see Trigger).

## Enhancement opportunity unlocked by the merge

Once the unified site is built on the R-capable M119/Projects foundation,
**executable R worksheets inline on the page** become feasible across the
course. m119-site can already ship *downloadable* `.qmd` worksheets — the
class-25 "Visualizing $f, f', f''$" activity at `site/assets/docs/visualizing_derivatives.qmd`
is the proof-of-concept, served as a static resource via a `!assets/**/*.qmd`
negation in `_quarto.yml`'s `render:` list (Quarto copies but doesn't render
it; students download and run in their own RStudio). That's the markdown-only
workaround for "no R in CI."

On the merged site this becomes **inline-executable** instead of
download-then-run:

- Author the worksheet as a normal page with `{r}` executable chunks — no
  separate downloadable file needed. CI executes R during render and ships the
  resulting plots/tables inline.
- Drop the `!assets/**/*.qmd` exclusion in `_quarto.yml` (it exists only to
  protect markdown-only m119-site CI from R-bearing files).
- Same pattern applies broadly to any class page where R is currently
  copy-paste — Brain Gains plotting boxes, the loglikelihood partial-derivative
  material in class-24 and class-26, the optimization plots in class-25, etc.

UX improvement: students see the immediate-feedback plots without leaving the
page or running anything locally. The current downloadable pattern stays valid
for "I want to mess with the code myself" — both modes coexist on the merged
site. Out of scope for the core merge work but a natural follow-up sprint.

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
  **site build** in that repo, commits, sets Status: applying → applied.
- **Companion (link updates):** once the M119 build lands, fire a second handoff
  to **m119_master** for the course cross-link rewrite + Canvas/external
  repointing (`swap_pages_url.py`) — done in the source of truth, next semester.
- **Archive:** producer (M119) deletes the dropped copy; this canonical copy
  stays in m119-site `handoffs/` with Status: archived.
