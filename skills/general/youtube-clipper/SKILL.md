---
name: youtube-clipper
version: 1.0.0
author: Roven
source: locally-developed
platform: universal
description: Convert YouTube links into structured clipping notes with metadata, transcript notes, and reusable insights.
updated: 2026-05-31
---

# YouTube Clipping Archive Workflow

Use this skill when a YouTube link should become a structured clipping note, research note, or source archive. The goal is one complete markdown file with source metadata, transcript-derived notes, and a reusable summary.

## Trigger

Use this when the user sends a YouTube link and asks for a clipping report, archive note, transcript summary, or structured analysis.

## File Naming

Use:

```text
Author - Chinese or translated title.md
```

Avoid characters that break sync or shell tools.

## Standard Structure

```markdown
---
time: "YYYY-MM-DDTHH:MM:SS+08:00"
title: "Original title"
source: "https://www.youtube.com/watch?v=..."
author:
  - "Author"
published: YYYY-MM-DD
created: YYYY-MM-DD
tags:
  - youtube
  - clipping
---

# Title

## Source Summary

## Key Claims

## Transcript Notes

## Reusable Ideas

## Follow-up Questions
```

## Workflow

1. Extract metadata: title, channel, URL, publish date.
2. Fetch transcript when available.
3. If transcript is missing, mark the gap instead of inventing details.
4. Build a single markdown note.
5. Keep claims traceable to transcript or video metadata.
