# Quarto authoring & layout gotchas

**When to read:** editing `.qmd` content (math, lists, tables) or the Quarto
site config (`_quarto.yml`, `styles.css`) for navigation/layout. Companion to
`converter.md` (conversion pipeline) and `publishing.md` (CI/deploy).

## Inline math: no whitespace next to the `$`

`$ X $` — a space right after the opening `$` or before the closing `$` — does
**not** render as math. Pandoc emits it as literal `$` text. Always write `$X$`.

- Verified: `$ [a, b] $` renders as literal "`$ [a, b] $`" in the HTML; `$[a, b]$`
  renders as math.
- Hits answer keys hardest. To find them, walk a `$`-tokenizer (alternate
  in/out of math on each `$`, skip `$$…$$`); a plain regex false-positives on
  prose like `$x$ … $y$`.
- 173 instances were fixed across 24 class pages on 2026-05-18.

## Horizontal rules: use `***` or `---`, never `----`

A line of **4+ dashes** (`----`) is parsed as a single-column pipe-table
separator and **swallows everything below it into a table** until the next
`---`. In class-15 a `----` between two discussion blocks ate Group Meeting,
the Activity headers, and the entire second Discussion section. Use `***` (or
3-dash `---`) for a thematic break.

## ATX headers need a blank line before them

A line of `#`/`##`/`###`/… immediately after a prose paragraph (no blank line
between) gets absorbed into that paragraph as inline text — the header
disappears and you see `#### Section title prose continues…` run together. Add
a blank line before every `#`-style header. Seen on 6 class-page headers
(class-23 ×2, class-25, class-33, class-43b, class-45) in the 2026-05-29 sweep.
The same rule applies to lists (next section) and to anchors followed by
headings (`<a id="…"></a>` immediately above `##` — converter.md gotcha #1).

## Lists need a blank line, a real parent, and content on the marker line

- `- ` / `1. ` immediately after a prose paragraph collapses into the
  paragraph → put a blank line before the first marker.
- Bullets/numbers indented 4 spaces with **no parent list item** render as an
  indented **code block** (raw `$…$`, no math) or as run-on inline text.
  Either dedent to column 0 or give them a real parent. Seen twice:
  class-16 "Introduction to Linearization" (ran on) and the class-20
  Linearization answer key (rendered as a literal code block).
- For lettered sub-answers use a real nested list (`a.`/`b.`/`c.` under a
  numbered parent), not 4-space-indented `1.` with no parent.
- **Empty marker** — `2.` (or `1.`) on its own line with content on the
  *next* line is parsed as an empty list item, and the content becomes a
  separate paragraph (not list-item content). Put the content on the marker
  line: `2. Use the information about …`. Seen in class-22 chain-rule
  exercise (questions 2 and 3 had empty `2.` / `3.` markers).

## Numbered items separated by `<details>` blocks ("all 1." bug)

Pandoc's auto-numbering with repeated `1.` works **only within a contiguous
list**. If items are separated by `<details>…</details>` blocks (very common for
answer/solution dropdowns), each `1.` starts a fresh single-item ordered list
— and in many themes the marker chrome on a one-item list is dropped, so the
items appear numberless or all as "1.".

**Always write Brain Gains / question sections with explicit numbering**
(`1.`, `2.`, `3.`, …), not repeated `1.`. With explicit numbers Pandoc emits
`<ol start="N">` on each fragment, so the browser renders the correct sequence
across the `<details>` interruptions.

Audit pattern (top-level `1.` markers per section):
```bash
# rough heuristic; manually verify it's the broken pattern, not separate lists
grep -nE '^1\.' site/class/*.qmd
```
Swept 19 class-pages' Brain Gains sections on 2026-05-29; ~120 items
renumbered. The same bug class also affects Group Meeting / Discussion /
Preparation sections across many class files — those weren't part of that
sweep.

## Run-on equation chains → align on `=`

Inline or single-line display math with 3+ `=` (`$$X = Y = Z = W$$`) reads as a
run-on. Convert to an aligned block:

```
$$
\begin{aligned}
X &= Y \\
  &= Z \\
  &= W
\end{aligned}
$$
```

When auditing, beware false positives: `=` inside subscripts (`\sum_{i=1}`) and
fractions inflate a naive `=` count. Only **top-level** `=` form a real chain.
Parameter lists like `$a=1, b=2, c=3$` are not chains — leave them inline.
(Inventory of remaining inline chains: `handoffs/2026-05-18_latex_pattern_B_deferred.md`.)

## Page navigation (prev/next) requires a sidebar

- Quarto has **no native header/top arrows.** The only built-in sequential
  navigation is `page-navigation: true`, which renders prev/next links at the
  **page bottom** and derives their order from the **sidebar `contents`**.
- Scope a sidebar to a section by listing only those pages in its `contents`;
  pages not listed render with no sidebar.
- To keep prev/next **without showing the list**: leave the sidebar defined
  (it supplies the order) but hide it. Use `style: floating`, not `docked` — a
  docked sidebar reserves a content column (hiding it leaves a left gap), while
  a floating sidebar sits in the left margin so content stays centered like a
  no-sidebar page. Then in `styles.css`:
  ```css
  #quarto-sidebar { display: none !important; }
  .quarto-sidebar-toggle { display: none !important; }
  ```
  This is how class pages get bottom "Class N−1 / Class N+1" buttons with no
  visible class index (see `_quarto.yml` sidebar `Class Sessions`).

## Build / render caveats

- **`site/_site/` is build output** — gitignored. CI re-renders from source and
  deploys to `gh-pages`; never commit or hand-edit `_site/`.
- A single-file `quarto render path/to/page.qmd` does **not** fully re-apply
  project-level `_quarto.yml` layout changes (e.g. sidebar `style`). Run a full
  `quarto render` after editing `_quarto.yml`.
- Always render via the project (`cd site && quarto render`), not standalone —
  the custom MathJax macros (`\ds`, `\diff`) come from `_quarto.yml`'s
  `include-in-header` and won't resolve otherwise.
- `freeze: auto` caches code execution; if a referenced asset changed but the
  render looks stale, clear the relevant `_freeze/` entry.
