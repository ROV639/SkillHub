---
name: redbook-creator-publish
version: 1.0.0
author: Roven
source: locally-developed
platform: universal
description: Prepare RedNote/Xiaohongshu post drafts, image plans, and publish packages with human approval gates.
updated: 2026-05-31
---

# RedNote Creator and Publish Workflow

Use this skill to draft RedNote/Xiaohongshu-style posts, plan accompanying images, and prepare a publish package. Publishing or account actions require explicit human confirmation.

## Environment Checks

```bash
python3 --version
python3 -c "import playwright" 2>/dev/null && echo "Playwright installed" || echo "Playwright missing"
which ffmpeg || true
```

## Workflow

### 1. Pick the Topic

If the user provides a topic, use it. If not, research current AI/tool/productivity topics and present options before drafting.

### 2. Draft the Post

Create:

- a title under 20 Chinese characters when targeting RedNote;
- a strong opening hook;
- 3 to 6 short sections;
- practical takeaways;
- image/card suggestions;
- hashtags.

### 3. Image Plan

For each image, define:

- purpose,
- card text,
- visual style,
- aspect ratio,
- source or generation prompt.

### 4. Publish Package

Return a structured package with title, body, image list, hashtags, first comment, and risks.

## Guardrails

- Do not log into RedNote or publish without explicit confirmation.
- Do not invent personal experience, numbers, screenshots, or platform results.
- Keep generated images and claims reviewable before upload.
