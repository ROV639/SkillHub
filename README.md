# SkillHub

Agent Skill Hub For Rubin.

This repository is the shared source of truth for Rubin's reusable agent skills.
It is intentionally organized as a review-and-publish hub: local machines scan
their skills into manifests first, then reviewed skills are promoted into
`skills/ready/`.

## Structure

```text
skills/
  ready/                 # reviewed skills ready to install or sync
  lab/                   # local or custom skills still being cleaned up
  external_unverified/   # third-party skills kept isolated until reviewed
manifests/               # per-machine scan output
reports/                 # scan and dedupe reports
scripts/                 # local tooling
docs/                    # operating guides and Claude scan instructions
```

## Rule

Do not copy every discovered skill directly into `skills/ready/`.
Scan first, review risk flags, dedupe, then promote.
