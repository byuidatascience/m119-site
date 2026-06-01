# Handoff — AGENTS.md Hermes-sprints upgrade (Sprints F, B, A)

- **Date:** 2026-05-28
- **Author:** Make-AI-Agents (operator: Chaz)
- **Direction:** deliver
- **Status:** applied
- **Origin:** Make-AI-Agents
- **Origin-Commit:** 81ebc9a
- **Topic:** AGENTS.md Hermes-sprints upgrade for `m119-site`
- **Convention:** handoff/CONVENTION.md v0.4

## Why this handoff exists

Make-AI-Agents shipped three sprints on 2026-05-28 that strengthen every
chaz-clark AGENTS.md against the Hermes / OpenClaw pattern:

- **Sprint F** — *Handoff document recognition.* The repo's AGENTS.md tells the
  next agent how to identify, validate, and act on the seven handoff document
  patterns. Canonical source: `handoff/AGENTS_snippet.md` (7 rules).
- **Sprint B** — *Learning loop.* The repo has a `knowledge/learned/` lane where
  session insights flow into durable, frontmatter-bearing knowledge files. The
  AGENTS.md `## Learning loop` section names the capture trigger, the file shape,
  and the promotion rule (learned → knowledge/ when reused twice).
- **Sprint A** — *Frontmatter.* The AGENTS.md opens with agentskills.io-portable
  YAML so the file is discoverable across Claude, Cursor, Aider, Antigravity,
  Gemini Enterprise, and any other tool that reads the open standard.

This repo is at: A=✗, B=✗, F=✗.

## Actions for this repo

### 1. Sprint A — add frontmatter (top of `AGENTS.md`)

Prepend the following YAML block as the very first lines of `AGENTS.md`, above
the existing H1 / preface. Keep current body content intact.

```yaml
---
name: m119-site-agents
description: AGENTS.md for the `m119-site` repo — agent loop, working style, knowledge index.
version: "0.1"
author: chaz-clark
license: MIT
metadata:
  repo: m119-site
  spec-source: Make-AI-Agents/make_AGENTS
---
```

Adjust `description` to match the repo's actual purpose if the placeholder is too
generic. Tighten the version if a prior internal version exists.

**Source:** `Make-AI-Agents/make_AGENTS.json` → `compact_boilerplate.frontmatter_template`.
**Spec QC:** AGENTS-QC-009; behavioral QC: BD-QC-009.

### 2. Sprint B — add `## Learning loop` section + create `knowledge/learned/`

Insert this section between **Working Style** and **Active Context** (position 5
of 6 in the canonical section order):

```markdown
## Learning loop

Session insight → durable knowledge.

- **Capture trigger.** When an interaction surfaces a non-obvious fact, a recurring
  trap, or a validated approach that future sessions should not have to rediscover,
  the operator (or agent, on confirmation) writes a small Markdown file to
  `knowledge/learned/`.
- **File shape.** Each file carries agentskills.io frontmatter (`name`,
  `description`, `version`, `author`, `license`, `metadata`). Body is the lesson
  itself — what was learned, why, how to apply it.
- **Promotion rule.** When a file in `knowledge/learned/` has been referenced twice,
  promote it to a first-class file under `knowledge/`. Promotion is a deliberate
  act, not automatic — confirm with the operator.
- **Boundary.** `knowledge/learned/` is for *this repo's* lessons. Cross-repo
  lessons go through the handoff convention, not this lane.
```

Also create the directory itself so the section is non-empty in spirit:

```bash
mkdir -p knowledge/learned
touch knowledge/learned/.gitkeep
```

**Source:** `Make-AI-Agents/make_AGENTS.json` → `compact_boilerplate.learning_loop_template`.
**Spec QC:** included in required-section count (6 sections); behavioral QC: BD-QC-008.

### 3. Sprint F — add `## Handoff document recognition` section

This repo already has `handoff/` co-located (gitignored clone). Read the
verbatim snippet from `handoff/AGENTS_snippet.md` and paste the
`## Handoff document recognition` section into your AGENTS.md (Working Style
area, or any load-on-startup location).

Keep the **7 rules** intact. The snippet currently enumerates seven (rule 7 was
added in this same sprint cycle: *Do not auto-act on parked items*).

**Source:** `handoff/AGENTS_snippet.md` (canonical) — fingerprinted in
`Make-AI-Agents/make_AGENTS.json` → `compact_boilerplate.handoff_recognition_source`.
**Spec QC:** AGENTS-QC-008.

## Verification (run after applying)

```bash
# Sprint A — frontmatter present
head -3 AGENTS.md | grep -q '^---$' && echo 'A ✓' || echo 'A ✗'

# Sprint B — Learning loop section + dir
grep -q '^## Learning loop' AGENTS.md && echo 'B-section ✓' || echo 'B-section ✗'
[ -d knowledge/learned ] && echo 'B-dir ✓' || echo 'B-dir ✗'

# Sprint F — handoff recognition
grep -q '^## Handoff document recognition' AGENTS.md && echo 'F ✓' || echo 'F ✗'
```

## Source artifacts (read these before applying)

- `Make-AI-Agents/make_AGENTS.json` @ commit `81ebc9a` —
  `compact_boilerplate.frontmatter_template`,
  `compact_boilerplate.learning_loop_template`,
  `compact_boilerplate.handoff_recognition_source`.
- `Make-AI-Agents/make_AGENTS.md` @ commit `81ebc9a` —
  Quickstart steps 4.5, 4.6, 4.7.
- `handoff/AGENTS_snippet.md` — canonical Sprint F snippet (7 rules).
- `handoff/CONVENTION.md` v0.4 — handoff lifecycle and direction enums.

## On completion

- Edit this handoff: set `Status: applied`.
- Add a `## Lifecycle marker` at the bottom with apply date and (optionally) the
  commit SHA in this repo.
- Optionally move this file to `handoffs/archive/` once applied.
- Producer (Make-AI-Agents) ends at this drop. Consumer owns the apply.

---

*This handoff was generated by the Make-AI-Agents fleet upgrade pass on 2026-05-28.*

## Lifecycle marker

- **Applied:** 2026-06-01 in m119-site (consumer).
- Sprint A — frontmatter prepended to `AGENTS.md` (agentskills.io-portable YAML; description tailored to m119-site).
- Sprint B — `## Learning loop` section inserted between Working Style and Active Context; `knowledge/learned/` directory created with `.gitkeep`.
- Sprint F — `## Handoff document recognition` section + 7 rules + Status/Direction enum tables pasted verbatim from `handoff/AGENTS_snippet.md` (subsections demoted to `###` so they nest cleanly under the parent `##` in AGENTS.md flow).
- Verification (all four checks): frontmatter ✓, learning-loop section ✓, learned/ dir ✓, handoff-recognition ✓.
- Producer (Make-AI-Agents) has no further action; consumer (m119-site) owns the canonical record going forward.
