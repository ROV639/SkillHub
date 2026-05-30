---
name: hermes-telegram-buttons
version: 1.0.0
author: Roven
source: locally-developed
platform: hermes
description: Add native Telegram inline buttons to Hermes workflows without relying on text-only clarification prompts.
updated: 2026-05-31
---

# Hermes Telegram Buttons

Use this skill when Hermes needs real Telegram inline buttons instead of plain-text clarification options. The important lesson: a generic clarify flow does not render native Telegram buttons. Native buttons require Telegram Bot API `reply_markup.inline_keyboard` and callback handling in the Telegram platform code.

## What Works

| Approach | Native Telegram Buttons | Notes |
| --- | --- | --- |
| Clarify-style text choices | No | Renders as text only |
| BotFather-style buttons | Yes | Uses Telegram Bot API directly |
| Hermes platform patch | Yes | Best option for owned Hermes deployments |

## Implementation Shape

Patch Hermes in three places:

1. Register a command such as `/img` in the command registry.
2. Send a Telegram message with `reply_markup.inline_keyboard`.
3. Add callback handling in `gateway/platforms/telegram.py`.

## Minimal Callback Pattern

Use a prefix that cannot collide with existing callbacks:

```python
# Example callback_data values
img:menu
img:style:portrait
img:ratio:3x4
img:cancel
```

In the callback handler, route by prefix first, then parse the remaining segments. Store per-user state in the Telegram context or Hermes session state, not in a global singleton.

## Practical Debug Flow

```bash
grep -n "_handle_callback_query" ~/.hermes/hermes-agent/gateway/platforms/telegram.py
grep -n "CommandDef" ~/.hermes/hermes-agent/hermes_cli/commands.py
```

After patching:

1. Restart Hermes.
2. Send the command in Telegram.
3. Confirm buttons appear visually.
4. Click every branch once and watch gateway logs.
5. Only then wire the expensive action such as image generation.

## Guardrails

- Do not hard-code bot tokens. Read tokens from the existing Hermes config or environment.
- Keep callback data short; Telegram limits callback payload size.
- Add a Cancel button to every multi-step menu.
- Make repeated button clicks idempotent when possible.
