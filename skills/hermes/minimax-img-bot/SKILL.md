---
name: minimax-img-bot
version: 1.0.0
author: Roven
source: locally-developed
platform: hermes
description: Maintain a MiniMax image-generation Telegram bot with safe token handling, prompt assembly, and retry-aware operations.
updated: 2026-05-31
---

# MiniMax Image Telegram Bot

Use this skill when maintaining or rebuilding the local MiniMax image-generation Telegram bot. It captures the working architecture, common failure modes, and safe launch pattern without exposing real bot tokens or API keys.

## What the Bot Does

The bot guides users through image generation with Telegram buttons. The working design uses category menus, live prompt preview, fixed navigation controls, and a direct custom input mode.

Typical categories:

- Female portrait
- Male portrait
- Landscape
- Styled objects
- Anime
- Custom prompt

## Sensitive Values

Do not hard-code secrets. Use placeholders in docs and environment variables in runtime.

```bash
export TELEGRAM_BOT_TOKEN="<telegram-bot-token>"
export MINIMAX_CN_API_KEY="<minimax-api-key>"
```

## Core Runtime Paths

```text
~/.hermes/scripts/minimax_img_bot.py
~/.hermes/logs/minimax_bot.log
```

## Architecture Rules

1. Prompt keyword dictionaries should be English only. Mixed-language keyword fragments are a common source of poor outputs.
2. Male and female portrait dictionaries must be separate. Do not reuse a single look dictionary.
3. `build_prompt()` should be the only prompt assembly path.
4. Button state should be explicit and visible to the user.
5. Navigation buttons should include main menu, back, and exit.

## Launch Pattern

```bash
nohup python3 ~/.hermes/scripts/minimax_img_bot.py "$TELEGRAM_BOT_TOKEN" > ~/.hermes/logs/minimax_bot.log 2>&1 &
sleep 3
tail -50 ~/.hermes/logs/minimax_bot.log
```

## Debug Checklist

- Token comes from environment or secure config.
- MiniMax API key comes from `MINIMAX_CN_API_KEY`.
- Curl timeout is long enough for image generation.
- Retry logic handles 1004 rate limits.
- Prompt preview shows the current selections before generation.
- No full key or token appears in logs, screenshots, README files, or SkillHub.
