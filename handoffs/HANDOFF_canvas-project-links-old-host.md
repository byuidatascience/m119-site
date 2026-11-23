**Date:** 2026-11-23
**Author:** Claude (agent) + m119-site
**Direction:** request
**Status:** delivered
**Origin:** A student reported that the Project 3 links in Canvas are broken (`https://chaz-clark.github.io/M119/Projects/unit3.html` and `...unit3.html#task-1-data-and-general-models` both return 404).
**Origin-Commit:** eded15e
**Topic:** canvas-project-links-old-host
**Sensitivity:** standard. No student data; the course ID and item titles only.
**Producer (target repo):** m119-master (owns Canvas course content and Canvas writes)
**Companions:**
- m119-site PR #29 (`eded15e`): publishes the two `m119-docs` pages that were 404 on the new site, so every replacement target below now resolves.
- `.claude/knowledge/urls-canvas.md` (m119-site): the mapping table there is now out of date. Update it after this handoff is applied.

---

# Request: repoint the Canvas project links from the dead `chaz-clark.github.io/M119` host to `byuidatascience.github.io/m119-site`

## The problem

The old Projects site `chaz-clark.github.io/M119` is gone, and every URL on it returns 404. The live Canvas course still links to it in 36 places. During the August FA26 migration only the homepage button was repointed (see `2026-08-17_canvas-integration-complete.md`). The weekly Links pages, the assignment descriptions, and the module link items were never changed.

## The fix: one prefix swap

```
https://chaz-clark.github.io/M119/Projects/   →   https://byuidatascience.github.io/m119-site/projects/
```

The `P` in `Projects` becomes a lowercase `p`. The rest of each URL, including the `#anchor`, stays the same.

Verified on 2026-11-23: all 25 distinct old URLs in Canvas have a live replacement that returns HTTP 200, and every `#anchor` exists as an `id` on its new page. Two pages (`m119-docs/GreekLetters.html` and `m119-docs/ExampleProject_Task2.html`) were 404 on the new site until m119-site PR #29 merged today. Both now return 200.

## Where the old links are (live Canvas, course 425166)

These come from a read-only API scan of the live course on 2026-11-23: pages, assignments, discussions, module items and the syllabus. **36 items, 48 links.** Nothing was written to Canvas.

**Pages (13, one link each, all published)**
- Math 119 Weekly Rhythm
- Project 1 Task 1 Links, Task 2 Links, Task 3 Links, Task 4 Links, Final Links
- Project 2 Task 1 Links, Task 2 Links, Task 3 Links, Final Links
- Project 3 Task 1 Links, Task 2 Links, Final Links

**Assignment descriptions (12, two links each)**
- Project 1 / 2 / 3 (the parent assignments are unpublished)
- Project 1 Task 1–4 Cohesive Narrative (published)
- Project 2 Task 1–3 Cohesive Narrative (published)
- Project 3 Task 1–2 Cohesive Narrative (published)

**Module external-URL items (11, published)**
- Project 1 / 2 / 3 Instructions (one in each project module)
- Additional Resources: Commonly used Greek Letters; Derivative Rules, Log Properties, and Properties of Sums; Example Project Task 1; Example Project Task 2; Project 1 Task 1 Example; Project 1 Task 2 Example (f2); Project 2 Task 1 Example (f1); Project 2 Task 2 Example (f6)

No hits in discussions or the syllabus.

## ⚠️ Do not fix this with a full `canvas_sync --push`

`canvas_sync.py --status` reports **76 locally modified files** in `course/` that were never pushed to Canvas. They include the week 9–14 class-prep reminders, the AI-101 pages, `project-1-ready-for-review.json`, and several of the Links pages above. A full push would publish all of them to students along with the link fix. A full `--pull` would overwrite them. Find out what those edits are before running either command.

Instead, **update only the 36 items above.** `tools/swap_pages_url.py` already does this kind of targeted update (it scans the course, logs every hit, defaults to a dry run, and writes only with `--apply`). Before it can be reused here it needs two changes:
- It loads `.env` from `/Users/chazclar/Documents/GitHub/m119_master/` (underscore). The repo folder is now `m119-master`.
- Its `OLD`/`NEW` constants are set for the April 2026 migration. Set them to the prefix pair above. Matching must be case-sensitive on `/M119/Projects/`.

## Done when

1. A dry run of the swap lists the same 36 items / 48 links.
2. After `--apply`, a re-scan finds 0 occurrences of `chaz-clark.github.io/M119` in course 425166.
3. The Project 3 Task 1 Links page opens `projects/unit3.html` and jumps to the Task 1 section.
4. The local `course/` copies of these items are updated to match, so a later push doesn't put the old URLs back.
5. You reply to m119-site so `.claude/knowledge/urls-canvas.md` can be updated.

## Lifecycle marker

- 2026-11-23: authored and delivered (m119-site).
