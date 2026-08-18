# Site Enhancements - Fall 2026

**Date**: 2026-08-17
**Purpose**: Track student support improvements to m119-site for Fall 2026 semester

---

## Enhancement Map

### Enhancement #1: Quick Reference Hub ⏳

**Status**: Pending
**Files Created**:
- `site/resources.qmd` (NEW)

**Files Modified**:
- `site/_quarto.yml` (add Resources to navbar)

**How to Remove**:
1. Delete `site/resources.qmd`
2. In `site/_quarto.yml`, remove the Resources navbar entry:
   ```yaml
   - text: "Resources"
     href: resources.qmd
   ```
3. Rebuild site: `quarto render site/`

**Content Sections**:
- R Syntax Quick Reference (uniroot, plotting, functions)
- Mathematica Syntax Quick Reference (Integrate, Solve, percentiles)
- Math Formulas (derivative rules, chain rule, log properties, probability)
- Common Errors and Fixes

---

### Enhancement #2: Getting Started Guide ⏳

**Status**: Pending - CHECK EXISTING FIRST
**Note**: User mentioned setup instructions already exist, and Positron should be the only option (not RStudio)

**Action**:
1. Find and review existing setup instructions
2. Either enhance existing OR create new consolidated guide
3. Ensure Positron is the recommended IDE (not RStudio)

**Files Created** (if new):
- `site/getting-started.qmd` (NEW)

**Files Modified** (if enhancing existing):
- TBD - find existing setup docs first

**How to Remove**:
1. If new file: Delete `site/getting-started.qmd`
2. If enhanced existing: `git checkout HEAD -- <filename>`
3. Rebuild site: `quarto render site/`

**Content Sections**:
- Week 1 Setup Checklist (R, Positron, Mathematica)
- Positron installation instructions with BYU-I specific links
- Test scripts to verify setup
- R template for first assignment
- Troubleshooting common install issues

---

### Enhancement #3: Common Errors FAQ ⏳

**Status**: Pending
**Files Created**:
- `site/common-errors.qmd` (NEW)

**Files Modified**:
- `site/resources.qmd` (add link to Common Errors FAQ)

**How to Remove**:
1. Delete `site/common-errors.qmd`
2. In `site/resources.qmd`, remove link to Common Errors
3. Rebuild site: `quarto render site/`

**Content Sections**:
- R Errors (f not found, uniroot interval errors, syntax)
- Mathematica Errors (integration, solving, syntax)
- Math Errors (derivative mistakes, domain errors, algebra)
- Each error with copy-paste fix

---

### Enhancement #4: Topic Index ⏳

**Status**: Pending
**Files Created**:
- `site/topics.qmd` (NEW)

**Files Modified**:
- `site/_quarto.yml` (add Topics to navbar OR as dropdown under Resources)

**How to Remove**:
1. Delete `site/topics.qmd`
2. In `site/_quarto.yml`, remove Topics navbar entry
3. Rebuild site: `quarto render site/`

**Content Sections**:
- Searchable/browsable topic → class mapping
- Topics: Chain Rule, Optimization, uniroot, Maximum Likelihood, Derivatives, Integration, Probability, etc.
- Each topic links to relevant class sessions

---

## Implementation Status

| Enhancement | Status | Files | Commit |
|-------------|--------|-------|--------|
| #1 Quick Reference Hub | ✅ Complete | resources.qmd | — |
| #2 Getting Started | ⏸️ Deferred | — | See existing setup in class-3, class-4 |
| #3 Common Errors FAQ | ✅ Complete | common-errors.qmd | — |
| #4 Topic Index | ✅ Complete | topics.qmd | — |

---

## Quick Removal Commands

**Remove all enhancements at once**:
```bash
# Delete all new files
rm site/resources.qmd site/getting-started.qmd site/common-errors.qmd site/topics.qmd

# Revert _quarto.yml to previous navbar
git checkout HEAD -- site/_quarto.yml

# Revert index.qmd if modified
git checkout HEAD -- site/index.qmd

# Rebuild
quarto render site/
```

**Remove individual enhancement**:
```bash
# Example: Remove just the Getting Started guide
rm site/getting-started.qmd
# Then manually remove link from site/index.qmd
# Rebuild
quarto render site/
```

---

## Design Principles

All enhancements follow these principles:
1. **Self-contained**: Each page stands alone (can be removed independently)
2. **No code changes**: Pure content additions (no site logic changes)
3. **Clearly marked**: Comments indicate "Enhancement #X" in files
4. **Reversible**: Simple deletion or git revert works

---

## Testing Checklist

Before semester starts:
- [ ] All links work (no 404s)
- [ ] Mobile responsive (students use phones)
- [ ] Search works (if using Quarto search)
- [ ] Print-friendly (students may print reference sheets)
- [ ] Accessible (screen readers, color contrast)

---

## Feedback Collection

**During Fall 2026**:
- Note which resources students actually use (Google Analytics? Manual tracking?)
- Ask in mid-semester survey: "Which site resources were helpful?"
- Remove unused enhancements after semester

---

## Previous Enhancements (Already Complete)

✅ **Strategic Answer Boxes** (Aug 17, 2026)
- Added 7 answer boxes to classes 11, 12, 26, 42
- Commit: `28265c6` - "feat: add 7 strategic answer boxes for fast feedback loops"
- Files: class-11.qmd, class-12.qmd, class-26.qmd, class-42.qmd
- How to remove: Revert commit or manually delete `<details>` blocks

✅ **Projects Integration** (Aug 17, 2026)
- Integrated 163 project files locally
- Created site/projects/ directory
- Updated 54 class links from external to local
- Commit: Multiple commits Aug 17
- How to remove: `rm -rf site/projects/` and revert links to chaz-clark.github.io

✅ **Fall 2026 Calendar** (Aug 17, 2026)
- Updated schedule_config.yml to Fall 2026 dates
- Added holidays and instructor travel dates
- Regenerated schedule with 54 class days
- How to remove: Revert schedule_config.yml and regenerate

---

**End of Enhancement Map**
