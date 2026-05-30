---
name: qwen-research-2026
version: 1.0.0
author: Roven
source: locally-developed
platform: universal
description: Research Qwen models, qwen.ai features, pricing, and limits with source priority and browser verification.
updated: 2026-05-31
---

# Qwen Research 2026

Use this skill when researching Qwen, qwen.ai, Qwen model releases, API limits, pricing, or feature availability. Qwen information changes quickly and many pages are client-rendered, so prefer direct browser verification and official sources.

## Source Priority

| Priority | Source | Use For |
| --- | --- | --- |
| 1 | `chat.qwen.ai` direct browser access | Visible UI, account tier, feature list |
| 2 | `qwenlm.github.io/blog/` | Model releases and technical posts |
| 3 | Hugging Face `Qwen/*` model cards | Model specs and usage modes |
| 4 | `qwen.ai/pricing` | Pricing, if accessible in browser |
| 5 | Search results | Discovery only, verify elsewhere |

## Known Limitations

- Some Qwen pages are client-side rendered; curl may return only shell HTML.
- Pricing, quota, and rate limits may require logged-in UI access.
- Search availability varies by region.

## Checklist

```text
[ ] Confirm user region/account tier if relevant.
[ ] Visit qwen.ai or chat.qwen.ai in browser when current pricing or UI matters.
[ ] Check Qwen blog posts from 2025 onward.
[ ] Check Hugging Face model cards for Qwen3/Qwen latest models.
[ ] Separate verified facts from assumptions.
[ ] Record source URLs and access date.
```

## Output

Return a compact matrix: model, interface, access method, price/quota if verified, limits, evidence URL, and confidence.
