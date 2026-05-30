---
name: rov639-hermes-vs-openclaw
version: 1.0.0
author: Roven
source: locally-developed
platform: openclaw
description: Clarify ownership boundaries, config paths, and routing rules between Hermes and OpenClaw in the ROV639 system.
updated: 2026-05-31
---

# ROV639 Hermes vs OpenClaw System Map

Use this skill when a task involves both Hermes and OpenClaw and the operator needs to know which system owns the schedule, the agent identity, the gateway, or the output path. This prevents the most common failure: fixing the wrong config file because both systems expose similar cron and agent concepts.

## Responsibility Split

| Area | Hermes | OpenClaw |
| --- | --- | --- |
| Primary role | Nomos runtime, message gateway, scheduling shell | Specialist agent factory and report system |
| Typical jobs | Telegram/Discord messages, Nomos cron, memory compression | Jane, Eve, Rov, Hunter, DaVinci, Mary, Themis style reports |
| Main operator | Nomos assistant | Agent matrix |
| Skill system | Uses `~/.hermes/skills/` | Historically prompt/agent driven; SkillHub adds registry structure |

## Config Paths

| Item | Hermes | OpenClaw |
| --- | --- | --- |
| Main config | `~/.hermes/config.yaml` | `~/.openclaw/openclaw.json` |
| Cron jobs | `~/.hermes/cron/jobs.json` | `~/.openclaw/cron/jobs.json` |
| Agent model config | Hermes profile/config files | `~/.openclaw/agents/<agent>/agent/models.json` |
| Session data | `~/.hermes/sessions/` | `~/.openclaw/agents/<agent>/sessions/` |

Never copy session or auth files into a public repo.

## Command Comparison

| Operation | Hermes | OpenClaw |
| --- | --- | --- |
| List scheduled jobs | `cronjob list` | `openclaw cron list` |
| Run one job | `cronjob run --job-id <id>` | `openclaw cron run <id>` |
| Check gateway port | `lsof -i :18789` when using shared gateway | `lsof -i :18789` |
| Restart gateway | restart Hermes/OpenClaw process depending on owner | direct OpenClaw gateway restart |

## Model Clarification

Do not assume that "OpenClaw uses Codex" means Codex is the main model. In this local system, Codex may be available through ACP delegation, while OpenClaw agents can still use a separate primary model. Check the per-agent model file before changing behavior:

```bash
cat ~/.openclaw/agents/<agent>/agent/models.json
```

## Routing Rule of Thumb

- If the problem is about Nomos messages, Telegram buttons, memory compression, or Nomos daily reports, start in Hermes.
- If the problem is about specialist reports, OpenClaw cron runs, agent factories, or the OpenClaw gateway, start in OpenClaw.
- If both are involved, write down the owner of the job before editing any config.
