---
name: verify-maintenance-report
description: Independently judge maintenance-analysis evidence for missing sources, join errors, and calculation mismatches, returning PASS, REJECT, or ESCALATE without editing results.
---

# Verify Maintenance Report

Check source evidence, equipment join keys, and defect-rate calculations.

Return `PASS`, `REJECT` with concrete reasons, or `ESCALATE` after the retry limit. Never repair the executor output directly.

기술 배경(독립 검증, 재시도·이관)은 [skill·기술 참고 자료](../../../docs/skill-and-tech-reference.md)를 참고한다.

