---
name: openclaw-gateway-foreground-fix
version: 1.0.0
author: Roven
source: locally-developed
platform: openclaw
description: Recover a stuck OpenClaw gateway by diagnosing process state and restarting it in a reliable foreground mode.
updated: 2026-05-31
---

# OpenClaw Gateway Foreground Recovery

Use this skill when OpenClaw cron commands fail with `gateway timeout`, `gateway closed (1006)`, or when port `18789` is not listening. The core lesson from repeated local incidents: launchd may leave high-CPU OpenClaw processes alive without a working gateway, while a direct foreground Node launch brings the gateway back reliably.

## Trigger Conditions

- `openclaw cron run <job>` returns a gateway timeout.
- `openclaw cron list` cannot reach the gateway.
- `lsof -i :18789` has no listener.
- `ps aux | grep openclaw` shows multiple high-CPU OpenClaw processes.

## Diagnosis

Run these checks before killing anything:

```bash
ps aux | grep openclaw | grep -v grep
lsof -i :18789
tail -20 /tmp/openclaw/openclaw-$(date +%Y-%m-%d).log 2>/dev/null || ls /tmp/openclaw
```

Interpretation:

- Several OpenClaw processes plus no port listener usually means the gateway is wedged.
- A process with PPID 1 but no port listener is not healthy.
- Repeated memory-limit warnings often point to extension duplication or a stuck platform plugin.

## Recovery Flow

### 1. Stop residual OpenClaw processes

```bash
pkill -9 -f openclaw
sleep 3
ps aux | grep openclaw | grep -v grep
```

Continue only when the process list is empty or contains only your grep command.

### 2. Start the gateway directly

Prefer the direct Node launch when launchd is unreliable:

```bash
/opt/homebrew/opt/node/bin/node /opt/homebrew/lib/node_modules/openclaw/dist/index.js gateway --port 18789 &
sleep 10
lsof -i :18789
```

If the package path changes after an upgrade, locate it first:

```bash
which openclaw
npm root -g
```

### 3. Validate cron access

```bash
openclaw cron list
openclaw cron run <safe-test-job-id>
```

Do not run production publishing, account-writing, or bulk jobs as the first validation. Pick a harmless status/report job.

## Notes from Real Use

- `openclaw gateway start/stop` can report success while no port is listening. Trust `lsof` over status text.
- When the gateway has been stuck for hours, a single process kill is usually not enough. Kill all OpenClaw processes and restart cleanly.
- Keep a short log of every gateway incident: date, symptom, process count, port state, and recovery command. That log is more useful than another round of guessing.
