---
name: eco-knowledge-builder
description: Convert the repository's synthetic ECO records into traceable Markdown knowledge assets and verify retrieval evidence without modifying raw inputs.
---

# ECO Knowledge Builder

Use this skill when the user asks to normalize, index, search, or evaluate the ECO training data in this repository.

## Workflow

1. Read `AGENTS.md` and confirm that `data/raw/` is immutable.
2. Run `python3 scripts/normalize_docs.py`.
3. Inspect `knowledge/catalog.json` and at least two generated Markdown files.
4. Answer knowledge questions with document IDs and `source_path`; do not invent missing values.
5. Run `python3 scripts/validate_repo.py` and the unit tests before completion.

For Advanced work, add relation edges without changing the normalized source contract.

