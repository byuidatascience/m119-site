---
name: comprehensive-scan-first
description: When discovering a pattern of errors, do comprehensive scan upfront instead of reactive fixes
version: 1.0
author: Claude + Chaz
license: MIT
metadata:
  date_learned: 2026-07-12
  context: Mathematica code blocks missing language identifiers
  trigger: User asked "why do we keep finding more?"
  session: m119-site comprehensive code block fix
---

# Lesson: Comprehensive Scan First, Not Reactive Fixes

## What Happened

User reported Mathematica code blocks in class-42 weren't copy-pasteable (missing `mathematica` language identifier).

**Reactive approach taken (wrong)**:
1. Fixed class-42 (3 blocks)
2. Committed and pushed
3. User reported class-43 has same issue
4. Fixed class-43 (5 blocks)
5. Committed and pushed
6. User asked: "why do we keep finding more?"
7. **Finally** did comprehensive scan → found 21 MORE blocks across 5 files

## The Problem

**Reactive approach** = fix what's reported, wait for next report
- Inefficient (multiple commits for same issue)
- Frustrating for user (they become the scanner)
- Incomplete (always wondering "are there more?")

**Comprehensive approach** = when you find a PATTERN, scan everything immediately
- One commit fixes all instances
- User confidence that it's complete
- Systematic vs. ad-hoc

## The Pattern

**When to scan comprehensively:**
- Same type of error in multiple files
- Systematic issue (e.g., syntax pattern, missing attributes)
- User reports second instance of same issue
- Fix is mechanical/repetitive

**Behavioral trigger**: Second occurrence of same error type → STOP and scan ALL files

## How to Do It Right

1. **Recognize the pattern** - "This isn't a one-off error"
2. **Define the search** - What exact pattern am I looking for?
3. **Use Task agent or Grep** - Scan entire codebase comprehensively
4. **Fix all instances** - One batch operation
5. **Commit once** - Complete fix in single commit

## Example: Mathematica Code Blocks

**Wrong** (what I did):
```
User reports class-42 → fix class-42 → commit
User reports class-43 → fix class-43 → commit
User asks "why do we keep finding more?"
Finally scan all → find 21 more blocks → commit
```

**Right** (what I should have done):
```
User reports class-42 → recognize pattern
→ Scan ALL class/*.qmd files for unlabeled Mathematica blocks
→ Fix all 29 blocks (3+5+21) at once → commit once
```

## Aligns With

- **P-011 Genchi Gembutsu**: Go and see - don't assume there's only one
- **P-011 Jidoka**: Fix the root cause, not symptoms
- **P-011 Poka-yoke**: Prevent recurrence by fixing systematically

## Application

Next time I see a second occurrence of the same type of error:
1. STOP reactive mode
2. Launch Task agent with comprehensive search
3. Fix all instances in one pass
4. Document in knowledge if it's a gotcha

## Success Criteria

This lesson is "learned" when:
- I catch myself after the SECOND instance and scan comprehensively
- No more "why do we keep finding more?" moments
- One commit per systematic issue, not one per file
