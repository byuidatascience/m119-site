# Answer Box Distribution Audit - Fall 2026

**Date**: 2026-08-17
**Purpose**: Audit dropdown answer boxes (`<details>` tags) across all class sessions to ensure even distribution

---

## Summary Statistics

**Total Classes**: 47 (class-1 through class-46, plus class-43b)
**Total Answer Boxes**: 323
**Average per Class**: 6.9 boxes
**Median**: 7 boxes
**Range**: 1-19 boxes

---

## Distribution by Class Session

### High Usage (10+ boxes)
| Class | Count | Notes |
|-------|-------|-------|
| class-39 | 19 | 🔴 Much higher than average |
| class-25 | 17 | 🔴 Much higher than average |
| class-2 | 15 | 🔴 Much higher than average |
| class-29 | 14 | |
| class-7 | 13 | |
| class-9 | 11 | |
| class-30 | 11 | |
| class-33 | 11 | |
| class-45 | 11 | |
| class-13 | 10 | |
| class-20 | 10 | |
| class-38 | 10 | |

### Low Usage (1-3 boxes)
| Class | Count | Notes |
|-------|-------|-------|
| class-6 | 1 | 🟡 Much lower than average |
| class-46 | 1 | 🟡 Much lower than average |
| class-11 | 2 | 🟡 Lower than average |
| class-26 | 2 | 🟡 Lower than average |
| class-42 | 2 | 🟡 Lower than average |
| class-12 | 3 | |
| class-31 | 3 | |
| class-37 | 3 | |
| class-43b | 3 | |
| class-44 | 3 | |

### Moderate Usage (4-9 boxes)
All other classes fall within this range (34 classes total)

---

## Distribution by Course Phase

### Weeks 1-4 (Classes 1-15): **Foundation Phase**
**Total boxes**: 115
**Average**: 7.7 per class
**Range**: 2-15

Notable:
- class-2: 15 boxes (peak for this phase)
- class-7: 13 boxes
- class-11: 2 boxes (lowest)

### Weeks 5-8 (Classes 16-30): **Project 1-2 Phase**
**Total boxes**: 108
**Average**: 7.2 per class
**Range**: 4-17

Notable:
- class-25: 17 boxes (peak for entire semester)
- class-29: 14 boxes
- class-26: 2 boxes (lowest)

### Weeks 9-13 (Classes 31-46): **Project 3 & Review Phase**
**Total boxes**: 100
**Average**: 6.3 per class
**Range**: 1-19

Notable:
- class-39: 19 boxes (HIGHEST for entire semester)
- class-6, 46: 1 box each (tied for lowest)
- class-42: 2 boxes

---

## Patterns Observed

### Strengths ✅
1. **Majority consistent**: 34 out of 47 classes (72%) have 4-9 boxes
2. **Good average**: 6.9 boxes per class provides regular practice
3. **Distributed across semester**: Answer boxes present in all phases

### Areas for Improvement 🔧

1. **Outlier Classes - Too Many**:
   - class-39 (19 boxes) - Probability/Unit 3 intensive day?
   - class-25 (17 boxes) - Project 2 work day?
   - class-2 (15 boxes) - Second day of class, heavy on practice

   **Recommendation**: Review these classes - may overwhelm students. Consider:
   - Splitting content across 2 days
   - Moving some exercises to homework/prep
   - Reducing redundancy if present

2. **Outlier Classes - Too Few**:
   - class-6 (1 box) - Project work day?
   - class-46 (1 box) - Final review/flex day?
   - class-11, 26, 42 (2 boxes each)

   **Recommendation**: Review these classes - may lack practice. Consider:
   - Adding 3-4 more practice problems with answers
   - Including review exercises from prior topics
   - Adding worked examples with solutions

3. **End-of-Semester Decline**:
   - Average drops from 7.7 (Weeks 1-4) → 6.3 (Weeks 9-13)

   **Recommendation**: Maintain consistent practice opportunities through final weeks

---

## Recommended Actions

### Priority 1: Balance Outliers

**Add answer boxes to** (target: 5-7 boxes each):
- [ ] class-6 (currently 1) → Add 4-6 boxes
- [ ] class-46 (currently 1) → Add 4-6 boxes
- [ ] class-11 (currently 2) → Add 3-5 boxes
- [ ] class-26 (currently 2) → Add 3-5 boxes
- [ ] class-42 (currently 2) → Add 3-5 boxes

**Reduce answer boxes in** (target: 10-12 boxes each):
- [ ] class-39 (currently 19) → Remove or move 7-9 boxes
- [ ] class-25 (currently 17) → Remove or move 5-7 boxes
- [ ] class-2 (currently 15) → Remove or move 3-5 boxes

### Priority 2: Enhance Low Classes

Classes with 3-4 boxes could benefit from 2-3 more:
- class-12, 31, 37, 43b, 44 (3 boxes)
- class-17, 18, 23, 24, 28, 34, 35 (4 boxes)

### Priority 3: Review Special Days

Check if low-box classes are intentionally light:
- **Open lab days**: Week 4 (class-15), Week 9 (class-32)
- **Project work days**: Week 14 (class-46?)
- **Flex days**: class-46 is listed as flex-1 in schedule

If these are active work days, low answer box count is appropriate.

---

## Distribution Target (Recommended)

For optimal student practice:

| Boxes per Class | Target % of Classes | Current % | Status |
|-----------------|---------------------|-----------|--------|
| 5-9 boxes | 80% | 72% (34/47) | 🟡 Close |
| 10-12 boxes | 15% | 17% (8/47) | ✅ Good |
| 13+ boxes | 5% | 11% (5/47) | 🔴 Too many |
| 1-4 boxes | 0% (special days only) | 17% (8/47) | 🔴 Too many |

**Goal**: Move 13+ box classes down to 10-12, and 1-4 box classes up to 5-9.

---

## Implementation Plan

### Step 1: Identify Special Days
Review schedule_config.yml and class file headers to identify:
- Open lab days
- Project work days
- Flex/review days
- Testing days

These days should be exempted from the 5-9 box target.

### Step 2: Content Balancing
For each outlier class:
1. Review learning objectives
2. Identify redundant or overly similar problems
3. Move excess problems to:
   - Homework prep sections
   - Optional practice
   - Adjacent classes with lower counts

### Step 3: Gradual Enhancement
For low-count classes:
1. Review topic coverage
2. Add 2-3 practice problems with answer boxes from:
   - Previous topic review
   - Mixed practice combining recent concepts
   - Common mistake examples

### Step 4: Verification
After adjustments:
- Re-run this audit script
- Target: 80% of classes in 5-9 box range
- No class above 12 boxes (except identified intensive review days)
- No class below 4 boxes (except identified special days)

---

## Audit Script

To re-run this audit:

```bash
grep -c '<details>' site/class/class-*.qmd | \\
  sed 's|.*/||' | sed 's|\.qmd||' | sort -V
```

Or use Python for more detailed analysis:

```python
import glob
import statistics

counts = []
for file in sorted(glob.glob('site/class/class-*.qmd')):
    with open(file) as f:
        count = f.read().count('<details>')
        counts.append((file.split('/')[-1].replace('.qmd', ''), count))

total = sum(c[1] for c in counts)
avg = statistics.mean(c[1] for c in counts)
median = statistics.median(c[1] for c in counts)

print(f"Total: {total}")
print(f"Average: {avg:.1f}")
print(f"Median: {median}")
print("\\nDistribution:")
for name, count in counts:
    print(f"{name}: {count}")
```

---

## Conclusion

The course has a **good foundation** with answer boxes distributed across all classes, averaging 6.9 per session.

**Main improvements needed**:
1. Balance 5 high-outlier classes (13-19 boxes)
2. Enhance 8 low-count classes (1-4 boxes)
3. Maintain consistency through final weeks

**Timeline**: Complete before semester start (Sept 14, 2026)

**Impact**: More even student practice load, consistent active learning opportunities throughout semester
