---
name: openclaw-agent-routing
version: 1.0.0
author: Roven
source: locally-developed
platform: openclaw
description: Route OpenClaw tasks to the right specialist agent, model config, and cron lane without mixing responsibilities.
updated: 2026-05-31
---

# OpenClaw Agent Routing

Use this skill when deciding which OpenClaw agent should own a task, which cron lane should run it, or whether the work should be delegated to Codex, Claude, Gemini, OpenCode, or another ACP backend. The important habit: route by ownership and artifact, not by whichever agent is currently convenient.

## Routing Questions

Before dispatching, answer:

1. What artifact should exist after the run?
2. Which specialist agent already owns that artifact type?
3. Does the task need fresh data, writing, code changes, or review?
4. Is this a scheduled job, one-off run, or subagent delegation?
5. What must not be touched?

## Common Agent Ownership

Use your local agent names if they differ, but keep the ownership principle.

| Work Type | Likely Owner | Notes |
| --- | --- | --- |
| Market intelligence or macro scan | Jane / Themis | Needs source freshness and timestamped data. |
| Content topic selection and framing | Eve / Rov | Needs editorial judgment and platform fit. |
| Signal extraction or trading-style watchlist | Hunter | Needs strict invalidation rules and risk notes. |
| Systems and reliability reports | Mary | Needs logs, config, and reproducible checks. |
| Asset or media production packets | DaVinci / Asset | Needs output paths and QC criteria. |
| Code implementation | Codex lane or coding agent | OpenClaw owns routing; code agent owns bounded diff only. |

## Model Routing

Check the agent model config before changing behavior:

```bash
cat ~/.openclaw/agents/<agent>/agent/models.json
```

Do not assume the global default is the active model for every agent. If a task fails because the model is weak or unavailable, change one agent config at a time and record the change.

## ACP Delegation Rule

Use Codex or another ACP backend only when:

- the task is bounded;
- acceptance criteria are explicit;
- a diff or artifact can be reviewed;
- OpenClaw/Hermes remains responsible for final verification.

Never let a delegated coding agent mutate cron state, auth files, or publishing channels directly.

## Dispatch Template

```text
Route:
Agent:
Reason:
Input files:
Expected artifact:
Forbidden actions:
Model/provider:
Verification:
Rollback:
```

## Routing Smells

- The same task mentions three agents but no owner.
- The expected artifact is not named.
- The task asks for "research and publish" in one run.
- A coding agent is asked to edit scheduling or auth config.
- No one owns final verification.
