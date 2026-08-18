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


if __name__ == "__main__":
    unittest.main()

