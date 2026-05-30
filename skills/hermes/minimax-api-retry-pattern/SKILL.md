---
name: minimax-api-retry-pattern
version: 1.0.0
author: Roven
source: locally-developed
platform: hermes
description: Implement user-visible retry handling for MiniMax API rate limits and transient generation failures.
updated: 2026-05-31
---

# MiniMax API Retry Pattern

Use this skill when MiniMax image, music, or related API calls need reliable retry behavior inside a Telegram bot. The local lesson: retries must inform the user while the synchronous API call is cooling down.

## Retryable Errors

| Code | Meaning | Applies To |
| --- | --- | --- |
| 1004 | Rate limit | Image and music |
| 1033 | Internal service error | Image and music |
| 2151 | Music payload preparation failed | Music |

## Core Pattern

The generation function may be synchronous, but Telegram progress messages are async. Pass the callback query or message context into the function and schedule progress updates from the event loop.

Pseudo-structure:

```python
def generate_image(prompt, query=None, max_attempts=3, delay=30):
    for attempt in range(max_attempts):
        if query:
            schedule_progress_message(query, attempt, max_attempts)
        result = call_minimax_with_curl(prompt)
        if result.ok:
            return result.urls
        if result.code not in {1004, 1033}:
            raise RuntimeError(result.message)
        time.sleep(delay)
    raise RuntimeError("MiniMax generation failed after retries")
```

## User Messaging

Tell the user what is happening:

- first retry: rate limit, waiting 30 seconds;
- second retry: still cooling down;
- final failure: ask whether to retry later or simplify prompt.

## Curl Notes

Use explicit timeouts. Music generation may need longer than image generation. Do not dump full headers or keys into logs.

## Guardrails

- Never hard-code `sk-...` keys.
- Retry only known transient errors.
- Do not infinite-loop paid API calls.
- Log request IDs and sanitized error messages, not secrets.
