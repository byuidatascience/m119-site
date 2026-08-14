---
direction: notify
status: delivered
from_repo: m119-master
to_repos: m119-site
date_created: 2026-08-14
last_updated: 2026-08-14
trigger: Fall 2026 semester course migration completed
priority: medium
---

# Handoff: Fall 2026 Course Migration Complete

**To**: m119-site (course website)
**From**: m119-master (Canvas course management)
**Purpose**: Notify of completed Fall 2026 semester migration and potential site integration needs

---

## What Was Done

**Canvas Course Migration**: Spring 2026 (409936) → Fall 2026 (425166)

### Migration Stats
- **26 modules** migrated
- **108 assignments** migrated (all dates updated)
- **77 pages** migrated
- **15 enrolled students** in target course

### Date Updates Applied
- **Semester shift**: +147 days (April 20 → September 14, 2026)
- **Course start**: September 14, 2026 (Monday)
- **Course end**: December 16, 2026 (Wednesday)
- **Thanksgiving conflicts resolved**: Assignments falling on Nov 26 (Thanksgiving) → moved to Nov 24

### Key Assignments Date-Shifted
- Project 1 tasks: Week 2-6 (Sept 24 - Oct 22)
- Project 2 tasks: Week 7-10 (Oct 29 - Nov 19)
- Project 3 tasks: Week 11-13 (Nov 24 - Dec 10) ⚠️ **Thanksgiving week adjusted**
- Weekly reports: All shifted to Fall schedule
- Skills practice quizzes: All end-dates set to Dec 10

---

## Canvas Course Details

**Fall 2026 Course (425166)**:
- Name: Applied Calculus: Data Analysis
- Code: MATH 119
- Status: Unpublished (ready for review)
- Enrollment: 15 students

**What's Ready**:
- ✅ All assignment due dates set for Fall 2026
- ✅ Module structure intact (26 modules)
- ✅ Grading scaffolding in place (AI logs, cohesive narratives, ready-for-review)
- ✅ Course dates configured (Sept 14 - Dec 16)

**What Needs Review**:
- ⚠️ Canvas links in pages/assignments may reference old course
- ⚠️ NewQuiz items (can't be edited via API - require Canvas UI)
- ⚠️ Course still unpublished - review before publishing

---

## Potential Site Integration Tasks

You mentioned wanting to **integrate the projects site into the daily course site**. Here's what that might involve:

### Current Separation
- **m119-site**: Daily course schedule, lessons, activities
- **Projects content**: Currently in separate structure (possibly separate site?)

### Integration Options

**Option 1: Embed projects as sections**
- Add project pages to m119-site navigation
- Keep project milestones aligned with Canvas due dates
- Cross-link between daily lessons and project tasks

**Option 2: Unified schedule view**
- Merge project deadlines into daily schedule
- Show "Week X: Lesson Y + Project Z Task N" structure

**Option 3: Project hub page**
- Create central project landing page in m119-site
- Link to individual project task pages
- Show progress/timeline visualization

### Date Alignment Needed
If integrating, the m119-site schedule should align with:
- **Fall semester dates**: Sept 14 - Dec 16, 2026
- **Thanksgiving break**: Nov 25-27 (no classes)
- **Project deadlines**: See "Key Assignments Date-Shifted" above

---

## Canvas Link Fixes Needed

**Known Issues**:
1. **Old course ID references**: Any Canvas links with `/courses/409936/` should be `/courses/425166/`
2. **Semester-specific references**: "Spring 2026" text should be "Fall 2026"
3. **Date references**: Any hard-coded dates from Spring schedule

**How to Fix**:
```bash
# From m119-master repo:
cd course/
grep -r "409936" . | grep -v ".git"  # Find old course ID references
grep -r "Spring 2026" .              # Find semester references
```

Then update via Canvas UI or `canvas_sync.py --push` after editing local files.

---

## Lessons Learned / Process Improvements

### What Worked
- ✅ **Canvas course copy API**: Used `create_content_migration()` to copy 409936→425166
- ✅ **Automated date shifting**: Custom script applied +147 day shift with Thanksgiving logic
- ✅ **Thanksgiving auto-detection**: Script caught Nov 26 conflicts and moved to Nov 24

### What Could Be Better
- **canvas-toolbox v1.21.0 just shipped** with `--migrate-from` feature that automates steps 1-3
- Next semester migration can use: `canvas_sync.py --migrate-from OLD --to NEW --apply`
- Eliminates manual Canvas API calls and polling

### For Next Time (Winter 2027)
1. Use `canvas_sync.py --migrate-from 425166 --to <WINTER_COURSE_ID> --apply`
2. Apply semester date shift script
3. Review Canvas links
4. Push with `canvas_sync.py --push --allow-enrolled`

---

## Action Items for m119-site

### Immediate (Before Semester Start)
- [ ] Review whether projects site integration is still desired
- [ ] If yes, determine integration approach (Option 1, 2, or 3)
- [ ] Update m119-site schedule dates for Fall 2026
- [ ] Verify any Canvas embed links use course ID 425166

### Optional
- [ ] Add Fall 2026 calendar to site (with Thanksgiving noted)
- [ ] Update project milestone dates on site to match Canvas
- [ ] Test all Canvas → site navigation flows

---

## Files/Tools Created During Migration

**In m119-master:**
- `lib/analyze_course_dates.py` - Analyzes assignment dates vs. semester calendar
- `lib/calculate_fa26_dates.py` - Shows date shift mapping (Spring→Fall)
- `lib/update_to_fa26_dates.py` - Applies semester date shift with Thanksgiving handling
- `lib/clear_canvas_ids.py` - Strips canvas_ids for fresh course push

**Re-usable for future semesters** with date constant updates.

---

## Questions or Issues?

If you need:
- Canvas course access for review
- Specific assignment date details
- Help with site integration planning
- Canvas link audit assistance

Let me know and I can assist or provide data exports.

---

## Success Criteria

**This handoff is "applied" when**:
1. m119-site team has reviewed Fall 2026 dates
2. Decision made on projects site integration (yes/no, which option)
3. Any Canvas link fixes identified and scheduled

**This handoff is "complete" when**:
- m119-site schedule reflects Fall 2026 dates
- Projects integration (if desired) is implemented
- Canvas ↔ site navigation tested and working

---

## Resources

**Canvas Course**: https://byui.instructure.com/courses/425166
**Semester Calendar**: Sept 14 - Dec 16, 2026
**Thanksgiving Break**: Nov 25-27 (Wed-Fri)

**Migration Tools** (in m119-master/lib/):
- `analyze_course_dates.py`
- `update_to_fa26_dates.py`

**canvas-toolbox v1.21.0**: Now includes `--migrate-from` for automated semester migrations

---

**End of Handoff**
