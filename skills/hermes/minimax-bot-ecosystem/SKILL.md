---
name: minimax-bot-ecosystem
version: 1.0.0
author: Roven
source: locally-developed
platform: hermes
description: Coordinate the local MiniMax Telegram bot family across image, image-to-image, music, lyrics, and TTS workflows.
updated: 2026-05-31
---

# MiniMax Telegram Bot Ecosystem

Use this skill when coordinating the local MiniMax Telegram bot family. The system is easier to maintain when every bot owns one command and the cross-bot handoffs are explicit.

## Command Map

| Command | Job | Typical Follow-up |
| --- | --- | --- |
| `/img` | Text-to-image | Continue into image-to-image |
| `/pix` | Image-to-image / character consistency | Save or refine |
| `/bgm` | Background music | Generate lyrics |
| `/lyc` | Lyrics | Generate music |
| `/tts` | Speech synthesis | Package audio asset |

## Design Principle

Each bot should be independently restartable. Shared state should be minimal, visible, and stored in predictable files. Avoid one giant bot that owns every workflow and fails as one unit.

## Maintenance Checklist

1. Confirm every command responds.
2. Confirm each bot reads keys from environment or secure config.
3. Confirm logs do not print full prompts when private user material is present.
4. Confirm cross-command buttons point to the right command.
5. Keep a single ecosystem note with command names, script paths, and log paths.

## Handoff Pattern

When one bot suggests continuing in another bot, include:

- the next command,
- what data should be carried over,
- whether the user must upload a file,
- and what will be lost if they start fresh.
