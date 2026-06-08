# parkinglot.md

**File:** parkinglot.md
**Direction:** internal
**Status:** parked
**Purpose:** Near-term parked ideas for the `m119-site` repo — "good idea, not fully baked, busy now." Capacity-gated: these would likely be picked up soon if attention were free. NOT committed work — an item scheduled into a sprint leaves this file. See `handoff/CONVENTION.md` → Internal handoffs.
**Last-refined:** 2026-06-08

---

### Pull R Solution dropdowns from bmwoodruff/m119-w26 for every class day

**Trigger:** post-semester (after 2026-07-22) OR next time content-review work is scheduled — likely batched with the M119/Projects merge work parked in `HANDOFF_merge-projects-site.md`.
**Routes-to:** sprint
**Added:** 2026-06-08
**Origin-Commit:** 9bbd3d2

[bmwoodruff/m119-w26](https://github.com/bmwoodruff/m119-w26) has per-day `.R` files (18 as of survey on 2026-06-08: `01-09.R`, `01-12.R`, `01-16.R`, `01-20.R`, `01-22.R`, `01-26.R`, `01-29.R`, `01-30.R`, `02-02.R`, `02-03.R`, …, `02-27.R`, …, `03-02.R`, `03-05.R`, `03-09.R`, `03-13.R`, `03-20.R`). On 2026-06-08 we pulled the Q1 portion of `02-27.R` into class-27 Brain Gains Q1 as a new "Solution (R)" dropdown alongside the math Solution (commit `9bbd3d2`). Pattern is reusable: each problem that has a closed-form solution gets a parallel R cell that students can copy-paste.

The work:

1. Map bmwoodruff's WI26 date labels (`MM-DD.R`) to our SP26 class day numbers. The date labels are off — they're WI26 (Winter 2026) semester dates, not SP26 (Spring 2026). The mapping is by *sequential class meeting*, not calendar date: bmwoodruff's `01-09.R` ↔ our Class 1, `01-12.R` ↔ Class 2, etc. Watch for any gaps — WI26 and SP26 may have skipped different holidays.
2. For each bmwoodruff `.R` file, identify which problems on the corresponding class page it covers (sometimes one file spans all Brain Gains + activities for that day, sometimes only one section).
3. Add a `Solution (R)` dropdown next to each existing math `Solution` dropdown, containing the relevant code with attribution: `Source: [<file>.R](https://github.com/bmwoodruff/m119-w26/blob/main/<file>.R)`.
4. Skip days where the code wouldn't add anything (e.g. pure-derivation days, no computation step).

This is **purely additive** — the existing math Solutions stay; the R dropdowns sit alongside them. UX win: students who want to see the computational answer get it without context-switching to a separate file. Aligns with the broader "executable cells inline" direction noted in `HANDOFF_merge-projects-site.md`'s Enhancement section — though THAT one needs CI-side R support, while these R cells stay as copy-paste blocks until the M119/Projects merge unlocks inline execution.

Deferred because: (a) mid-semester URL/content changes risk breaking student bookmarks and live Canvas links; (b) 18 files × ~3 dropdowns each is a sustained effort that wants dedicated focus, not piecemeal additions. Best done as a contiguous sprint after the term wraps.
