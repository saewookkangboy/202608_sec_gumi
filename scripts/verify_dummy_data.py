#!/usr/bin/env python3
"""Verify Day 2~4 synthetic dummy data is present after git clone."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    (
        "day2-raw",
        ROOT / "mx-agentic-ai-day2-knowledge-harness/data/raw/eco_documents.jsonl",
        "jsonl",
        12,
    ),
    (
        "day2-eval",
        ROOT / "mx-agentic-ai-day2-knowledge-harness/eval/questions.jsonl",
        "jsonl",
        1,
    ),
    (
        "day3-csv",
        ROOT / "mx-agentic-ai-day3-mcp-tools/data/equipment_logs.csv",
        "csv",
        10,
    ),
    (
        "day4-quality",
        ROOT / "mx-agentic-ai-day4-multi-agent-hitl/fixtures/quality_summary.json",
        "json-list",
        1,
    ),
    (
        "day4-errors",
        ROOT / "mx-agentic-ai-day4-multi-agent-hitl/fixtures/equipment_errors.json",
        "json-list",
        1,
    ),
]


def count_rows(path: Path, kind: str) -> int:
    text = path.read_text(encoding="utf-8")
    if kind == "jsonl":
        return sum(1 for line in text.splitlines() if line.strip())
    if kind == "csv":
        with path.open(encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh))
        return len(rows)
    if kind == "json-list":
        data = json.loads(text)
        if not isinstance(data, list):
            raise ValueError(f"{path}: expected JSON array")
        return len(data)
    raise ValueError(kind)


def main() -> int:
    errors: list[str] = []
    for label, path, kind, min_rows in REQUIRED:
        rel = path.relative_to(ROOT)
        if not path.is_file():
            errors.append(f"MISSING {label}: {rel}")
            continue
        try:
            n = count_rows(path, kind)
        except (OSError, ValueError, json.JSONDecodeError, csv.Error) as exc:
            errors.append(f"INVALID {label}: {rel} ({exc})")
            continue
        if n < min_rows:
            errors.append(f"TOO_FEW {label}: {rel} has {n} rows, need >= {min_rows}")
            continue
        print(f"OK  {label}: {rel} ({n} rows)")

    if errors:
        print("FAIL: dummy data incomplete", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        print("See docs/dummy-data.md", file=sys.stderr)
        return 1

    print("PASS: Day 2~4 dummy data ready for GitHub clone labs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
