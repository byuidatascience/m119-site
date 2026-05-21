# Handoff: LaTeX Pattern B (inline run-on `=` chains) — deferred for surgical pass

**Date:** 2026-05-18
**Author:** Claude (in-session audit)
**Status:** deferred — captured for later surgical review
**Direction:** internal note (no cross-repo transfer)

---

## Context

Companion to the 2026-05-18 LaTeX hygiene sweep that bulk-fixed:

- **Pattern A** — 173 instances of spaced inline math `$ X $` (renders as literal `$` text). Mechanical bulk-fix applied across 24 class files.
- **Pattern D** — 10 single-line display-math chains converted to `\begin{aligned}` blocks (out of 22 audit hits — 12 were subscript-`=` false positives).

This handoff records the 109 **Pattern B** findings deferred from that sweep.

## Pattern B definition

Inline math `$X = Y = Z = …$` with **3 or more `=` signs in a single inline segment**. These render correctly (math mode works fine), but a long chain inline reads as a visually run-on line.

The fix when warranted: convert to a display block aligned at `=`:

```
$$
\begin{aligned}
X &= Y \\
  &= Z \\
  &= W
\end{aligned}
$$
```

## Why deferred (not bulk-fixed)

Three categories are mixed inside the 109 findings, and the right call differs per case:

1. **Genuine long chains worth aligning.** Example: `$(f_x)_x = f_{xx} = \dfrac{\partial}{\partial x}\left(\dfrac{\partial f}{\partial x}\right) = \dfrac{\partial^2 f}{\partial x^2}$` (class-23.qmd:88–91). Long, hard to scan inline — convert.
2. **Short answer-key chains, OK as inline.** Example: `$P(X = 4) = p(4;2) = 0.09022352$` (class-14.qmd:93). Short and reads naturally; aligning would over-format.
3. **False positives — parameter lists, not chains.** Example: `$a = 1, b = 2, c = 5, d = -2$` (class-5.qmd:52). Multiple `=` but each is independent; aligning would make it worse.

Bulk conversion would catch #3 wrongly and over-format #2. Per-file judgment needed.

## Findings by file (counts)

| File | Hits | Notes |
|---|---|---|
| class-13.qmd | 12 | Probability answer keys (dice). Mostly short chains — leave inline. |
| class-14.qmd | 7 | Prep answer keys. Mostly short. Leave inline. |
| class-30.qmd | 8 | Loglikelihood derivations. **Long** — convert most. |
| class-22.qmd | 4 | Chain-rule chains. Convert. |
| class-23.qmd | 4 | Partial-derivative notation `(f_x)_x = f_{xx} = \dfrac{\partial}{\partial x}(...)`. **Long** — convert. |
| class-5.qmd | 9 | Parameter lists `$A=1, B=1, C=0, D=0$`. **NOT a chain — false positives, skip.** |
| class-9.qmd | 3 | Log identities. Short, leave inline. |
| class-20.qmd | 5 | Long derivative quotient/product expressions. Convert. |
| class-13.qmd | (covered above) | |
| class-38.qmd | 4 | Definite integrals. Long — convert. |
| class-39.qmd | 5 | CDF integrals. Long — convert. |
| class-40.qmd | 4 | Exponential RV `E[X]`, `Var[X]`. Long — convert. |
| class-2.qmd | 1 | Polynomial def. Long — convert. |
| class-27.qmd | 2 | Linear system. Convert. |
| class-28.qmd | 3 | Likelihood partial derivatives. Convert. |
| class-29.qmd | 2 | Partial derivatives. Convert. |
| class-31.qmd | 1 | Already covered in Pattern D pass. |
| class-32.qmd | 1 | Convert. |
| class-33.qmd | 6 | CDF / expected value chains. Convert. |

(The full audit output with exact line numbers and source text is in the git log of the 2026-05-18 sweep commit.)

## How to run the audit again

```bash
cd site/class
python3 -c "
import re, glob

def tokenize(line):
    out, i, n = [], 0, len(line)
    while i < n:
        if line[i] == '$':
            if i+1 < n and line[i+1] == '\$':
                j = line.find('\$\$', i+2)
                if j < 0: break
                i = j + 2; continue
            j = line.find('\$', i+1)
            if j < 0: break
            out.append((i, line[i+1:j]))
            i = j + 1
        else:
            i += 1
    return out

for fp in sorted(glob.glob('*.qmd')):
    for ln, line in enumerate(open(fp), 1):
        for _, content in tokenize(line):
            if content.count('=') >= 3:
                print(f'{fp}:{ln}: \${content}\$')
"
```

## Recommended next pass

Tackle one file at a time, in order of visual pain:

1. **class-23** (partial-derivative notation, most legitimate "long chain" use case)
2. **class-38, class-39, class-40** (integral expressions — these are the visually worst)
3. **class-30** (likelihood derivations)
4. **class-22, class-28, class-29** (chain-rule / partial derivatives)

Skip: **class-5** (parameter lists, not chains).

Leave inline (acceptable as-is): **class-13, class-14, class-9** short answer-key chains.

---

*Companion to the 2026-05-18 LaTeX hygiene sweep commit.*
