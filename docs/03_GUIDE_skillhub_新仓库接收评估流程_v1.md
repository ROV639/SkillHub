# SkillHub 新仓库接收评估流程 v1

日期：2026-05-25  
用途：当 Robin 丢给 Agent 一个新仓库、新 Skill、工具集合、工作流仓库时，统一按本流程分析、分类、评价和推荐。

## 0. 触发条件

Robin 发送：

- GitHub 仓库 URL
- Skill 仓库
- 单个 Skill 目录
- 工具/工作流项目
- 社媒自动化项目
- 多 Agent 长工作流
- “看看这个有没有用”

都按本流程执行。

## 1. 固定流程

```text
接收仓库
→ 登记来源
→ 读取 README / docs / SKILL.md / package files
→ 判断类型
→ 风险分级
→ Rubin 价值评分
→ 给推荐动作
→ 输出决策卡
→ 必要时生成评分卡
→ 写入 SkillHub 索引或报告
```

## 2. 分类

| 分类 | 含义 |
|---|---|
| `rubin-original` | Rubin 自建 |
| `rubin-adapted-candidate` | 值得改写成本地版本 |
| `external-sandbox` | 可沙盒测试 |
| `external-reference` | 只读参考 |
| `blocked-prod` | 可研究，但禁止生产 |

## 3. 风险分级

| 风险 | 规则 |
|---|---|
| R0 | 纯文档/提示词 |
| R1 | 读本地文件或公开网页 |
| R2 | API、生图、下载、外部服务 |
| R3 | 登录态、cookie、账号草稿、浏览器 session |
| R4 | 真实发布、互动、删除、远程执行 |

## 4. 评分维度

| 维度 | 权重 |
|---|---:|
| Rubin 变现价值 | 25% |
| 直接可用性 | 20% |
| 输出可控性 | 20% |
| 安全/权限风险 | 15% |
| 维护与反馈 | 10% |
| 可复盘性 | 10% |

## 5. 推荐动作

| 动作 | 含义 |
|---|---|
| SHIP | 可进入下一步或 ready |
| FIX-FIRST | 有价值，需先改写或补测试 |
| HOLD | 有价值但不急 |
| BLOCK | 不建议继续投入或禁止生产 |

## 6. 输出格式

默认输出决策卡：

```text
结论：
分类：
风险等级：
证据等级：
Rubin 价值：
可直接学习：
需要改写：
只读参考：
禁止生产：
推荐动作：
下一步：
```

需要入库时，再生成：

- `scorecards/<skill-or-repo>.md`
- `reports/NN_REPORT_<repo>_评估_v1.md`
- 更新 `SKILL_INDEX.md`
- 更新 `registry/skills_index.json`
- 更新 `CHANGELOG.md`

## 7. MiniMax agent 分工

可交给 MiniMax agent：

- README 摘要
- SKILL.md 摘要
- 风险关键词扫描
- 字段提取
- 使用卡初稿
- 评分卡初稿

必须由 Codex / Robin 判断：

- 是否晋升 ready
- 是否接账号/API key
- 是否写正式 Skill 路径
- 是否推送 GitHub
- 是否允许发布/互动/自动化

