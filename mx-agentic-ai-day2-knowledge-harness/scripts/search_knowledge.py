#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "knowledge/catalog.json"


def tokens(text):
    return set(re.findall(r"[A-Za-z0-9가-힣-]+", text.lower()))


def search(question, limit=3):
    rows = json.loads(CATALOG.read_text(encoding="utf-8"))
    q = tokens(question)
    scored = []
    for row in rows:
        hay = tokens(" ".join(str(v) for v in row.values()))
        score = len(q & hay)
        scored.append((score, row["source_id"], row))
    return [row for score, _, row in sorted(scored, key=lambda x: (-x[0], x[1]))[:limit] if score > 0]


def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: search_knowledge.py <question>")
    if not CATALOG.exists():
        raise SystemExit("run scripts/normalize_docs.py first")
    print(json.dumps(search(" ".join(sys.argv[1:])), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

