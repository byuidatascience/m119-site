# GitHub Repository Transfer Guide

## Transfer m119-site to byuidatascience Organization

**Why**: Future instructors will copy Canvas course 425166. If the site stays under `chaz-clark`, all Canvas links break when they copy the course. Moving to `byuidatascience` creates permanent institutional URLs.

**Target URL**: `https://byuidatascience.github.io/m119-site/`

---

## Prerequisites

1. You must be an **owner** or **admin** of the `byuidatascience` GitHub organization
2. The organization must allow GitHub Pages (public repos)

---

## Transfer Steps

### 1. Transfer Repository Ownership

**In GitHub Web UI**:

1. Go to `https://github.com/chaz-clark/m119-site`
2. Click **Settings** tab
3. Scroll to bottom → **Danger Zone**
4. Click **Transfer ownership**
5. Enter new owner: `byuidatascience`
6. Confirm transfer

**Result**: Repository moves to `https://github.com/byuidatascience/m119-site`

---

### 2. Update Local Git Remote

**After transfer, update your local repo**:

```bash
cd /Users/chazclar/Documents/GitHub/m119-site
git remote set-url origin https://github.com/byuidatascience/m119-site.git
git remote -v  # Verify new URL
```

---

### 3. Verify GitHub Pages Settings

**In new repo settings**:

1. Go to `https://github.com/byuidatascience/m119-site/settings/pages`
2. **Source**: Should be set to `gh-pages` branch
3. If not set:
   - Source: `Deploy from a branch`
   - Branch: `gh-pages` / `/ (root)`
   - Click **Save**

**Expected URL**: `https://byuidatascience.github.io/m119-site/`

---

### 4. Trigger First Deployment

**Option A - Automatic** (already configured):
- Workflow runs on every push to `main`
- Since we updated the workflow file, next push will trigger it

**Option B - Manual**:
```bash
# From Actions tab in GitHub
https://github.com/byuidatascience/m119-site/actions
# Click "Publish Quarto Site" → "Run workflow"
```

---

### 5. Verify Deployment

**Test these URLs after ~2-5 minutes**:

- Homepage: `https://byuidatascience.github.io/m119-site/`
- Schedule: `https://byuidatascience.github.io/m119-site/schedule.html`
- Projects: `https://byuidatascience.github.io/m119-site/projects/`
- Project 1: `https://byuidatascience.github.io/m119-site/projects/unit1.html`

**All should load without 404 errors.**

---

## Files Already Updated

✅ `.github/workflows/publish.yml` - Updated to check for `byuidatascience/m119-site`
✅ `handoffs/2026-08-17_deployment-url-confirmed.md` - Updated with new production URL

---

## What Doesn't Need Updating

**Site content**: No changes needed - all links are relative
**Canvas content**: m119-master will add the new URL to Canvas after verification

---

## Rollback Plan

If something goes wrong:

1. **Transfer back**: Use GitHub UI to transfer back to `chaz-clark`
2. **Revert workflow**: Change `publish.yml` back to `chaz-clark/m119-site`
3. **Update remote**: `git remote set-url origin https://github.com/chaz-clark/m119-site.git`

---

## Post-Transfer Checklist

- [ ] Repository transferred to byuidatascience org
- [ ] Local git remote updated
- [ ] GitHub Pages enabled in new repo
- [ ] Workflow triggered (automatic on push or manual)
- [ ] Deployment verified - all URLs load
- [ ] Handoff sent to m119-master with new URL
- [ ] m119-master confirms Canvas links working

---

## Timeline

**Do this**: Before m119-master adds Canvas links
**Best time**: Now (before semester starts Sept 14, 2026)
**Duration**: ~10 minutes + 2-5 minutes for deployment

---

## Questions?

If you hit issues:
- Check GitHub Actions logs: `https://github.com/byuidatascience/m119-site/actions`
- Verify Pages settings: `https://github.com/byuidatascience/m119-site/settings/pages`
- Ensure you're an org owner/admin
