---
name: hermes-tweet
version: 1.0.0
author: Xquik
source: Xquik-dev/hermes-tweet
platform: hermes
description: Use the native Hermes Tweet plugin for X/Twitter reads, social listening, launch monitoring, and approval-gated account actions through Xquik.
updated: 2026-06-29
---

# Hermes Tweet

Use this skill when a Hermes Agent workflow needs X/Twitter context or controlled X account actions through the native Hermes Tweet plugin.

## Install

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

If Hermes already installed it without enabling it:

```bash
hermes plugins enable hermes-tweet
```

Set `XQUIK_API_KEY` in the Hermes runtime environment or `~/.hermes/.env`. Do not paste API keys into chat, prompts, logs, issue bodies, or tool inputs.

Keep actions disabled unless the workflow has explicit approval:

```bash
export HERMES_TWEET_ENABLE_ACTIONS=false
```

## Tool Flow

1. Use `tweet_explore` to find the catalog endpoint.
2. Use `tweet_read` for read-only endpoints after `XQUIK_API_KEY` is configured.
3. Use `tweet_action` only for approved writes, private reads, monitors, webhooks, extraction jobs, media, or giveaway draws when `HERMES_TWEET_ENABLE_ACTIONS=true`.

## Use Cases

- Social listening and launch monitoring.
- Creator, brand, and community research.
- Support triage from public mentions or profiles.
- Giveaway and follower evidence checks.
- Drafting or publishing X posts through an explicit approval step.

## Guardrails

- Never request or reveal API keys, passwords, cookies, signing keys, or TOTP secrets.
- Never pass credentials in tool arguments.
- Do not guess endpoint paths; use `tweet_explore`.
- Keep `tweet_action` disabled for unattended or read-only workflows.
- For remote gateway profiles, install and configure Hermes Tweet on the remote Hermes host where plugin tools execute.
