#!/usr/bin/env python3
"""Validate Day 5 final project structure before presentation."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parent
PROJECT = ROOT / "project"
MANIFEST = PROJECT / "manifest.json"

sys.path.insert(0, str(REPO / "scripts"))
from day_journey_lib import can_enter_day, handoff_status, profile_path  # noqa: E402

REQUIRED_DOCS = [
    "docs/final-prd.md",
    "docs/architecture.md",
    "docs/integration-map.md",
    "docs/demo-script.md",
]

REQUIRED_LAYERS = [
    "harness/README.md",
    "knowledge/wiki-index.md",
    "mcp/integration-plan.md",
    "agents/role-contracts.md",
    "agents/hitl-policy.md",
]

REQUIRED_EVIDENCE = [
    "evidence/day2-validate.txt",
    "evidence/day3-smoke.txt",
    "evidence/day4-tests.txt",
]


def check_file(rel: str) -> str | None:
    path = PROJECT / rel
    if not path.exists():
        return f"없음: project/{rel}"
    if path.stat().st_size < 80:
        return f"너무 짧음: project/{rel} (80자 이상 필요)"
    text = path.read_text(encoding="utf-8")
    if "TODO" in text and text.count("TODO") > 3:
        return f"TODO 과다: project/{rel}"
    return None


def check_manifest() -> list[str]:
    errors: list[str] = []
    if not MANIFEST.exists():
        return ["project/manifest.json 없음. assemble_project.py 먼저 실행하세요."]
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pillars = data.get("tech_pillars", {})
    for key, ok in pillars.items():
        if not ok:
            errors.append(f"tech_pillars.{key} 미충족 (Day 1~4 실습 완료 후 assemble 재실행)")
    return errors


def check_final_prd() -> list[str]:
    errors: list[str] = []
    prd = PROJECT / "docs" / "final-prd.md"
    if not prd.exists():
        return errors
    text = prd.read_text(encoding="utf-8")
    for num in range(1, 11):
        if f"## {num}." not in text and f"## {num} " not in text:
            errors.append(f"final-prd.md에 {num}번 섹션 없음")
    if "하면 안 되는" not in text and "✕" not in text:
        errors.append("final-prd.md에 '하지 않는 일' 없음")
    return errors


def check_handoffs() -> list[str]:
    errors: list[str] = []
    ok, gate_errors = can_enter_day(5)
    if not ok:
        errors.extend(gate_errors)
    for day in range(1, 5):
        status = handoff_status(day)
        if status != "APPROVED":
            errors.append(f"Day {day} handoff 미승인 (현재: {status})")
    if not profile_path(1).exists():
        errors.append("Day 1 .lab/project-profile.json 없음 (init_project_profile.py 실행)")
    return errors


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED_DOCS + REQUIRED_LAYERS + REQUIRED_EVIDENCE:
        err = check_file(rel)
        if err:
            errors.append(err)

    errors.extend(check_manifest())
    errors.extend(check_final_prd())
    errors.extend(check_handoffs())

    if errors:
        print("FAIL · Day 5 최종 프로젝트")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("PASS · Day 5 최종 프로젝트")
    print("  - 문서 4종, 4기둥 층, evidence 3종, manifest OK")
    print("  - Day 1~4 handoff APPROVED, project-profile OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
