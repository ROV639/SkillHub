---
name: hermes-compression-debug
version: 1.0.0
author: Roven
source: locally-developed
platform: hermes
description: Diagnose Hermes automatic context compression failures and restore predictable compression behavior.
updated: 2026-05-31
---

# Hermes Compression Debug

Use this skill when Hermes automatic context compression triggers too late, does not trigger at all, or only works after a manual `/clear`.

## Symptoms

- Telegram reports context usage above 90% before compression begins.
- Manual `/clear` works, but automatic compression does not.
- The configured threshold appears correct, but the running process behaves as if it loaded an older config.

## Check the Config

```bash
grep -n "compact\|threshold\|compression" ~/.hermes/config.yaml
```

Expected shape:

```yaml
compression:
  enabled: true
  threshold: 0.5
  target_ratio: 0.2
  protect_last_n: 20
  summary_provider: auto
```

## Common Causes

| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| Threshold is 0.5 but compression happens near 96% | Telegram layer reports late or Hermes did not reload config | Restart Hermes; consider 0.7 if 0.5 is too aggressive |
| `enabled` is false | Config was overwritten | Set `enabled: true` and restart |
| Summary fails silently | Summary model/provider unavailable | Switch summary provider/model and test with a small chat |

## Recovery

1. Back up the config.
2. Set `enabled: true`.
3. Pick a conservative threshold for the current workload.
4. Restart Hermes.
5. Watch one long Telegram thread and record the actual trigger point.

Do not delete sessions as a first move. Sessions are evidence. Copy the relevant config and logs first.
