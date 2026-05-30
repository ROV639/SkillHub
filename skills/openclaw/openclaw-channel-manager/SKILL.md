---
name: openclaw-channel-manager
version: 1.0.0
author: Roven
source: locally-developed
platform: openclaw
description: Manage OpenClaw delivery channels, report outputs, and publish gates without leaking credentials or mixing account contexts.
updated: 2026-05-31
---

# OpenClaw Channel Manager

Use this skill when OpenClaw outputs need to move from agent reports into delivery channels such as Feishu, Telegram, local folders, dashboards, or publishing queues. This skill is deliberately conservative: channel work is where accidental account writes and leaked tokens happen.

## Channel Inventory

Start by naming the channel and the allowed action.

| Channel Type | Allowed First Action | Risk |
| --- | --- | --- |
| Local report folder | write draft or copy artifact | Low |
| Feishu / Lark bot | send approved summary | Medium |
| Telegram bot | send approved summary or buttons | Medium |
| Social platform | prepare package only | High |
| Email / DM | draft only unless confirmed | High |

## Standard Flow

1. Identify the source artifact.
2. Decide whether the channel receives a draft, summary, link, or final post.
3. Check whether the channel writes to a real account.
4. Prepare the channel package locally.
5. Ask for explicit approval before external sending.
6. Record what was sent and where.

## Safe Package Format

```text
Channel Package
Source:
Destination:
Action: draft / send / schedule / archive
Message:
Attachments:
Links:
Approval required:
Audit note:
```

## Path and Config Checks

Inspect only non-secret routing files first:

```bash
find ~/.openclaw -maxdepth 4 -type f \( -name '*channel*' -o -name '*route*' -o -name '*cron*' \) 2>/dev/null
```

Do not print full environment variables, bot tokens, cookies, auth JSON, or session files.

## Publish Gate

External sends require confirmation when:

- the target is a public or semi-public platform;
- a real account is used;
- the message includes claims, market commentary, or personal data;
- the run is batch or scheduled;
- the channel could notify other people.

## Troubleshooting

If a channel delivery fails:

1. Verify the source artifact exists.
2. Verify the channel package is well formed.
3. Check network and gateway state.
4. Check sanitized logs.
5. Retry once manually.
6. If it still fails, mark the channel blocked and preserve the draft.

Do not "fix" a channel problem by pasting tokens into a script or public config.
