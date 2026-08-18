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

기술 배경(`AGENTS.md` 하네스, 원본 경계, 상태 파일)은 [skill·기술 참고 자료](../../../docs/skill-and-tech-reference.md)를 참고한다.

