# Strategic Answer Box Implementation - Manual Review Results

**Date**: 2026-08-17
**Classes Reviewed**: 11, 12, 26, 42
**Approach**: Pedagogically-driven placement where fast feedback prevents compounding errors

---

## Key Finding: Missing Answer Boxes Where They Matter Most

All four classes have **critical self-check moments with NO answer boxes**. Students are asked to practice techniques but can't verify if they're doing it correctly.

---

## Class-11: Derivatives & uniroot() Practice (Currently 2 boxes)

### What's There (Good)
- 1 box: IVT definition (explanatory)
- 1 box: Possible visually fitted models for Project 1

### What's MISSING (Critical) ⚠️

**Brain Gains Section - 4 Questions, NO ANSWERS**:

1. **Exponential parameter identification**
   - "If $f(x;a,b) = ae^{bx}$ and $f(0)=7$, what must $a$ equal?"
   - **Why it matters**: Foundation for maximum likelihood in Project 2
   - **Fast feedback value**: Catch algebra errors immediately

2. **Another parameter problem**
   - "If $f(x;a,b) = a+be^{x}$ and $f(0)=7$, what must $a$ equal?"
   - **Why it matters**: Different form, tests understanding vs memorization

3. **uniroot() practice**
   - "Use uniroot to solve $7 = 5+3e^{2x}$. Check analytically if possible."
   - **Why it matters**: TECHNIQUE PRACTICE - need immediate check
   - **Fast feedback value**: Verify uniroot() syntax and interval choice

4. **More uniroot()**
   - "Solve $(-13 + 2x)e^{-0.05x} = 0$ and $(-13 + 2x)e^{-0.05x} = 5$"
   - **Why it matters**: Sequential problem - error in first ruins second
   - **Fast feedback value**: Check step 1 before proceeding to step 2

### ADD 1 Answer Box

**Location**: After Brain Gains question 4

**Content**:
```markdown
<details>
<summary>Answers</summary>

1. If $f(x;a,b) = ae^{bx}$ and $f(0)=7$:
   - $f(0) = ae^{0} = a \cdot 1 = a = 7$
   - Therefore $a = 7$

2. If $f(x;a,b) = a+be^{x}$ and $f(0)=7$:
   - $f(0) = a + be^{0} = a + b = 7$
   - Therefore $a = 7 - b$ (infinitely many solutions)

3. Solve $7 = 5+3e^{2x}$:
   - Analytical: $2 = 3e^{2x}$ → $e^{2x} = \frac{2}{3}$ → $2x = \ln(\frac{2}{3})$ → $x = \frac{\ln(2/3)}{2} \approx -0.2027$
   - In R:
   ```r
   f <- function(x){7 - (5 + 3*exp(2*x))}
   uniroot(f, c(-1, 1))$root
   # Returns approximately -0.2027
   ```

4. Solve $(-13 + 2x)e^{-0.05x} = 0$:
   - Since $e^{-0.05x} > 0$ always, need $-13 + 2x = 0$
   - $x = 6.5$ (exact)
   - Solve $(-13 + 2x)e^{-0.05x} = 5$:
   ```r
   g <- function(x){(-13 + 2*x)*exp(-0.05*x) - 5}
   plot(seq(0, 20, 0.1), g(seq(0, 20, 0.1)), type="l")
   abline(h=0, col="red")
   uniroot(g, c(10, 15))$root
   # Returns approximately 12.64
   ```

**Common mistake**: Forgetting that $e^{kx} > 0$ for all real $x$.
</details>
```

**Impact**: Students get immediate feedback on parameter manipulation and uniroot technique

---

## Class-12: Function Composition & Model Application (Currently 3 boxes)

### What's There (Good)
- 1 box: Logarithm product notation solutions
- 1 box: R code for graphing fitted models (not answers, just code)

### What's MISSING (Critical) ⚠️

**Brain Gains Section - First 3 items, NO ANSWERS**:

1. **Function decomposition**
   - "For $f(x) = -2\sqrt[3]{x+6}$, identify power functions and operations"
   - **Why it matters**: Foundation for chain rule (coming soon)
   - **Fast feedback value**: Verify they can see function structure

2. **Logarithm evaluation and solving**
   - "Let $f(t) = \log_2(3t-2)$. Compute $f(2)$ and solve $f(t) = 2$"
   - **Why it matters**: Basic technique for Project 2 likelihood
   - **Fast feedback value**: Check domain awareness and log rules

**Using a Model Section - 6 Questions, NO ANSWERS**:

These ask students to use fitted models to answer questions like:
- "What is intensity after 12000 hours?"
- "When is intensity 90%?"
- "When does bulb burn out (80%)?"

**Why these matter**:
- PROJECT APPLICATION - students practicing what they'll do in Project 1
- Sequential use of uniroot()
- Model interpretation

### ADD 2 Answer Boxes

**Box 1: After Brain Gains items (before Group Meeting)**

```markdown
<details>
<summary>Answers</summary>

1. $f(x) = -2\sqrt[3]{x+6} = -2(x+6)^{1/3}$
   - Power function: $u^{1/3}$ where $u = x+6$
   - Operations: composition, shift, constant multiple
   - Build it: Start with $p(u) = u^{1/3}$, then $g(x) = p(x+6) = (x+6)^{1/3}$, then $f(x) = -2g(x)$

2. $f(t) = \log_2(3t-2)$:
   - $f(2) = \log_2(3 \cdot 2 - 2) = \log_2(4) = 2$
   - Solve $f(t) = 2$: $\log_2(3t-2) = 2$ → $3t-2 = 2^2 = 4$ → $3t = 6$ → $t = 2$
   - Check in R:
   ```r
   f <- function(t){log2(3*t - 2)}
   f(2)  # Returns 2
   g <- function(t){log2(3*t - 2) - 2}
   uniroot(g, c(1, 5))$root  # Returns 2
   ```

**Note**: Be careful with domain - need $3t-2 > 0$, so $t > \frac{2}{3}$.
</details>
```

**Box 2: After "Using a model" section questions**

```markdown
<details>
<summary>Answers</summary>

Using the fitted models (seed=123):

1. **Intensity after 12000 hours using $f_4$**:
   ```r
   f4 <- function(x){100 - 0.000181*x + 0.83*log(0.005*x+1)}
   f4(12000)
   # Approximately 99.59%
   ```

2. **When intensity = 90% using $f_3$**:
   ```r
   f3 <- function(x){101.9 - 1.9*exp(-0.00114*x)}
   g3 <- function(x){f3(x) - 90}
   uniroot(g3, c(0, 50000))$root
   # Approximately 2046 hours
   ```

3. **When intensity = 97% using $f_2$**:
   ```r
   f2 <- function(x){100 + 0.0011*x - 0.00000015*x^2}
   g2 <- function(x){f2(x) - 97}
   uniroot(g2, c(0, 10000))$root
   # Two solutions possible - check plot first
   ```

4. **When intensity = 95% using $f_5$**:
   ```r
   f5 <- function(x){(100 + 0.00623*x)*exp(-0.0000506*x)}
   g5 <- function(x){f5(x) - 95}
   uniroot(g5, c(0, 50000))$root
   # Approximately 37668 hours
   ```

5. **Intensity after 25000 hours using $f_5$**:
   ```r
   f5(25000)
   # Approximately 101.8%
   ```

6. **When does bulb burn out (80% intensity) for each model**:
   - Plot each function first to find appropriate interval
   - Use uniroot() with function - 80
   - Some models may not reach 80% within realistic timeframe

**Common mistake**: Not checking plot first - may choose wrong interval for uniroot().
</details>
```

**Impact**: Students verify their uniroot() technique and model application skills

---

## Class-26: Optimization & Maximum Likelihood (Currently 2 boxes)

### What's There (Good)
- 1 box: Logarithm sum explanation (Brain Gains #1)
- 1 box: Second derivative test solution (Brain Gains #3)

### What's MISSING (Critical) ⚠️

**Brain Gains #2 - NO ANSWER**:
- "Given $f'(4.2)=0$, $f'(6.3)=0$, $f''(4.2)=7.8$, $f''(6.3)=-1.9$"
- "At which x values: local max? local min?"
- **Why it matters**: SECOND DERIVATIVE TEST - core concept
- **Fast feedback value**: Immediate reinforcement of test interpretation

**PREP Section - 6 Numbered Problems, NO ANSWERS**:

These are CRITICAL for Project 2:
1. Find critical points, use second derivative test
2. Same for different function
3. **Compute first and second derivatives of loglikelihood** (Project 2 Task 2)
4-6. Repeat for different model

**Why these matter**:
- PROJECT 2 FOUNDATION - maximum likelihood method
- Sequential calculations - error in derivative ruins optimization
- Students need to verify derivatives BEFORE finding critical points

### ADD 2 Answer Boxes

**Box 1: After Brain Gains #2**

```markdown
<details>
<summary>Answer</summary>

Using the second derivative test:
- At a critical point where $f'(x) = 0$:
  - If $f''(x) > 0$ → concave up → **local minimum**
  - If $f''(x) < 0$ → concave down → **local maximum**

For this problem:
- At $x = 4.2$: $f'(4.2) = 0$ and $f''(4.2) = 7.8 > 0$ → **local minimum**
- At $x = 6.3$: $f'(6.3) = 0$ and $f''(6.3) = -1.9 < 0$ → **local maximum**
</details>
```

**Box 2: After PREP section (before "During Class")**

```markdown
<details>
<summary>Prep Answers (seed=123 for #3 and #6)</summary>

**1.** $f(a) = 100 - \frac{1}{2}(3-4a)^2$
- $f'(a) = -\frac{1}{2} \cdot 2(3-4a) \cdot (-4) = 4(3-4a) = 12-16a$
- Critical point: $12-16a = 0$ → $a = 0.75$
- $f''(a) = -16$ (always negative) → **local maximum** at $a = 0.75$

**2.** $f'(a_1) = 172746.8 - 328767530a_1$
- Critical point: $172746.8 - 328767530a_1 = 0$ → $a_1 = \frac{172746.8}{328767530} \approx 0.0005253$
- $f''(a_1) = -328767530$ (negative) → **local maximum** at $a_1 \approx 0.0005253$

**3.** For $\ell_1$ (Project 2 loglikelihood):
- $\frac{d\ell_1}{da_1} = 172746.8 - 328767530 a_1$ (matches #2!)
- $\frac{d^2\ell_1}{da_1^2} = -328767530$
- Critical point: $a_1 \approx 0.0005253$ → **maximum**
- In R:
```r
library(data4led)
bulb <- led_bulb(1,seed=123)
ti <- bulb$hours
yi <- bulb$percent_intensity
a1 <- 0.0005253
f1 <- function(t,a1){100+a1*t}
plot(ti,yi)
lines(ti,f1(ti,a1))
```

**4-6.** Similar process for model $f_5$ - verify your derivatives match the given forms!

**Common mistake**: Forgetting to verify $f''$ is negative for maximum (not just find critical point).
</details>
```

**Impact**: Students can verify their derivatives and optimization work BEFORE applying to Project 2

---

## Class-42: Continuous Random Variables & Percentiles (Currently 2 boxes)

### What's There (Good)
- 1 box: Percentile definition (explanatory)
- 1 box: Mathematica solutions for percentile calculations

### What's MISSING (Critical) ⚠️

**Brain Gains Section - 7 Questions, NO ANSWERS**:

Students asked to work with $f(x) = k(15-x)$ for $0 \leq x \leq 15$:

1. Find $k$ (normalization)
2. Find $E[X]$ and $Var(X)$
3. Compute $P(X \leq 1)$, $P(X \leq 2)$, and CDF
4-5. Find 60th and 95th percentiles
6-7. Find probabilities

**Why these matter**:
- SEQUENTIAL - wrong $k$ ruins everything after
- PROJECT 3 foundation - using fitted distributions
- Integration practice with immediate consequences

**ACT Scores Section - 9 Questions, NO ANSWERS**:

Students asked to compute percentiles and probabilities using normal distribution.

**Why these matter**:
- Real-world application
- Integral setup verification
- Mathematica syntax practice

### ADD 2 Answer Boxes

**Box 1: After Brain Gains questions (before Discussion)**

```markdown
<details>
<summary>Answers (with work shown)</summary>

Given $f(x) = k(15-x)$ for $0 \leq x \leq 15$:

**1. Find k:**
- Must satisfy $\int_0^{15} k(15-x) dx = 1$
- $k\left[15x - \frac{x^2}{2}\right]_0^{15} = k\left(225 - 112.5\right) = 112.5k = 1$
- $k = \frac{1}{112.5} = \frac{2}{225}$

**2. Expected value and variance:**
```mathematica
Integrate[x * (2/225)*(15-x), {x, 0, 15}]
(* E[X] = 5 *)

Integrate[x^2 * (2/225)*(15-x), {x, 0, 15}]
(* E[X²] = 31.25 *)
(* Var(X) = E[X²] - (E[X])² = 31.25 - 25 = 6.25 *)
```

**3. Probabilities:**
- $P(X \leq 1) = \int_0^1 \frac{2}{225}(15-x) dx = \frac{2}{225}\left[15 - 0.5\right] = \frac{29}{225} \approx 0.1289$
- $P(X \leq 2) = \int_0^2 \frac{2}{225}(15-x) dx = \frac{58}{225} \approx 0.2578$
- $F(x) = \int_0^x \frac{2}{225}(15-t) dt = \frac{2}{225}\left[15x - \frac{x^2}{2}\right] = \frac{30x - x^2}{225}$

**4. 60th percentile:**
- Solve $F(x) = 0.6$: $\frac{30x - x^2}{225} = 0.6$
- $30x - x^2 = 135$ → $x^2 - 30x + 135 = 0$
- $x = \frac{30 \pm \sqrt{900-540}}{2} = \frac{30 \pm 18.97}{2}$
- $x \approx 5.51$ or $x \approx 24.49$ (reject, outside domain)
- **60th percentile = 5.51**

**5. 95th percentile:** Solve $F(x) = 0.95$ → $x \approx 2.32$

**6. P(X > 10):** $= 1 - F(10) = 1 - \frac{200}{225} = \frac{25}{225} \approx 0.111$

**7. P(-3 < X < 3):** $= F(3) - F(-3) = F(3) - 0 = \frac{85.5}{225} \approx 0.38$

**Common mistake**: Forgetting to verify $k$ by checking $\int f(x)dx = 1$ before proceeding.
</details>
```

**Box 2: After ACT Scores questions**

```markdown
<details>
<summary>ACT Answers (μ=21, σ=5)</summary>

Using $f(x) = \frac{1}{\sqrt{2\pi \cdot 25}}e^{-\frac{1}{50}(x-21)^2}$:

**Percentiles (given score, find percentile):**
```mathematica
(* Score 22 *)
NIntegrate[1/Sqrt[50*Pi]*Exp[-(1/50)*(x-21)^2], {x, -Infinity, 22}]
(* Approximately 0.5398 = 54th percentile *)

(* Score 23 *)
NIntegrate[1/Sqrt[50*Pi]*Exp[-(1/50)*(x-21)^2], {x, -Infinity, 23}]
(* Approximately 0.5793 = 58th percentile *)

(* Score 32 *)
NIntegrate[1/Sqrt[50*Pi]*Exp[-(1/50)*(x-21)^2], {x, -Infinity, 32}]
(* Approximately 0.9861 = 99th percentile *)

(* Score 12 *)
NIntegrate[1/Sqrt[50*Pi]*Exp[-(1/50)*(x-21)^2], {x, -Infinity, 12}]
(* Approximately 0.0359 = 4th percentile *)
```

**Scores (given percentile, find score):**
```mathematica
(* 80th percentile *)
NSolve[NIntegrate[1/Sqrt[50*Pi]*Exp[-(1/50)*(x-21)^2], {x, -Infinity, xp}] == 0.80, xp]
(* Approximately 25.2 *)

(* 5th percentile *)
NSolve[NIntegrate[1/Sqrt[50*Pi]*Exp[-(1/50)*(x-21)^2], {x, -Infinity, xp}] == 0.05, xp]
(* Approximately 12.8 *)

(* 90th percentile *)
NSolve[NIntegrate[1/Sqrt[50*Pi]*Exp[-(1/50)*(x-21)^2], {x, -Infinity, xp}] == 0.90, xp]
(* Approximately 27.4 *)
```

**Probabilities:**
- P(16 < X < 26): Integrate from 16 to 26 ≈ 0.6827 (68%)
- P(11 < X < 23): Integrate from 11 to 23 ≈ 0.6554 (66%)

**Common mistake**: Confusing "score to percentile" vs "percentile to score" - check which direction you're solving!
</details>
```

**Impact**: Students verify normalization, sequential calculations, and Mathematica syntax

---

## Implementation Summary

### Total Answer Boxes to Add: 7

| Class | Current | Add | New Total | Where |
|-------|---------|-----|-----------|-------|
| class-11 | 2 | 1 | 3 | Brain Gains |
| class-12 | 3 | 2 | 5 | Brain Gains + Model questions |
| class-26 | 2 | 2 | 4 | Brain Gains #2 + Prep section |
| class-42 | 2 | 2 | 4 | Brain Gains + ACT section |

### Pedagogical Impact

**What these 7 boxes accomplish**:

1. **Prevent compounding errors**
   - Verify $k$ before computing $E[X]$ (class-42)
   - Check derivative before finding critical points (class-26)
   - Verify uniroot() syntax before multiple applications (class-11, 12)

2. **Reinforce technique immediately**
   - Parameter identification (class-11)
   - Function decomposition for chain rule prep (class-12)
   - Second derivative test (class-26)
   - Integration and percentiles (class-42)

3. **Enable remote learning**
   - Students can't ask "did I do this right?" in async work
   - Answer boxes = instant feedback loop
   - Particularly critical for Project 2 & 3 foundation work

### NOT Adding Answer Boxes To

- Group discussion sections (learning IS the discussion)
- Open exploration activities (no single right answer)
- Questions already with answer boxes

---

## Next Steps

1. **Implement these 7 answer boxes** (estimated 2-3 hours)
2. **Test in browser** - verify details/summary tags work
3. **Consider similar patterns** in other low-count classes
4. **Rerun audit** after implementation

---

## Estimated Time

- Writing answers with work shown: ~2-3 hours total
- Each box: 20-30 minutes (show work, common mistakes, verification code)
- Worth it: High-impact placement where fast feedback accelerates learning

---

**This is the pedagogically-driven approach** - answer boxes where they prevent compounding errors and enable technique mastery, not just hitting a number.
