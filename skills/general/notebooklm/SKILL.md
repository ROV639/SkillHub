---
name: notebooklm
version: 1.0.0
author: Roven
source: locally-developed
platform: universal
description: Use NotebookLM as a source-grounded research workflow for URLs, PDFs, YouTube videos, notes, and reports.
updated: 2026-05-31
---

# NotebookLM Research Workflow

Use this skill when a task needs source-based research using NotebookLM: YouTube videos, PDFs, URLs, pasted text, notes, Q&A, reports, quizzes, slide outlines, mind maps, or briefing documents.

## Authentication

Run the NotebookLM CLI login before first use:

```bash
nlm login
```

Credentials are stored by the CLI. Do not copy them into SkillHub, reports, or public logs.

## Practical CLI Notes

The local workflow uses the `nlm` CLI directly. Tool names in older notes may be conceptual; prefer actual CLI commands.

Examples:

```bash
nlm notebook list
nlm source add <notebook-id> --url <url> --wait
nlm query notebook <notebook-id> "What are the main claims?"
```

## Workflow

1. Create or select a notebook.
2. Add sources with URLs, PDFs, YouTube links, or text.
3. Wait for source processing to finish.
4. Ask source-grounded questions.
5. Export a report, briefing, outline, or Q&A.
6. Record source gaps and uncertain claims.

## Source Hygiene

- Keep each source URL visible in the final notes.
- Separate what the source says from your inference.
- Mark unavailable, region-locked, or failed sources.
- Do not pretend NotebookLM read a source when ingestion failed.

## Output Template

```text
NotebookLM Research Brief
Topic:
Notebook:
Sources added:
Failed sources:
Key claims:
Useful quotes or evidence notes:
Open questions:
Next action:
```
