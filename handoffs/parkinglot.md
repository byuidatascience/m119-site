# parkinglot.md

**File:** parkinglot.md
**Direction:** internal
**Status:** parked
**Purpose:** Near-term parked ideas for the `m119-site` repo — "good idea, not fully baked, busy now." Capacity-gated: these would likely be picked up soon if attention were free. NOT committed work — an item scheduled into a sprint leaves this file. See `handoff/CONVENTION.md` → Internal handoffs.
**Last-refined:** 2026-06-08

---

### Site-wide sweep: drop trailing `.` from command-prompt lines ending in inline math

**Status:** **superseded — applied 2026-06-08 in commit `dc79a80`** (97 lines across 30 files, with the multi-sentence safety guard catching the edge cases automatically).

**Trigger:** when a maintainer can afford the visual review (the rule needs human eyes — see below) OR batched with the post-semester content review.
**Routes-to:** sprint (single PR, content review).
**Added:** 2026-06-08
**Origin-Commit:** eb87333

Site-wide audit on 2026-06-08 found **225 lines** with the pattern `<verb> $X$.`
where `<verb>` is one of {`Solve`, `Find`, `Compute`, `Show`, `Write`, `Give`,
`Sketch`, `Determine`, `Identify`, `Calculate`, `State`, `Evaluate`,
`Simplify`, `Differentiate`, `Integrate`, `Estimate`, `Plot`, `Graph`,
`List`, `Assume`, `Verify`} — short imperative prompts where the trailing
period feels awkward (e.g. `- Find any extrema of $A(x) = 1200x - x^2$.`).
These weren't in scope for the earlier display-math sweep (`.$$`) or the
Brain Gains numbering sweep.

The class-27 instances are fixed (commits `9bbd3d2`, `98eae19`, `eb87333`).
The other ~218 span basically every class — sample heads in the audit output:
class-10, 12, 14, 16, 17, 18, 19, 20, 21, 22, … through class-46.

Why not bulk-fix mechanically: the rule needs a human eyeball to skip
multi-sentence cases like class-27:417 (`Find the critical points of
$\ell_1$. This means you must set the first derivative equal to zero and
solve for $a_1$.`) — the trailing period there is grammatically correct
because the line is two sentences. Bulk-stripping would damage those.

Suggested approach for the sweep:

```bash
# rerun the audit to get the current list:
python3 -c "
import re, glob
verbs = r'(Solve|Find|Compute|Show|Write|Give|Sketch|Determine|Identify|Calculate|State|Evaluate|Simplify|Differentiate|Integrate|Estimate|Plot|Graph|List|Assume|Verify)'
for fp in sorted(glob.glob('site/class/*.qmd')):
    in_code = False
    for i, ln in enumerate(open(fp), 1):
        if re.match(r'^\`\`\`', ln): in_code = not in_code; continue
        if in_code: continue
        if re.search(r'\$\.\s*\$', ln):
            s = ln.lstrip(' \t*-1234567890.').lstrip()
            if re.match(verbs + r'\s', s):
                print(f'{fp}:{i}  {ln.rstrip()[:90]}')
"
```

Then review each line — accept the bare-prompt cases (e.g. `- Find any
extrema of $X$.`), reject the multi-sentence ones (e.g. lines where there's
an embedded period mid-line followed by `This means…`).

### Audit bmwoodruff/m119-w26 against every class day, add Solution (R) dropdowns where helpful

**Trigger:** post-semester (after 2026-07-22) OR next time content-review work is scheduled — likely batched with the M119/Projects merge work parked in `HANDOFF_merge-projects-site.md`.
**Routes-to:** sprint
**Added:** 2026-06-08
**Last-refined:** 2026-06-16
**Origin-Commit:** 9bbd3d2 (proof of concept) / `<current>` (audit refinement)

[bmwoodruff/m119-w26](https://github.com/bmwoodruff/m119-w26) has 18 per-day `.R` files (survey on 2026-06-08): `01-09.R`, `01-12.R`, `01-16.R`, `01-20.R`, `01-22.R`, `01-26.R`, `01-29.R`, `01-30.R`, `02-02.R`, `02-03.R`, `02-04.R`, `02-26.R`, `02-27.R`, `03-02.R`, `03-05.R`, `03-09.R`, `03-13.R`, `03-20.R`. Two proofs of concept so far — `02-27.R` → class-27 Brain Gains Q1 (commit `9bbd3d2`), `03-05.R` + `03-09.R` → class-32 Group Meeting "Compare loglikelihood and least squares" + "Another model" (current commit).

**The work — audit-first, then add:**

1. **Walk every class page's existing Solution dropdowns** (Brain Gains, Group Meeting, Discussion, Activities). For each, decide: would adding a parallel `Solution (R)` dropdown using bmwoodruff's matching `.R` content add value? Sometimes yes (computation-heavy answer), sometimes no (pure derivation, no code).
2. **Match by content, not calendar date.** The `MM-DD.R` labels are WI26 dates, not SP26. There's no strict sequential index — `02-27.R` matched our class-27 by *topic* (solving 2×2 systems), and `03-09.R` matched our class-32 by data (`data2_ls.csv` linear-fit problem). Map by what's *taught*, not by file number.
3. **Update data URLs.** bmwoodruff's files reference `byuistats.github.io/M119/...`; our site uses `chaz-clark.github.io/M119/...`. Update on import so students can run the code without 404s.
4. **Attribution format:** standard footer line in each new dropdown — `Source: [<file>.R](https://github.com/bmwoodruff/m119-w26/blob/main/<file>.R)`. If the code is adapted (e.g. swapped a model), note "Adapted from".
5. **Note for students:** when a class has classroom-permitted reuse for homework (like class-32 today), add a single short sentence in the dropdown — "OK to use this pattern on the related homework." Verbatim from maintainer guidance.
6. **Skip days where it wouldn't help** — pure-derivation pages, definition pages, or pages whose Solution is already a one-line algebraic answer.

**Pattern is purely additive** — existing math Solutions stay, R dropdowns sit alongside them. UX win: students who want the computational answer get it without context-switching to GitHub. Aligns with the broader "executable cells inline" direction noted in `HANDOFF_merge-projects-site.md`'s Enhancement section — though THAT one needs CI-side R support, while these R cells stay as copy-paste blocks until the M119/Projects merge unlocks inline execution.

**Deferred because:** (a) mid-semester URL/content changes risk breaking student bookmarks and live Canvas links; (b) ~18 files × multiple dropdowns each is a sustained effort that wants dedicated focus, not piecemeal additions. Best done as a contiguous sprint after the term wraps.
