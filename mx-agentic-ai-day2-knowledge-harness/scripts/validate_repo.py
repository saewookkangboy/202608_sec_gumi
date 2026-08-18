#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/eco_documents.jsonl"


def main():
    errors = []
    catalog_path = ROOT / "knowledge/catalog.json"
    if not catalog_path.exists():
        errors.append("knowledge/catalog.json missing")
        rows = []
    else:
        rows = json.loads(catalog_path.read_text(encoding="utf-8"))
    if len(rows) != 12:
        errors.append(f"expected 12 records, got {len(rows)}")
    for row in rows:
        for key in ("source_id", "source_path", "knowledge_path"):
            if not row.get(key):
                errors.append(f"{row.get('source_id', '?')}: missing {key}")
        if not (ROOT / row.get("knowledge_path", "missing")).exists():
            errors.append(f"{row.get('source_id', '?')}: knowledge file missing")
    hash_path = ROOT / "knowledge/raw.sha256"
    if hash_path.exists() and hash_path.read_text().strip() != hashlib.sha256(RAW.read_bytes()).hexdigest():
        errors.append("raw source hash changed")
    for name in ("plan.md", "progress.md", "decisions.md"):
        if len((ROOT / name).read_text(encoding="utf-8").strip()) < 10:
            errors.append(f"{name} is empty")
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("PASS: 12 records, traceable sources, immutable raw data, state files ready")


if __name__ == "__main__":
    main()

