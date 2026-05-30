---
name: hermes-telegram-inline-keyboard
version: 1.0.0
author: Roven
source: locally-developed
platform: hermes
description: Extend Hermes Telegram callback handling with custom inline keyboard prefixes and handlers.
updated: 2026-05-31
---

# Hermes Telegram Inline Keyboard Extension

Use this skill to add a custom inline-keyboard flow to Hermes Telegram without relying on clarify tools. Hermes already has callback plumbing for model picker and approvals; custom workflows need their own callback prefix and handler.

## Existing Callback Families

| Prefix | Purpose | Handler Area |
| --- | --- | --- |
| `mp:` / `mm:` | Model picker | model picker callback handler |
| `ea:` | Execution approval | generic callback query handler |
| `update_prompt:` | Prompt update | generic callback query handler |

Pick a new prefix, for example `img:`, `route:`, or `ops:`.

## Extension Steps

### 1. Locate the callback handler

```bash
grep -n "_handle_callback_query" ~/.hermes/hermes-agent/gateway/platforms/telegram.py
```

### 2. Add a prefix branch

Pseudo-structure:

```python
if data.startswith("img:"):
    await self._handle_image_callback(update, context, data)
    return
```

### 3. Build a dedicated handler

The handler should:

- Parse the callback payload.
- Load or initialize per-user state.
- Edit the existing message rather than spamming new messages.
- Render the next keyboard.
- Provide Cancel and Back branches.

### 4. Test in Telegram

Start with a non-expensive dry-run action. Once button routing is stable, connect the real task.

## Notes from Practice

- Callback collisions are painful. Prefixes are cheap; use one.
- Store state per user/session. Global state breaks when two people click buttons at once.
- For long-running tasks, acknowledge the click immediately, then update the message with progress.
