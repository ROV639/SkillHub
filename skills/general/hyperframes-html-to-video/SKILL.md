---
name: hyperframes-html-to-video
version: 1.0.0
author: Roven
source: locally-developed
platform: universal
description: Render deterministic animated videos from HTML, timing metadata, browser frames, and FFmpeg.
updated: 2026-05-31
---

# HyperFrames HTML-to-Video

Use this skill when a user wants deterministic animated video generated from HTML, CSS, JavaScript, GSAP, Lottie, or data-driven visual scenes. It is for generated motion graphics, chart videos, social title cards, and short explainers rather than timeline editing in CapCut or Premiere.

## Positioning

Input: an HTML file with timing attributes.

Output: MP4 rendered from headless Chrome frames and encoded with FFmpeg.

Animation engines: GSAP, Lottie, CSS transitions, canvas, or SVG.

## When to Use

- Animated social title cards.
- Data chart videos.
- Explainer motion graphics.
- Repeatable AI-generated short videos.
- CI-friendly rendering where the same input should produce the same output.

## Environment Check

```bash
node --version
ffmpeg -version
```

Install FFmpeg if missing:

```bash
brew install ffmpeg
```

## HTML Timing Contract

Use explicit timing attributes so the renderer does not have to infer intent:

```html
<section data-start="0" data-duration="4">...</section>
<section data-start="4" data-duration="5">...</section>
```

## Workflow

1. Define the video length, aspect ratio, and frame rate.
2. Build HTML with explicit scene timing.
3. Keep fonts local or web-safe.
4. Render a short preview first.
5. Inspect text clipping and animation timing.
6. Render final MP4.

## Division of Labor

- Use FFmpeg for encoding, joining, and format conversion.
- Use HyperFrames for generated animated scenes.
- Use manual editors only when human timing, voice, or complex subtitles need judgment.
