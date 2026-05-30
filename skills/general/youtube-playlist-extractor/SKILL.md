---
name: youtube-playlist-extractor
version: 1.0.0
author: Roven
source: locally-developed
platform: universal
description: Extract YouTube playlist or channel video lists with yt-dlp while avoiding playlist coverage gaps.
updated: 2026-05-31
---

# YouTube Playlist and Channel Extractor

Use this skill when extracting video URLs from a playlist or channel with `yt-dlp`. The practical lesson: playlists often miss newer videos, so the channel videos page is usually more complete.

## Key Finding

Playlist mode only returns videos included in that playlist. Channel mode can catch videos that have not been added to a playlist yet.

## Commands

Extract a playlist:

```bash
yt-dlp --flat-playlist --print "%(title)s|%(url)s" "PLAYLIST_URL"
```

Extract a channel videos page:

```bash
yt-dlp --flat-playlist --print "%(title)s|%(url)s" "https://www.youtube.com/@CHANNEL/videos"
```

## Recommended Flow

1. Start with the channel videos page for maximum coverage.
2. Save title and URL pairs.
3. Filter by keyword or publish date.
4. Use playlist extraction only when the playlist itself is the object of study.
5. Record which extraction mode was used.
