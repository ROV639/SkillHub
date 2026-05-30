---
name: social-card-design
version: 1.0.0
author: Roven
source: locally-developed
platform: universal
description: Turn content into publishable social card systems with layout, density, image, and thumbnail-readability checks.
updated: 2026-05-31
---

# Social Card Design System

Use this skill when turning written content into publishable visual cards: RedNote/Xiaohongshu carousels, vertical social cards, WeChat cover pairs, square post images, or multi-size social graphics. The workflow turns content into a visual system before creating images.

## Trigger Conditions

Use this skill for requests like:

- Create RedNote/Xiaohongshu cards.
- Turn this article into vertical social images.
- Make a WeChat cover image pair.
- Create a 3:4 or 4:5 visual post.
- Convert content into a publishable card set.

## Workflow

1. Identify the content type: opinion, tutorial, checklist, comparison, story, case study, or announcement.
2. Choose a visual system based on feeling, not category.
3. Decide card count and aspect ratio.
4. Draft every card: headline, body copy, visual cue, density level, and image need.
5. Check thumbnail readability before final output.

## Visual Systems

### Editorial Magazine / Paper Ink

Use for slower material: culture, travel, reflection, emotional writing, interviews, and essays. It should feel calm, printed, and intentional.

### Swiss International / Grid

Use for faster material: product comparisons, data, workflows, tool explainers, scoreboards, and operational notes. It should feel structured, sharp, and scannable.

Decision question: is this a feature article or a release note? Feature article means Editorial. Release note means Swiss.

## Density Rules

For vertical cards:

- Content should occupy at least 75% of the canvas.
- Any blank band taller than 15% of the canvas needs a reason.
- Do not center a tiny block of text between empty divs.
- Test at 360px width before approving.

## Text Over Images

1. Detect quiet zones and brightness first.
2. Map the subject area before placing text.
3. Add tint or mask only if thumbnail readability fails.

## Image Source Priority

1. User-provided photos.
2. Public or licensed documentary-style images.
3. Generated images when a specific visual concept is needed.
4. Abstract backgrounds only when content does not need inspection.

## Output Format

Return a card plan with: card number, headline, body, visual direction, layout, image source/prompt, and risk notes.
