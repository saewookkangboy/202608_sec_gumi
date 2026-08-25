#!/usr/bin/env python3
"""Build a dependency-free static GraphRAG demo from the synthetic ECO source."""

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/eco_documents.jsonl"
OUT = ROOT / "knowledge/graphrag"


def write_jsonl(path, rows):
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows),
        encoding="utf-8",
    )


def main():
    source_rows = [json.loads(line) for line in RAW.read_text(encoding="utf-8").splitlines() if line.strip()]
    documents = []
    chunks = []
    entities_by_id = {}
    entity_sources = defaultdict(set)
    entity_chunks = defaultdict(set)
    relationships = []
    unknown_values = []

    def add_entity(entity_id, entity_type, name, description, source_id, chunk_id):
        entities_by_id.setdefault(
            entity_id,
            {
                "entity_id": entity_id,
                "type": entity_type,
                "name": name,
                "description": description,
            },
        )
        entity_sources[entity_id].add(source_id)
        entity_chunks[entity_id].add(chunk_id)

    def add_relationship(source_id, target_id, relation_type, row, chunk_id, evidence):
        relationships.append(
            {
                "relationship_id": f"rel:{row['source_id']}:{relation_type.lower()}",
                "source_entity_id": source_id,
                "target_entity_id": target_id,
                "type": relation_type,
                "source_id": row["source_id"],
                "source_path": "data/raw/eco_documents.jsonl",
                "chunk_id": chunk_id,
                "evidence": evidence,
            }
        )

    for row in source_rows:
        source_id = row["source_id"]
        document_id = f"doc:{source_id}"
        chunk_id = f"chunk:{source_id}:000"
        eco_entity_id = f"eco:{source_id}"
        part_entity_id = f"part:{row['part_id']}"
        reason_entity_id = f"reason:{source_id}"
        impact_entity_id = f"impact:{source_id}"

        sentence = (
            f"{source_id}는 {row['date']}에 {row['part_id']} {row['part_name']}의 "
            f"'{row['reason']}'을 위해 '{row['impact']}'을 기록했다. "
            f"도면은 {row['drawing']}, 설비는 {row['equipment']}이다."
        )
        documents.append(
            {
                "document_id": document_id,
                "source_id": source_id,
                "title": f"{source_id} · {row['part_name']}",
                "source_path": "data/raw/eco_documents.jsonl",
                "knowledge_path": f"knowledge/eco/{source_id}.md",
                "date": row["date"],
                "text": sentence,
                "metadata": {
                    "part_id": row["part_id"],
                    "drawing": row["drawing"],
                    "equipment": row["equipment"],
                },
            }
        )

        entity_ids = [eco_entity_id, part_entity_id, reason_entity_id, impact_entity_id]
        add_entity(eco_entity_id, "ECO_CHANGE", source_id, f"{row['part_name']} 변경 기록", source_id, chunk_id)
        add_entity(part_entity_id, "PART", row["part_name"], row["part_id"], source_id, chunk_id)
        add_entity(reason_entity_id, "CHANGE_REASON", row["reason"], f"{source_id} 변경 사유", source_id, chunk_id)
        add_entity(impact_entity_id, "CHANGE_IMPACT", row["impact"], f"{source_id} 변경 영향", source_id, chunk_id)

        add_relationship(eco_entity_id, part_entity_id, "AFFECTS", row, chunk_id, f"{source_id} 대상 부품: {row['part_id']} {row['part_name']}")
        add_relationship(reason_entity_id, eco_entity_id, "TRIGGERS", row, chunk_id, f"변경 사유: {row['reason']}")
        add_relationship(eco_entity_id, impact_entity_id, "RESULTS_IN", row, chunk_id, f"변경 영향: {row['impact']}")

        for field, entity_type, prefix, relation_type in (
            ("drawing", "DRAWING", "drawing", "DOCUMENTED_IN"),
            ("equipment", "EQUIPMENT", "equipment", "USES_EQUIPMENT"),
        ):
            value = row[field]
            if value == "UNKNOWN":
                unknown_values.append({"source_id": source_id, "field": field, "value": value})
                continue
            entity_id = f"{prefix}:{value}"
            entity_ids.append(entity_id)
            add_entity(entity_id, entity_type, value, f"{source_id}에 근거한 {field}", source_id, chunk_id)
            add_relationship(eco_entity_id, entity_id, relation_type, row, chunk_id, f"{field}: {value}")

        chunks.append(
            {
                "chunk_id": chunk_id,
                "document_id": document_id,
                "source_id": source_id,
                "ordinal": 0,
                "text": sentence,
                "entity_ids": entity_ids,
                "metadata": {"date": row["date"], "source_path": "data/raw/eco_documents.jsonl"},
            }
        )

    entities = []
    for entity_id in sorted(entities_by_id):
        entity = entities_by_id[entity_id]
        entity["source_ids"] = sorted(entity_sources[entity_id])
        entity["chunk_ids"] = sorted(entity_chunks[entity_id])
        entities.append(entity)

    OUT.mkdir(parents=True, exist_ok=True)
    write_jsonl(OUT / "documents.jsonl", documents)
    write_jsonl(OUT / "chunks.jsonl", chunks)
    write_jsonl(OUT / "entities.jsonl", entities)
    write_jsonl(OUT / "relationships.jsonl", relationships)

    with (OUT / "entity_index.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["entity_id", "type", "name", "source_ids", "chunk_ids"])
        for entity in entities:
            writer.writerow(
                [
                    entity["entity_id"],
                    entity["type"],
                    entity["name"],
                    "|".join(entity["source_ids"]),
                    "|".join(entity["chunk_ids"]),
                ]
            )

    metadata = {
        "schema_version": "1.0",
        "dataset": "synthetic-eco-static-graphrag-demo",
        "generated_from": "data/raw/eco_documents.jsonl",
        "generator": "scripts/build_static_graphrag.py",
        "counts": {
            "documents": len(documents),
            "chunks": len(chunks),
            "entities": len(entities),
            "relationships": len(relationships),
        },
        "entity_types": dict(sorted(Counter(row["type"] for row in entities).items())),
        "relationship_types": dict(sorted(Counter(row["type"] for row in relationships).items())),
        "unknown_values": unknown_values,
        "notes": [
            "각 합성 ECO 문서는 학습용으로 한 개의 chunk를 사용한다.",
            "UNKNOWN 값은 추정하지 않으며 엔터티·관계에서 제외하고 unknown_values에 남긴다.",
            "모든 관계는 source_id, source_path, chunk_id, evidence로 원문까지 추적할 수 있다.",
        ],
    }
    (OUT / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"PASS: {len(documents)} documents, {len(chunks)} chunks, "
        f"{len(entities)} entities, {len(relationships)} relationships"
    )


if __name__ == "__main__":
    main()
