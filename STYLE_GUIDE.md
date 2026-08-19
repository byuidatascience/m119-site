# Math 119 Site Style Guide

This document describes the content and formatting conventions used consistently across the m119-site. Follow these patterns when creating or editing content.

**Last updated**: 2026-08-19
**Purpose**: Ensure consistency across 47 class sessions, 3 projects, and enhancement pages

---

## File Structure & Naming

### Directory Organization
```
site/
├── index.qmd              # Homepage
├── schedule.qmd           # Semester calendar
├── resources.qmd          # Quick Reference (R, Mathematica, Math)
├── common-errors.qmd      # FAQ for debugging
├── topics.qmd             # Topic index
├── class/
│   └── class-{1-46}.qmd  # Daily class sessions (hyphenated, lowercase)
├── projects/
│   ├── index.qmd          # Projects landing page
│   ├── unit1.qmd          # Project 1 instructions
│   ├── unit2.qmd          # Project 2 instructions
│   └── unit3.qmd          # Project 3 instructions
└── definitions/
    └── {topic}.qmd        # Definition pages (lowercase, no spaces)
```

### File Naming Conventions
- **Class sessions**: `class-N.qmd` (lowercase, hyphenated, 1-indexed)
- **Projects**: `unitN.qmd` (lowercase, no hyphen)
- **Definitions**: `{concept}.qmd` (lowercase, no spaces: `conditionalprobability.qmd`)
- **Enhancement pages**: `{purpose}.qmd` (lowercase, hyphenated if multi-word)

---

## Content Structure

### Class Session Pages

**Standard hierarchy**:
```markdown
---
title: "Class N"
---

# Between Class Sessions - Prep for Day N <a id="tasklist"></a>

<!-- Standard prep instructions paragraph -->

## Preparation
### (1) Topic Name
### (2) Topic Name

## Regular Reminders
### Skill Practice (KA Homework)
### Applied Practice (Project Work)

# During Class
## Brain Gains
## Group Meeting
### Activity - Activity Name
## Discussion
```

**Rules**:
- Use `# Between Class Sessions - Prep for Day N` (not `# Prep` or other variants)
- Use `# During Class` (NOT `# During Class - Day N`)
- Number prep tasks with `(1)`, `(2)`, etc.
- Activity headings: `### Activity - {Name}` (title case for activity name)

### Project Pages

**Standard structure**:
```markdown
---
title: "Project N Instructions"
author: ""
date: "Updated {Month Day}"
format:
  html:
    code-fold: true
---

# Project Outline
Background and context...

## Task 1: {Task Name}
- Create a Quarto document. In the YAML header, include `embed-resources: true`...
- Organize your work into a **cohesive analysis** and submit it to Canvas.

## Project N: Bringing it All Together
- Create a new Quarto document.
- Reflect on your work for this project...
```

**Rules**:
- Always say "Quarto document" (NOT "Quarto file")
- End each task with "Organize your work into a **cohesive analysis**"
- Final section titled "Project N: Bringing it All Together"

### Enhancement Pages (resources, common-errors, topics)

**Standard footer**:
```markdown
---

## Related Resources

- [Quick Reference](resources.html) - R, Mathematica, and math formula syntax
- [Common Errors FAQ](common-errors.html) - Debugging help
- [Topic Index](topics.html) - Find which classes cover topics
- [Class Sessions](class/class-1.html) - Browse all daily content

---

**Last updated**: {Date}
**{Context-specific note}**
```

**Rules**:
- Always cross-reference the other two enhancement pages
- Include last-updated timestamp
- End with contextual help note

---

## Formatting Conventions

### Headings

**Hierarchy rules**:
- `#` (H1): Major page sections only (`# During Class`, `# Between Class Sessions`)
- `##` (H2): Main content divisions (`## Preparation`, `## Brain Gains`)
- `###` (H3): Subsections and numbered items (`### (1) Topic`, `### Activity - Name`)
- `####` (H4): Rare; only for deep nesting

**Capitalization**:
- H1/H2: Title case for proper nouns only (`# During Class`, `## Brain Gains`)
- H3 activities: `### Activity - {Title Case Name}`
- H3 prep items: `### (N) {Sentence case description}`

### Callout Boxes

**Standard usage**:
```markdown
::: {.callout-tip}
## Heading (optional)
Content for students to notice or remember.
:::

::: {.callout-warning}
## Common Error
Error explanation and fix.
:::

::: {.callout-note}
## Additional Context
Supplementary information.
:::
```

**When to use**:
- `.callout-tip` - Helpful hints, checklists, bookmarkable content
- `.callout-warning` - Errors, gotchas, things to avoid
- `.callout-note` - Additional context, "Stuck?" sections

**Examples**:
- Week 1 checklist on homepage: `.callout-tip`
- Common R errors in resources.qmd: `.callout-warning`
- "Stuck on an error?" in resources.qmd: `.callout-note`

### Code Blocks

**Language tags (required)**:
```markdown
```r
# R code
```

```mathematica
(* Mathematica code *)
```

```markdown
# Markdown examples
```

```yaml
# YAML examples
```

```bash
# Shell commands
```
```

**Rules**:
- Always specify language for syntax highlighting
- Use lowercase language names (`r` not `R`)
- Include comments explaining non-obvious code

### Links

**External links** (open in new tab):
```markdown
[Link text](https://example.com){target="_blank"}
```

**Internal links** (same tab):
```markdown
[Link text](page.html)
[Link text](relative/path.qmd)
```

**Rules**:
- External links: ALWAYS add `{target="_blank"}`
- Internal links: Use `.html` for rendered links, `.qmd` for source references
- Link text: Descriptive ("Install Positron" not "click here")

### Math Notation

**Inline math**: `$x^2 + 5$`
**Display math**:
```markdown
$$
\frac{d}{dx}[f(x)] = f'(x)
$$
```

**Custom macros** (defined in `_quarto.yml`):
- `\ds` → `\displaystyle`
- `\diff{y}{x}` → `\frac{dy}{dx}`
- `\pd{f}{x}{2}` → `\frac{\partial^2 f}{\partial x^2}`

**Rules**:
- Use `\text{}` for words in equations: `$f(x) \text{ where } x > 0$`
- Spell out "where" and "for" outside math mode when possible
- Consistent notation: $f'(x)$ for derivatives, $\int$ for integrals

### Images

**Standard format**:
```markdown
![Descriptive alt text](path/to/image.png){width=300px}
```

**Rules**:
- ALWAYS include alt text (accessibility requirement)
- Use `{width=...}` or `{height=...}` for sizing
- Relative paths from current file location
- Alt text: describe content ("Graph of exponential function" not "Image 1")

### Lists

**Ordered lists**:
```markdown
1. First item
2. Second item
    a. Sub-item (letter)
    b. Sub-item
```

**Unordered lists**:
```markdown
- First item
- Second item
  - Sub-item (indent 2 spaces)
  - Sub-item
```

**Rules**:
- Use `1.` `2.` for numbered (Markdown auto-numbers)
- Use `-` for bullets (NOT `*`)
- Indent sub-items with 4 spaces (or 2 for compatibility)

---

## Layout Components

### Grid Layouts

**Two-column responsive grid**:
```markdown
::: {.grid}

::: {.g-col-12 .g-col-md-6}
### Column 1 Title
Content...
:::

::: {.g-col-12 .g-col-md-6}
### Column 2 Title
Content...
:::

:::
```

**Usage**: Projects landing page, homepage resources section

### Tabsets

**Multiple tabs**:
```markdown
::: {.panel-tabset}

## Tab 1 Title
Content for tab 1...

## Tab 2 Title
Content for tab 2...

:::
```

**Usage**: resources.qmd (R Syntax | Mathematica | Math Formulas)

### Details/Summary (Progressive Disclosure)

**Expandable sections**:
```markdown
<details>
<summary>Answer</summary>

Hidden content revealed on click.

</details>
```

**Usage**: Answer boxes in class sessions, solutions to exercises

---

## Terminology Standards

### Consistent Terms

| Use This | NOT This |
|----------|----------|
| Quarto document | Quarto file |
| Class session | Class, Day (context-dependent) |
| Positron | RStudio |
| specifications grading | spec grading, specs grading |
| cohesive analysis | write-up, report |
| Between Class Sessions | Prep, Homework |
| During Class | In Class |

### Mathematical Terms

**Function notation**:
- $f(x)$ - function f of x
- $f'(x)$ - derivative of f
- $\frac{df}{dx}$ - derivative using Leibniz notation

**Probability notation**:
- $P(A)$ - probability of event A
- $E[X]$ - expected value of X
- $\text{Var}(X)$ - variance of X

**Consistency**: Use the same notation throughout all materials

---

## Navigation & Organization

### Navbar Structure (from `_quarto.yml`)

```yaml
navbar:
  right:
    - text: "Home"
    - text: "Projects"
    - text: "Help"
      menu:
        - text: "Quick Reference"
        - text: "Common Errors FAQ"
        - text: "Topic Index"
        - text: "---"
        - text: "Install Positron"
        - text: "R Commands"
        - text: "R Cheat Sheets"
        - text: "Quarto Hints"
    - text: "Definitions"
      menu:
        - text: "**Category Name**"
        - text: "Definition Name"
        - text: "---"
    - text: "Schedule"
```

**Rules**:
- Top-level: "Home", "Projects", "Help", "Definitions", "Schedule"
- Help menu: grouped (references, then tools)
- Definitions menu: categorized with bold headers and separators
- Use `---` for visual separators

### Sidebar (Class Sessions)

```yaml
sidebar:
  - title: "Class Sessions"
    style: floating
    collapse-level: 1
    contents:
      - class/class-1.qmd
      - class/class-2.qmd
      # ... all 47 classes in order
```

**Rules**:
- All class files in numerical order (1-46)
- Don't skip numbers
- Floating style for better mobile UX

---

## Content Guidelines

### Cohesive Analysis

**Requirements** (used in all projects):
1. Introduce all calculations BEFORE showing code
2. Introduce all plots BEFORE showing them
3. Explain results AFTER calculations/plots
4. Use complete sentences and paragraphs
5. Make connections and transitions
6. Assume reader has no access to instructions

**Example**:
```markdown
To determine when the LED bulb reaches 80% intensity, we solve the
equation $f(t) = 80$ using the fitted model from Task 3.

```{r}
# R code here
```

The bulb reaches 80% intensity after approximately 15,200 hours, or
about 1.7 years of continuous operation.
```

### Answer Boxes

**When to use**: Strategic placement where feedback accelerates learning
- After "CHECK YOUR WORK" prompts
- For multi-step calculations students should verify
- NOT for every exercise (avoid box fatigue)

**Format**:
```markdown
<details>
<summary>Answer</summary>

**Solution**: $f(3) = 14$

**Explanation**: We substitute $x=3$ into the function...

</details>
```

### External Resources

**Citation format**:
```markdown
- [Resource Title](url){target="_blank"} (~duration or description)
```

**Examples**:
- [Chain Rule Video](https://youtube.com/...){target="_blank"} (~9 min)
- [Desmos file for function 3](https://desmos.com/...){target="_blank"}

---

## Accessibility

### Requirements

1. **Alt text**: Every image must have descriptive alt text
2. **Link text**: Descriptive, not "click here"
3. **Headings**: Proper hierarchy (don't skip levels)
4. **Color**: Don't rely solely on color to convey meaning
5. **Math**: Use MathJax (not images) for equations

### SEO

**Site-level** (`_quarto.yml`):
```yaml
website:
  title: "Math 119 — Applied Calculus for Data Analysis"
  description: "Applied Calculus for Data Analysis using R and Mathematica..."
```

**Page-level** (optional):
```yaml
---
title: "Page Title"
description: "Brief description for search results"
---
```

---

## Quality Checklist

Before publishing new content:

- [ ] File named correctly (lowercase, hyphenated)
- [ ] Headings follow standard hierarchy
- [ ] All external links have `{target="_blank"}`
- [ ] All images have alt text
- [ ] "Quarto document" not "Quarto file"
- [ ] Code blocks have language tags
- [ ] Math uses `$ $` or `$$ $$` (not images)
- [ ] Callout boxes used appropriately
- [ ] Cross-references to other pages work
- [ ] Content is proofread
- [ ] Local preview renders correctly

---

## Common Mistakes to Avoid

1. ❌ `# During Class - Day 10` → ✅ `# During Class`
2. ❌ `Create a Quarto file` → ✅ `Create a Quarto document`
3. ❌ `[click here](url)` → ✅ `[Install Positron](url)`
4. ❌ External link without `{target="_blank"}`
5. ❌ Image without alt text: `![](path.png)`
6. ❌ Inconsistent heading levels (skipping from H2 to H4)
7. ❌ Using RStudio instead of Positron in new content

---

## Version History

- **2026-08-19**: Initial style guide created based on site audit
- Patterns extracted from 47 class sessions, 3 projects, enhancement pages
- Documents conventions established during Fall 2026 migration

---

**Questions?** Update this guide as new patterns emerge. Keep it as the single source of truth for site conventions.
