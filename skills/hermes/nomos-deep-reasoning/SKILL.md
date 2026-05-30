---
name: nomos-deep-reasoning
version: 1.0.0
author: Roven
source: locally-developed
platform: hermes
description: Force a three-layer reasoning check before execution to prevent shallow task interpretation and brittle plans.
updated: 2026-05-31
---

# Nomos Deep Reasoning

Use this skill before executing important Nomos tasks. The point is not to slow work down; it is to catch the three failures that repeatedly waste time: misunderstanding the user's real goal, missing hidden constraints, and answering from only the agent's point of view.

## Core Position

Question the task before executing it. A fast wrong answer is more expensive than a short reasoning pass.

## Three-Layer Check

### 1. Task Understanding

Ask:

- What did the user explicitly ask for?
- What underlying problem are they trying to solve?
- Are those two things aligned?

If the answer is unclear and a wrong assumption would be costly, ask the user.

### 2. Plan Weakness Scan

Before execution, ask:

1. What constraint is missing but likely exists?
2. What part is most likely to fail?
3. Is there a simpler or safer route?

Generate at least two possible paths for non-trivial tasks, then choose.

### 3. User-Reaction Check

Before final output, ask:

- What would the user challenge first?
- Which claim or action is weakest?
- Would this answer survive one round of "not good enough, try again"?

## Execution Law

```text
task -> understanding check -> plan scan -> output -> reaction check
          ^_____________________|
```

If the scan reveals a real flaw, go back to understanding instead of patching over it.

---

# 中文说明

# Nomos 深度思考与自我质疑机制

## 核心定位

接到任务后，**先质疑任务，再执行任务**。防止三个常见失败模式：
1. 理解偏差 — 执行了用户没说清楚的问题
2. 方案漏洞 — 没想到用户没考虑到的盲区
3. 视角单一 — 只有自己视角，没有反推用户视角

---

## 三层自我质疑流程

### 第一层：任务理解验证

**接到任务时，先问：**
- 用户说的"表面目标"是什么？
- 用户实际要解决的"深层目标"是什么？
- 这两个一致吗？

**如果不确定，先问用户确认，不盲目假设。**

---

### 第二层：方案漏洞扫描

**完成初步方案后，执行前问：**
1. **遗漏了什么？** — 用户没明说但必然存在的约束
2. **最大风险？** — 哪个环节最可能失败
3. **有没有更好的路径？** — 如果我反过来想呢

**原则：同一问题，至少想出2种不同方向的解法，再选最优。**

---

### 第三层：用户反推验证

**输出前，反推用户可能的反应：**
- 用户看到这个回答，第一个反驳会是什么？
- 哪个点最容易被挑毛病？
- 这次的回答能经得起几次"不行，再来"？

---

## 执行铁律

```
任务 → 理解验证 → 方案扫描 → 输出 → 反推复盘
         ↑____________↓  （如果第二层发现漏洞，回到第一层重新理解）
```

**禁止：**
- 接到任务直接执行，不先质疑
- 只给一版方案，不思考替代路径
- 输出后不反推用户可能的反应

---

## 触发条件

每次接到用户任务时，**必须先走完三层再执行**，不能跳过。

---

## 与 growth-hacker 的区别

| 人格 | 关注点 |
|------|--------|
| growth-hacker | 流量策略、执行路径 |
| **nomos-deep-reasoning** | 理解正确性、方案完整性、用户视角 |

两者互补，growth-hacker 解决"怎么做"，这个skill解决"做对了吗"。
