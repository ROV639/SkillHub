---
name: nomos-ops
version: 1.0.0
author: Roven
source: locally-developed
platform: hermes
description: Operate the Nomos, Hermes, and OpenClaw stack with clear ownership, safe config handling, and repeatable checks.
updated: 2026-05-31
---

# Nomos Operations Manual

Use this skill before changing Nomos, Hermes, OpenClaw, report routing, cron jobs, or bridge behavior in the ROV639 system. It is an operations map: identify the owner, inspect the right config, avoid deleting state, then act.

## System Map

```text
User -> Telegram -> Hermes / Nomos
                         |
                         v
                    OpenClaw agent system
                         |
        Jane / Eve / Rov / Hunter / DaVinci / Mary / Themis
                         |
                         v
                    NAS / Feishu Bot / reports
```

## Critical Paths

| Component | Path | Notes |
| --- | --- | --- |
| Hermes config | `~/.hermes/config.yaml` | System-level Hermes config |
| Hermes skills | `~/.hermes/skills/` | Skill runtime path |
| Hermes cron | `~/.hermes/cron/jobs.json` | Nomos daily schedules |
| OpenClaw cron | `~/.openclaw/cron/jobs.json` | Specialist agent schedules |
| OpenClaw agents | `~/.openclaw/agents/<agent>/` | Agent config and sessions |

Do not publish or copy auth files, session dumps, API keys, cookies, or private report payloads.

## Before Any Operation

1. Identify whether the task belongs to Hermes, Nomos, or OpenClaw.
2. Inspect only the relevant config.
3. Make a small backup before editing config files.
4. Prefer status/list commands before run commands.
5. For cron changes, test one harmless job before enabling a daily schedule.

## Common Commands

```bash
# Hermes config inspection
grep -n "cron\|compression\|telegram" ~/.hermes/config.yaml

# OpenClaw cron inspection
openclaw cron list

# Gateway port
lsof -i :18789

# Process check
ps aux | grep -E "hermes|openclaw" | grep -v grep
```

## Cleanup Rules

Safe to inspect: config files, skill files, public docs, non-sensitive logs.

Do not remove by default: databases, sessions, auth files, memories, cron jobs, `.env`, and active workspaces. If cleanup is needed, move to a timestamped backup first.

## Handoff Format

When finishing an ops task, report:

- Owner: Hermes / Nomos / OpenClaw.
- Files inspected.
- Commands run.
- Changes made.
- Remaining risk.
- Next verification step.
