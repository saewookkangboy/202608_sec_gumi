import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from search_knowledge import search


class Day2LabTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable, str(ROOT / "scripts/normalize_docs.py")], check=True)

    def test_twelve_documents_are_created(self):
        self.assertEqual(len(list((ROOT / "knowledge/eco").glob("ECO-*.md"))), 12)

    def test_search_returns_expected_document(self):
        ids = [row["source_id"] for row in search("P-100 후면 하우징", 3)]
        self.assertIn("ECO-001", ids)
        self.assertIn("ECO-003", ids)

    def test_catalog_is_traceable(self):
        rows = json.loads((ROOT / "knowledge/catalog.json").read_text(encoding="utf-8"))
        self.assertTrue(all(row["source_path"] == "data/raw/eco_documents.jsonl" for row in rows))

    def test_static_graphrag_files_are_parseable_and_traceable(self):
        subprocess.run([sys.executable, str(ROOT / "scripts/build_static_graphrag.py")], check=True)
        graph_dir = ROOT / "knowledge/graphrag"
        parsed = {}
        for name in ("documents.jsonl", "chunks.jsonl", "entities.jsonl", "relationships.jsonl"):
            rows = [json.loads(line) for line in (graph_dir / name).read_text(encoding="utf-8").splitlines()]
            self.assertTrue(rows, f"{name} should not be empty")
            parsed[name] = rows

        relationships = parsed["relationships.jsonl"]
        self.assertTrue(
            all(row.get(key) for row in relationships for key in ("source_id", "source_path", "chunk_id", "evidence"))
        )
        entity_ids = {row["entity_id"] for row in parsed["entities.jsonl"]}
        chunk_ids = {row["chunk_id"] for row in parsed["chunks.jsonl"]}
        document_ids = {row["document_id"] for row in parsed["documents.jsonl"]}
        self.assertTrue(all(set(row["entity_ids"]) <= entity_ids for row in parsed["chunks.jsonl"]))
        self.assertTrue(all(row["document_id"] in document_ids for row in parsed["chunks.jsonl"]))
        self.assertTrue(
            all(
                row["source_entity_id"] in entity_ids
                and row["target_entity_id"] in entity_ids
                and row["chunk_id"] in chunk_ids
                for row in relationships
            )
        )

        metadata = json.loads((graph_dir / "metadata.json").read_text(encoding="utf-8"))
        self.assertEqual(
            metadata["counts"],
            {"documents": 12, "chunks": 12, "entities": 64, "relationships": 58},
        )

    def test_unknown_values_are_not_promoted_to_graph_entities(self):
        graph_dir = ROOT / "knowledge/graphrag"
        entities = [json.loads(line) for line in (graph_dir / "entities.jsonl").read_text(encoding="utf-8").splitlines()]
        metadata = json.loads((graph_dir / "metadata.json").read_text(encoding="utf-8"))
        self.assertNotIn("UNKNOWN", {row["name"] for row in entities})
        self.assertEqual(len(metadata["unknown_values"]), 2)


if __name__ == "__main__":
    unittest.main()
