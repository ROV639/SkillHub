---
name: hermes-upgrade-workflow
version: 1.0.0
author: Roven
source: locally-developed
platform: hermes
description: Upgrade Hermes Agent while preserving local modifications and resolving stash conflicts.
updated: 2026-05-31
---

# Hermes Upgrade Workflow

## Context
Hermes Agent uses `git stash` during `curl | bash` upgrade. Local modifications are automatically stashed before pulling new code. After upgrade, stash must be manually reapplied.

## Standard Upgrade Flow

```bash
# 1. Run upgrade (creates automatic stash of local changes)
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# 2. After upgrade completes, check for stash
cd ~/.hermes/hermes-agent && git stash list

# 3. If stash exists, inspect what it contains
git stash show -p

# 4. Resolve any conflicting files (e.g. package-lock.json)
git checkout --theirs package-lock.json && git add package-lock.json

# 5. Apply remaining stash changes
git stash pop

# 6. Verify local modifications are preserved before committing
git diff --cached <file>  # e.g. gateway/platforms/telegram.py

# 7. Commit
git commit -m "merge: v<version> + local modifications"
```

## Common Issues

### package-lock.json conflict
- **Cause**: npm deps differ between local and upstream
- **Fix**: `git checkout --theirs package-lock.json && git add package-lock.json`
- **Rationale**: package-lock.json is auto-generated; local changes are in Python source files

### Stash not applying cleanly
- Check `git status` — staged = merged successfully, unmerged = need resolution

## What Gets Stashed (Typical Local Modifications)
- Chinese UI translations (telegram.py approval buttons, run.py help text)
- Additional DANGEROUS_PATTERNS in approval.py
- package-lock.json npm dependency updates

These are intentionally preserved by the upgrade script — user customizations.
