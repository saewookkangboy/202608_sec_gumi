#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/eco_documents.jsonl"
OUT = ROOT / "knowledge/eco"
CATALOG = ROOT / "knowledge/catalog.json"
HASH_FILE = ROOT / "knowledge/raw.sha256"


def load_records():
    return [json.loads(line) for line in RAW.read_text(encoding="utf-8").splitlines() if line.strip()]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    records = load_records()
    catalog = []
    for row in records:
        source_id = row["source_id"]
        source_path = "data/raw/eco_documents.jsonl"
        text = "\n".join([
            f"# {source_id} · {row['part_name']}",
            "",
            f"- source_id: {source_id}",
            f"- source_path: {source_path}",
            f"- date: {row.get('date', 'UNKNOWN')}",
            f"- part_id: {row.get('part_id', 'UNKNOWN')}",
            f"- reason: {row.get('reason', 'UNKNOWN')}",
            f"- impact: {row.get('impact', 'UNKNOWN')}",
            f"- drawing: {row.get('drawing', 'UNKNOWN')}",
            f"- equipment: {row.get('equipment', 'UNKNOWN')}",
            "",
        ])
        (OUT / f"{source_id}.md").write_text(text, encoding="utf-8")
        catalog.append({**row, "source_path": source_path, "knowledge_path": f"knowledge/eco/{source_id}.md"})
    CATALOG.parent.mkdir(parents=True, exist_ok=True)
    CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    HASH_FILE.write_text(hashlib.sha256(RAW.read_bytes()).hexdigest() + "\n", encoding="utf-8")
    print(f"created={len(records)} catalog={CATALOG.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

