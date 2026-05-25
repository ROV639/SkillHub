#!/usr/bin/env python3
"""Classify SkillHub inventory into source classes, risk levels, and actions."""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
INVENTORY = REPO / "registry/skills_inventory.json"
OUT = REPO / "registry/skills_classification.json"
REPORT = REPO / "reports/06_REPORT_skillhub_自动分类结果_v1.md"

R4 = re.compile(r"(?i)(publish|post|upload|comment|reply|delete|remove|dm|message|互动|发布|上传|评论|私信|删除)")
R3 = re.compile(r"(?i)(cookie|session|login|auth|browser|chrome|wechat|xhs|xiaohongshu|账号|登录|会话|浏览器)")
R2 = re.compile(r"(?i)(api|key|download|generate|image|tts|openai|minimax|gemini|下载|生图|接口)")
R1 = re.compile(r"(?i)(url|markdown|readme|transcript|diagram|svg|file|网页|文档|字幕|图解)")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def risk_for_text(text: str, hint: str = "") -> str:
    normalized_hint = hint.lower().strip()
    if normalized_hint == "low":
        return "R0"
    if normalized_hint == "mixed":
        return "R2"
    if normalized_hint in {"medium", "med"}:
        return "R2"
    if normalized_hint == "high":
        return "R3"
    blob = f"{text} {hint}"
    if R4.search(blob):
        return "R4"
    if R3.search(blob):
        return "R3"
    if R2.search(blob):
        return "R2"
    if R1.search(blob):
        return "R1"
    return "R0"


def action_for(item: dict, risk: str) -> str:
    status = item.get("status", "")
    kind = item.get("kind", "")
    rec = item.get("recommended_action")
    if rec:
        return rec
    if status == "BLOCKED_PROD" or risk == "R4":
        return "BLOCK-PROD"
    if kind == "local-skill" and item.get("source_type") == "rubin-original":
        return "LAB-TEST"
    if risk in {"R0", "R1", "R2"}:
        return "SANDBOX"
    if risk == "R3":
        return "GATE"
    return "REFERENCE"


def classify_inventory(data: dict) -> list[dict]:
    rows = []
    for item in data.get("local_skills", []):
        text = " ".join(str(item.get(k, "")) for k in ["id", "display_name", "summary", "path"])
        risk = item.get("risk_level") or risk_for_text(text)
        rows.append({**item, "computed_risk": risk, "recommended_action": action_for(item, risk)})
    for item in data.get("sources", []):
        text = " ".join(str(item.get(k, "")) for k in ["name", "type", "notes", "url"])
        risk = item.get("risk_hint") if str(item.get("risk_hint", "")).startswith("R") else risk_for_text(text, item.get("risk_hint", ""))
        rows.append({**item, "kind": "external-source", "computed_risk": risk, "recommended_action": action_for(item, risk)})
    return rows


def table(rows: list[list[str]]) -> str:
    if not rows:
        return "- 无\n"
    lines = [
        "| " + " | ".join(rows[0]) + " |",
        "| " + " | ".join(["---"] * len(rows[0])) + " |",
    ]
    for row in rows[1:]:
        lines.append("| " + " | ".join(str(x).replace("\n", " ") for x in row) + " |")
    return "\n".join(lines) + "\n"


def build_report(rows: list[dict]) -> str:
    counts = Counter(r["computed_risk"] for r in rows)
    action_counts = Counter(r["recommended_action"] for r in rows)
    lines = [
        "# SkillHub 自动分类结果 v1",
        "",
        f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 总览",
        "",
        table([["风险", "数量"]] + [[k, str(v)] for k, v in sorted(counts.items())]),
        table([["建议动作", "数量"]] + [[k, str(v)] for k, v in sorted(action_counts.items())]),
        "## 分类结果",
        "",
    ]
    lines.append(
        table(
            [["名称", "类型", "风险", "建议动作", "备注"]]
            + [
                [
                    r.get("display_name") or r.get("name") or r.get("id", ""),
                    r.get("kind") or r.get("type", ""),
                    r.get("computed_risk", ""),
                    r.get("recommended_action", ""),
                    r.get("notes") or r.get("summary", ""),
                ]
                for r in rows
            ]
        )
    )
    lines += [
        "## MiniMax agent 可接任务",
        "",
        "- 为 `SANDBOX` 和 `REFERENCE` 项生成使用卡初稿。",
        "- 为 `BLOCK-PROD` 项整理字段和限制，不做运行。",
        "- 为 R0-R2 项提取依赖、输入、输出、失败点。",
        "",
        "## Codex / Robin 保留判断",
        "",
        "- 是否晋升 READY。",
        "- 是否接账号、API key、cookie、登录态。",
        "- 是否执行外部脚本或真实发布。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    data = load(INVENTORY)
    rows = classify_inventory(data)
    result = {
        "schema_version": "0.1.0",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": rows,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(build_report(rows), encoding="utf-8")
    print(OUT)
    print(REPORT)


if __name__ == "__main__":
    main()
