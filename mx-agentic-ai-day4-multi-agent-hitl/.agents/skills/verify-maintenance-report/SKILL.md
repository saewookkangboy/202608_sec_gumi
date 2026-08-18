---
name: verify-maintenance-report
description: Independently judge maintenance-analysis evidence for missing sources, join errors, and calculation mismatches, returning PASS, REJECT, or ESCALATE without editing results.
---

# Verify Maintenance Report

Check source evidence, equipment join keys, and defect-rate calculations.

Return `PASS`, `REJECT` with concrete reasons, or `ESCALATE` after the retry limit. Never repair the executor output directly.

