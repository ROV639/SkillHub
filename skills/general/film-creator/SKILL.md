---
name: film-creator
version: 1.0.0
author: Roven
source: locally-developed
platform: universal
description: Turn a short idea or image reference into a 30-second cinematic screenplay, shot list, and assembly plan.
updated: 2026-05-31
---

# Film Creator

Use this skill to turn a short idea, sentence, or image reference into a 30-second cinematic video plan. It produces the creative analysis, screenplay, shot list, generation prompts, and FFmpeg assembly plan.

## Core Capabilities

1. Analyze the concept, emotional tone, and visual style.
2. Write a compact three-act script for 30 seconds.
3. Plan 5 to 6 shots, roughly 5 seconds each.
4. Generate prompts for video backends when available.
5. Assemble clips with FFmpeg when the assets are ready.

## Environment Check

```bash
which ffmpeg
which node && node --version
```

Optional backends may require their own CLI or API keys. Do not request or store keys in the skill.

## Script Template

```markdown
# Screenplay: [Title]

## Basic Info
- Genre:
- Mood:
- Duration: 30 seconds
- Scenes: 6

## Shot Script

### Shot 1: Establishing Moment [0-5s]
Camera:
Action:
Dialogue / Voiceover:
Generation prompt:
```

## Assembly

After clips are generated, use FFmpeg to normalize resolution, frame rate, and audio before concatenation. Always inspect the final file before delivery.
