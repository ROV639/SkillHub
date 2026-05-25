# 证据研究所回测报告：baoyu-skills

日期：2026-05-25  
执行 Skill：`rubin-evidence-lab`  
任务等级：L2 标准调研  
回测对象：JimLiu / baoyu-skills  
来源核查日期：2026-05-25

## 决策卡

结论：FIX-FIRST

证据等级：强

可用价值：高。`baoyu-skills` 覆盖内容生产、图像、网页转 Markdown、公众号 HTML、小红书图卡、信息图、SVG 图解等 Rubin 高频场景。

商业价值：高。它能支持教程、公众号、小红书图文、AI 工具内容、内容生产流水线评估。

内容转化：高。`baoyu-xhs-images`、`baoyu-infographic`、`baoyu-diagram`、`baoyu-markdown-to-html` 都能转成 Rubin 内容链路候选。

系统迁移：中高。方法和参数体系值得吸收，但不应全量安装或原样进入 `ready/`。

风险：中。低风险内容类 skill 可沙盒测试；发布类、danger 类、登录态类必须隔离。

建议动作：FIX-FIRST

下一步：把 `baoyu-skills` 放入 `external_unverified/` 作为外部样本池，并优先测试 7 个低风险内容类 skill。

## 已验证事实

| 事实 | 来源 | 证据等级 | 备注 |
|---|---|---|---|
| GitHub 页面显示该仓库为 Public，约 19.5k stars、2.3k forks、688 commits | GitHub 仓库页 | A | 当前页面值，后续会变化 |
| README 提示不要一次性安装 20+ skills，因为会增加 Agent 上下文负担 | README / README.zh.md | A | 支持按需收录策略 |
| 仓库支持将 `skills/baoyu-*` 作为单个 ClawHub skill 发布，并支持 `--dry-run` | README / README.zh.md | A | 值得借鉴发布预览机制 |
| `baoyu-xhs-images` 支持 Style × Layout 系统和 palette 覆盖 | README / README.zh.md | A | 可改写为 Rubin 小红书图卡工坊 |
| `baoyu-infographic` 支持多种 layout、style、aspect 和 lang 参数 | README / README.zh.md | A | 可改写为 Rubin 信息图工坊 |
| `baoyu-diagram` 输出自包含 SVG，支持 flowchart、sequence、structural、illustrative、class | README / README.zh.md | A | 可改写为 Rubin 图解工坊 |
| 仓库包含内容技能、AI 生成技能、工具技能三类 | README / README.zh.md | A | 分类可参考但不照搬 |

## 可直接学习

1. 不全量安装，按需选择具体 skill。
2. 每个 skill 独立发布/安装，而不是一个大包全进上下文。
3. `--dry-run` 预览机制。
4. 视觉类 skill 的参数体系：style、layout、palette、aspect、lang。
5. SVG 图解优先用于结构准确的教程图。

## 需要改写

| 原型 | Rubin 改写方向 |
|---|---|
| `baoyu-diagram` | `rubin-diagram-workshop`：架构图、教程图、流程图 |
| `baoyu-infographic` | `rubin-infographic-workshop`：信息结构转图 |
| `baoyu-xhs-images` | `rubin-xhs-card-workshop`：图卡草稿、钩子、版式 QC |
| `baoyu-url-to-markdown` | `rubin-url-evidence-capture`：公开网页取证 |
| `baoyu-markdown-to-html` | `rubin-wechat-html-format`：公众号 HTML 排版 |
| `baoyu-youtube-transcript` | `rubin-youtube-transcript-capture`：视频字幕取证 |

## 只读参考 / 受限

| 类型 | 处理 |
|---|---|
| 发布类 skill | 只研究草稿、预览、字段结构；不做实发 |
| danger 类 skill | 只读研究；不读取真实 cookie / token |
| 需要登录态的 skill | 进入受限区，必须人工确认 |
| 需要 API key 的 skill | 进入 R2/R3，先做环境检查 |

## 回测结论

`rubin-evidence-lab` 能完成这次 L2 调研：输出了决策卡、事实表、风险分层、迁移建议和下一步动作。它可以继续保留在 LAB，但尚未满足 READY 条件，因为还需要：

1. 再完成一次工具/API 调研回测。
2. 再完成一次内容事实核查回测。
3. 形成正式评分卡闭环。

## 来源

- GitHub 仓库页：https://github.com/JimLiu/baoyu-skills
- README：https://raw.githubusercontent.com/JimLiu/baoyu-skills/main/README.md
- README 中文：https://raw.githubusercontent.com/JimLiu/baoyu-skills/main/README.zh.md

