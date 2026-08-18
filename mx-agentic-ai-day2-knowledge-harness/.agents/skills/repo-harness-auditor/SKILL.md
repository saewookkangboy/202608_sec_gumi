---
name: repo-harness-auditor
description: Audit this training repository's AGENTS.md, immutable input boundary, state files, and completion checks before declaring an agent task finished.
---

# Repository Harness Auditor

Use this skill to verify that the repository harness actually constrains work.

## Checks

- `AGENTS.md` protects `data/raw/` and names allowed output locations.
- `plan.md`, `progress.md`, and `decisions.md` contain usable state.
- Generated knowledge records retain `source_id` and `source_path`.
- The raw data SHA-256 still matches `knowledge/raw.sha256`.
- `python3 scripts/validate_repo.py` and all tests pass.

Report failures with the exact file and corrective action. Do not silently repair raw data.

