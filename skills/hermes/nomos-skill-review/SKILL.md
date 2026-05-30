---
name: nomos-skill-review
version: 1.0.0
author: Roven
source: locally-developed
platform: hermes
description: Run a daily review of local and curated skills for freshness, safety, metadata quality, and promotion readiness.
updated: 2026-05-31
---

# Nomos Skill Review

Use this skill for a daily SkillHub/Nomos skill health check. The goal is to catch stale external sources, weak descriptions, unsafe automation, and locally developed skills that should be promoted, retired, or rewritten.

## Schedule

Run after the evening review, ideally after the daily report cycle has finished.

## Scope

### External skills

Check skills with source/provenance metadata:

- Has the upstream source changed?
- Did license information change?
- Did new risky behavior appear?
- Should SkillHub update the curated copy?

### Locally developed skills

Review the most-used local skills first. Do not rewrite every skill every day. Pick a small rolling window, such as the top nine recently used skills.

## Review Steps

1. List skills and source metadata.
2. Check whether descriptions still match behavior.
3. Scan for secrets, account writes, publishing actions, or hidden external calls.
4. Mark each skill: keep, update, test, archive, or block.
5. Write a short report with only actionable changes.

## Output

```text
Skill Review
Date:
Checked:
Changed upstream:
Needs metadata fix:
Needs test:
Blocked/risky:
Recommended commits:
```
