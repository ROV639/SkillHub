# SkillHub 双机合并分析 v1

生成时间：2026-05-25 19:52:07

## 结论

- 现在应该先做合并分析和分级，不建议直接把 Skill 本体推到 GitHub。
- `robin_mac` 的 Skill 数量明显更大，且 `altman/research` 占比高，应默认进入候选/外部未验证池。
- `old_mac` 更适合作为补充来源，优先找只在旧机存在且不是系统内置的 Skill。
- 所有 `secret_risk=true` 的 Skill 暂不进入 `skills/ready/`。

## 总览

| 指标 | 数量 |
| --- | --- |
| robin_mac skills | 314 |
| old_mac skills | 130 |
| 合计记录 | 444 |
| 唯一名称 | 410 |
| 跨机器同名 | 4 |
| 同名但 hash 不同 | 0 |
| 完全重复 hash 组 | 7 |
| 只在 robin_mac | 287 |
| 只在 old_mac | 119 |
| secret risk 记录 | 1 |
| external/research 候选记录 | 234 |

## 来源分布

| 机器 | 来源 | 数量 |
| --- | --- | --- |
| old_mac | codex | 5 |
| old_mac | codex_vendor | 38 |
| old_mac | openclaw | 52 |
| old_mac | plugins | 28 |
| old_mac | workplace | 7 |
| robin_mac | altman/arthur | 1 |
| robin_mac | altman/research | 197 |
| robin_mac | altman/roveve | 1 |
| robin_mac | altman/skills_ready | 5 |
| robin_mac | ~/.agentProject/.agents/skills | 28 |
| robin_mac | ~/.agents/skills | 50 |
| robin_mac | ~/.claude/skills | 8 |
| robin_mac | ~/.openclaw/workspace/skills | 24 |

## 同名但内容不同

- 无

## 只在 old_mac 的 Skill

| Skill | 来源 | 文件数 | secret | 路径 |
| --- | --- | --- | --- | --- |
| 1password | openclaw | 3 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/1password |
| access | plugins | 1 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/discord/skills/access |
| access | plugins | 1 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/telegram/skills/access |
| access | plugins | 1 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/imessage/skills/access |
| agent-development | plugins | 7 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/plugin-dev/skills/agent-development |
| apple-notes | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/apple-notes |
| apple-reminders | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/apple-reminders |
| arthur_observatory_production | workplace | 32 | False | /Users/Robin/Documents/claude-codex-workplace/Dionysus_Theater/skills/arthur_observatory_production |
| aspnet-core | codex_vendor | 17 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/aspnet-core |
| bear-notes | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/bear-notes |
| blogwatcher | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/blogwatcher |
| blucli | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/blucli |
| build-mcp-app | plugins | 7 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app |
| build-mcp-server | plugins | 9 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server |
| build-mcpb | plugins | 3 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb |
| camsnap | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/camsnap |
| canvas | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/canvas |
| cardputer-buddy | plugins | 1 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/cwc-makers/skills/cardputer-buddy |
| chatgpt-apps | codex_vendor | 11 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/chatgpt-apps |
| claude-automation-recommender | plugins | 6 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender |
| claude-md-improver | plugins | 4 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver |
| clawhub | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/clawhub |
| cli-creator | codex_vendor | 4 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/cli-creator |
| cloudflare-deploy | codex_vendor | 312 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/cloudflare-deploy |
| coding-agent | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/coding-agent |
| command-development | plugins | 11 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/plugin-dev/skills/command-development |
| configure | plugins | 1 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/discord/skills/configure |
| configure | plugins | 1 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/telegram/skills/configure |
| configure | plugins | 1 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/imessage/skills/configure |
| discord | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/discord |
| eightctl | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/eightctl |
| example-command | plugins | 1 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/example-plugin/skills/example-command |
| example-skill | plugins | 1 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/example-plugin/skills/example-skill |
| figma | codex_vendor | 8 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/figma |
| figma-code-connect-components | codex_vendor | 8 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/figma-code-connect-components |
| figma-create-design-system-rules | codex_vendor | 8 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/figma-create-design-system-rules |
| figma-create-new-file | codex_vendor | 7 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/figma-create-new-file |
| figma-generate-design | codex_vendor | 7 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/figma-generate-design |
| figma-generate-library | codex_vendor | 23 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/figma-generate-library |
| figma-implement-design | codex_vendor | 6 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/figma-implement-design |
| figma-use | codex_vendor | 29 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/figma-use |
| frontend-design | plugins | 1 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/frontend-design/skills/frontend-design |
| gemini | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/gemini |
| gh-address-comments | codex_vendor | 6 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/gh-address-comments |
| gh-fix-ci | codex_vendor | 6 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/gh-fix-ci |
| gh-issues | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/gh-issues |
| gifgrep | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/gifgrep |
| github | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/github |
| gog | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/gog |
| goplaces | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/goplaces |
| gsap | workplace | 3 | False | /Users/Robin/Documents/claude-codex-workplace/Dionysus_Theater/📡VideoAI工坊/hyperframes_vertical/node_modules/hyperframes/dist/skills/gsap |
| hatch-pet | codex_vendor | 14 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/hatch-pet |
| healthcheck | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/healthcheck |
| himalaya | openclaw | 3 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/himalaya |
| hook-development | plugins | 11 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/plugin-dev/skills/hook-development |
| hyperframes | workplace | 46 | False | /Users/Robin/Documents/claude-codex-workplace/Dionysus_Theater/📡VideoAI工坊/hyperframes_vertical/node_modules/hyperframes/dist/skills/hyperframes |
| hyperframes-cli | workplace | 1 | False | /Users/Robin/Documents/claude-codex-workplace/Dionysus_Theater/📡VideoAI工坊/hyperframes_vertical/node_modules/hyperframes/dist/skills/hyperframes-cli |
| imagegen | codex | 12 | False | /Users/Robin/.codex/skills/.system/imagegen |
| imsg | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/imsg |
| jupyter-notebook | codex_vendor | 12 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/jupyter-notebook |
| linear | codex_vendor | 5 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/linear |
| m5-onboard | plugins | 1 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/cwc-makers/skills/m5-onboard |
| math-olympiad | plugins | 11 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/math-olympiad/skills/math-olympiad |
| mcp-integration | plugins | 7 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/plugin-dev/skills/mcp-integration |
| mcporter | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/mcporter |
| migrate-to-codex | codex_vendor | 19 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/migrate-to-codex |
| model-usage | openclaw | 4 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/model-usage |
| nano-pdf | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/nano-pdf |
| netlify-deploy | codex_vendor | 8 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/netlify-deploy |
| node-connect | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/node-connect |
| notion | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/notion |
| notion-knowledge-capture | codex_vendor | 18 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/notion-knowledge-capture |
| notion-meeting-intelligence | codex_vendor | 19 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/notion-meeting-intelligence |
| notion-research-documentation | codex_vendor | 23 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/notion-research-documentation |
| notion-spec-to-implementation | codex_vendor | 19 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/notion-spec-to-implementation |
| openai-docs | codex | 9 | False | /Users/Robin/.codex/skills/.system/openai-docs |
| openai-docs | codex_vendor | 9 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/openai-docs |
| openai-whisper | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/openai-whisper |
| openai-whisper-api | openclaw | 2 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/openai-whisper-api |
| openhue | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/openhue |
| oracle | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/oracle |
| ordercli | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/ordercli |
| peekaboo | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/peekaboo |
| playground | plugins | 7 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/playground/skills/playground |
| playwright | codex_vendor | 9 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/playwright |
| playwright-interactive | codex_vendor | 6 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/playwright-interactive |
| plugin-creator | codex | 6 | False | /Users/Robin/.codex/skills/.system/plugin-creator |
| plugin-settings | plugins | 8 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/plugin-dev/skills/plugin-settings |
| plugin-structure | plugins | 7 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/plugin-dev/skills/plugin-structure |
| poseidon-content-recon | workplace | 2 | False | /Users/Robin/Documents/claude-codex-workplace/Poseidon_Aigai/skills/poseidon-content-recon |
| render-deploy | codex_vendor | 21 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/render-deploy |
| sag | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/sag |
| screenshot | codex_vendor | 11 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/screenshot |
| security-best-practices | codex_vendor | 13 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/security-best-practices |
| security-ownership-map | codex_vendor | 8 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/security-ownership-map |
| security-threat-model | codex_vendor | 5 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/security-threat-model |
| sentry | codex_vendor | 5 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/sentry |
| session-logs | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/session-logs |
| session-report | plugins | 3 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/session-report/skills/session-report |
| sherpa-onnx-tts | openclaw | 2 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/sherpa-onnx-tts |
| skill-development | plugins | 2 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/plugin-dev/skills/skill-development |
| skill-installer | codex | 8 | False | /Users/Robin/.codex/skills/.system/skill-installer |
| slack | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/slack |
| songsee | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/songsee |
| sonoscli | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/sonoscli |
| speech | codex_vendor | 16 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/speech |
| spotify-player | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/spotify-player |
| taskflow | openclaw | 3 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/taskflow |
| taskflow-inbox-triage | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/taskflow-inbox-triage |
| themis-agent-governance | workplace | 1 | False | /Users/Robin/Documents/claude-codex-workplace/OldMac_Agent_Altman_Themis_Deployment/Themis_Hermes/skills/themis-agent-governance |
| themis-background-audit | workplace | 1 | False | /Users/Robin/Documents/claude-codex-workplace/OldMac_Agent_Altman_Themis_Deployment/Themis_Hermes/skills/themis-background-audit |
| things-mac | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/things-mac |
| tmux | openclaw | 3 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/tmux |
| transcribe | codex_vendor | 7 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/transcribe |
| trello | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/trello |
| vercel-deploy | codex_vendor | 6 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/vercel-deploy |
| video-frames | openclaw | 2 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/video-frames |
| voice-call | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/voice-call |
| wacli | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/wacli |
| weather | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/weather |
| winui-app | codex_vendor | 21 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/winui-app |
| writing-rules | plugins | 1 | False | /Users/Robin/.claude/plugins/marketplaces/claude-plugins-official/plugins/hookify/skills/writing-rules |
| xurl | openclaw | 1 | False | /Users/Robin/Documents/Agent/npm/lib/node_modules/openclaw/skills/xurl |
| yeet | codex_vendor | 5 | False | /Users/Robin/.codex/vendor_imports/skills/skills/.curated/yeet |

## Secret Risk 暂停清单

| Skill | 机器 | 来源 | 路径 |
| --- | --- | --- | --- |
| bluesky | robin_mac | altman/research | /Users/robin/AltmanCodex/ONE_SPARK/_workspace/research_raw/openclaudia-skills/skills/bluesky |

## 建议动作

1. 先提交并推送仓库结构、扫描脚本、两份 manifest 和本报告。
2. 暂不上传 Skill 本体，避免把研究素材、旧版和敏感风险一起推上去。
3. 下一步生成 `promotion_plan.json`，只挑选：只在旧机存在、自写、非 secret、非 research/external 的候选。
4. 再按候选清单复制 Skill 本体到 `skills/lab/`，人工确认后升到 `skills/ready/`。
