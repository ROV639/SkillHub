# SkillHub 项目适配图谱 v1

日期：2026-05-25

## 0. 结论

当前 SkillHub 应该按项目使用，而不是所有项目都装同一批 Skill。

最直接的对应关系：

- `Arthur_Observatory`：视频生产、旁白、FINAL 验收，适合语音、视频规划、信息图，不适合社媒自动发布。
- `Eve_Frames`：EVE 人像图组和多平台文案，适合封面、图卡、品牌语气、社媒草稿，但生图仍按项目授权边界。
- `Rov_Eve`：固定角色 AI 生活教程图文，适合图卡、漫画、配图规划、内容复用。
- `ONE_SPARK`：账号体检、平台边界、社媒合规，适合社媒草稿、Google 工作区闸门、营销文案、证据研究。
- `MacBook_Rovin`：远程设备、配置排查、SkillHub 运维，适合证据研究、Skill 建造、知识库、办公资产。
- `RUBIN的书架`：个人资料区，默认不应用自动整理 Skill，除非 Robin 点名。

## 1. 项目 × Skill 推荐

| 项目 | 适合优先使用 | 适合但需确认 | 不建议默认使用 |
|---|---|---|---|
| `Arthur_Observatory` | `rubin-minimax-tts-workshop`, `rubin-manga-video-planner`, `rubin-infographic-workshop`, `rubin-office-asset-workbench` | `rubin-diagram-workshop`, `rubin-marketing-copy-lab` | `rubin-social-draft-repurposer` 真实发布部分、Google Gmail 自动化 |
| `Eve_Frames` | `rubin-cover-image-workshop`, `rubin-xhs-card-workshop`, `rubin-brand-voice-gate`, `rubin-social-draft-repurposer` | `rubin-article-illustration-planner`, `rubin-marketing-copy-lab` | 未授权直接生图、自动发布 |
| `Rov_Eve` | `rubin-xhs-card-workshop`, `rubin-comic-card-workshop`, `rubin-article-illustration-planner`, `rubin-content-repurposer` | `rubin-manga-video-planner`, `rubin-social-draft-repurposer` | 跳过角色锁定的视觉 Skill |
| `ONE_SPARK` | `rubin-social-draft-repurposer`, `rubin-google-workspace-gate`, `rubin-marketing-copy-lab`, `rubin-evidence-lab` | `rubin-url-markdown-intake`, `rubin-knowledge-base-builder` | 任何真实自动互动、批量账号操作、绕过风控 |
| `MacBook_Rovin` | `rubin-skill-builder`, `rubin-knowledge-base-builder`, `rubin-evidence-lab`, `rubin-office-asset-workbench` | `rubin-google-workspace-gate` 只做权限模型 | 内容生图、社媒执行、账号写操作 |
| `SkillHub` | `rubin-skill-builder`, `rubin-agent-orchestration-reference`, `rubin-knowledge-base-builder`, `rubin-diagram-workshop` | `rubin-google-workspace-gate` 用于文档同步设计 | 直接安装外部未验证 Skill |

## 2. 项目说明

### Arthur_Observatory

核心目标是地缘经济视频的 FINAL 包。最有价值的是：

1. `rubin-minimax-tts-workshop`：把旁白脚本转成 TTS 任务包和音频验收。
2. `rubin-manga-video-planner`：用于短视频分镜和镜头节奏，不替代现有导演包门禁。
3. `rubin-infographic-workshop`：适合把宏观概念、时间线、经济结构做成画面资产。
4. `rubin-office-asset-workbench`：用于最终报告、制作说明、交付包整理。

### Eve_Frames

核心目标是 EVE 成品候选图组和多平台文案。适合：

1. `rubin-cover-image-workshop`：封面方向与构图。
2. `rubin-xhs-card-workshop`：图组发布包结构。
3. `rubin-brand-voice-gate`：保持文案不像模板 AI。
4. `rubin-social-draft-repurposer`：生成小红书、抖音、快手、微信草稿，但不发布。

### Rov_Eve

核心目标是 ROV × EVE 固定角色 AI 生活教程图文。适合：

1. `rubin-comic-card-workshop`：教程漫画化。
2. `rubin-article-illustration-planner`：每页图文信息层规划。
3. `rubin-xhs-card-workshop`：小红书图卡结构。
4. `rubin-content-repurposer`：把同一集改成多平台版本。

### ONE_SPARK

核心目标是多平台账号体检、协同与合规边界。适合：

1. `rubin-evidence-lab`：平台规则、工具、账号策略证据核查。
2. `rubin-social-draft-repurposer`：只做草稿包和发布包 schema。
3. `rubin-google-workspace-gate`：用于账号资料、表格、文档协作的权限边界。
4. `rubin-marketing-copy-lab`：用于变现评分、账号定位和转化文案。

### MacBook_Rovin

核心目标是本机/副机配置排查、SkillHub 运维和调研落地。适合：

1. `rubin-skill-builder`：把调研结果变成本地 Skill。
2. `rubin-knowledge-base-builder`：整理报告、索引、项目知识。
3. `rubin-evidence-lab`：外部仓库和工具调研。
4. `rubin-office-asset-workbench`：把调研结果变成可交付文档。

## 3. MiniMax 可接的项目任务

MiniMax 适合做：

1. `Eve_Frames` / `Rov_Eve`：草稿文案、图卡页文案、平台改写、标签建议。
2. `Arthur_Observatory`：旁白候选、TTS 任务包、分镜草案、QC 初稿。
3. `ONE_SPARK`：账号体检表初稿、风险词扫描、平台草稿包。
4. `MacBook_Rovin` / `SkillHub`：README 摘要、风险卡、使用卡、评分卡初稿。

MiniMax 不负责：

1. 最终入库 READY 判断。
2. 真实账号发布、互动、发送邮件。
3. 读取 cookie/session/token。
4. 修改项目规则或正式 Git 推送。

## 4. 下一步测试建议

先按项目实测：

1. `MacBook_Rovin`：测 `rubin-skill-builder`，把一个外部候选转成 Rubin Skill。
2. `Arthur_Observatory`：测 `rubin-minimax-tts-workshop`，用一段旁白生成 TTS 任务包。
3. `Rov_Eve`：测 `rubin-comic-card-workshop`，把一个 AI 生活技巧转成 6 格漫画分镜。
4. `ONE_SPARK`：测 `rubin-social-draft-repurposer`，生成一组多平台草稿包。
5. `Eve_Frames`：测 `rubin-brand-voice-gate`，检查一篇多平台文案。
