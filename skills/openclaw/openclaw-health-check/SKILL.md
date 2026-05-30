---
name: openclaw-health-check
version: 1.0.0
author: Roven
source: locally-developed
platform: openclaw
description: Run a practical OpenClaw health check across gateway, cron jobs, agents, models, logs, and workspace outputs.
updated: 2026-05-31
---

# OpenClaw Health Check

Use this skill when OpenClaw feels "alive but not working": cron jobs hang, specialist agents stop producing reports, the gateway port is silent, or the UI says a job ran but no usable output appears. This is a field checklist, not a theoretical status page.

## What to Check First

Start with the gateway and cron layer before looking at individual agents.

```bash
lsof -i :18789
openclaw cron list
ps aux | grep openclaw | grep -v grep
```

Interpretation:

- Port `18789` listening: gateway is at least accepting traffic.
- Port missing but OpenClaw processes exist: likely a wedged gateway.
- Multiple high-CPU OpenClaw processes: clear process pileup before testing jobs.
- Cron list fails: do not debug individual agents yet.

## Gateway Recovery Probe

If the port is not listening:

```bash
pkill -9 -f openclaw
sleep 3
/opt/homebrew/opt/node/bin/node /opt/homebrew/lib/node_modules/openclaw/dist/index.js gateway --port 18789 &
sleep 10
lsof -i :18789
```

Trust the port check more than a friendly "started" message. In real use, launchd can leave a process around without a working listener.

## Agent Config Check

For a failing agent:

```bash
ls ~/.openclaw/agents/<agent>/agent
cat ~/.openclaw/agents/<agent>/agent/models.json
```

Do not copy `auth-state.json`, `auth-profiles.json`, session files, or private output into public logs. Only inspect whether files exist and whether the selected model/provider looks plausible.

## Cron Job Check

```bash
openclaw cron list | sed -n '1,80p'
openclaw cron run <safe-job-id>
```

Pick a harmless report or dry-run job. Do not use a publish, account-writing, or batch job as the first health test.

## Output Check

After a cron run, confirm a real artifact changed:

```bash
find ~/.openclaw -maxdepth 4 -type f -mtime -1 | sort | tail -40
```

If the job "succeeds" but no report changes, treat it as a workflow failure, not success.

## Health Report Format

```text
OpenClaw Health Check
Time:
Gateway port:
Process state:
Cron list:
Agent checked:
Model config:
Recent outputs:
Risk:
Next action:
```

## Stop Conditions

Stop and ask for human approval before:

- deleting sessions or auth files;
- editing model provider config;
- running publish jobs;
- rotating keys;
- changing every agent at once.
