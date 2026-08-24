#!/usr/bin/env python3
"""[선택] Day 5 구조 검증 — 교육생 기본 경로는 README 예제 2)·9) 점검 프롬프트입니다."""

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

# assemble가 복사·생성하는 레이어 (디렉터리 존재)
REQUIRED_DIRS = [
    "knowledge",
    "mcp",
    "agents",
    "docs",
    "evidence",
]

# 둘 중 하나면 evidence 충족 (참조 트랙 요약 또는 PRD 연속형 데모)
EVIDENCE_ANY = [
    ["evidence/demo-data.json"],
    ["evidence/day2-validate.txt", "evidence/day3-smoke.txt", "evidence/day4-tests.txt"],
]


def check_file(rel: str, min_size: int = 40) -> str | None:
    path = PROJECT / rel
    if not path.exists():
        return f"없음: project/{rel}"
    if path.stat().st_size < min_size:
        return f"너무 짧음: project/{rel} ({min_size}자 이상 필요)"
    return None


def check_manifest() -> list[str]:
    errors: list[str] = []
    if not MANIFEST.exists():
        return ["project/manifest.json 없음. assemble_project.py 먼저 실행하세요."]
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    overall = data.get("overall_status")
    if overall == "READY":
        return errors
    if overall == "NOT_READY":
        for layer in data.get("layers") or []:
            if layer.get("status") != "PASS":
                errors.append(
                    f"레이어 미충족: {layer.get('label')} "
                    f"({layer.get('count')}/{layer.get('required')})"
                )
        if not errors:
            errors.append("manifest overall_status=NOT_READY")
        return errors

    # 레거시 manifest (tech_pillars)
    pillars = data.get("tech_pillars") or {}
    for key, ok in pillars.items():
        if not ok:
            errors.append(f"tech_pillars.{key} 미충족 (assemble 재실행)")
    if not pillars and not overall:
        errors.append("manifest 형식을 알 수 없음. assemble_project.py를 다시 실행하세요.")
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
    if "하면 안 되는" not in text and "✕" not in text and "금지" not in text:
        errors.append("final-prd.md에 '하지 않는 일/금지' 표현 없음")
    return errors


def check_evidence() -> list[str]:
    for group in EVIDENCE_ANY:
        if all((PROJECT / rel).exists() for rel in group):
            return []
    return [
        "evidence 부족: demo-data.json 또는 day2/3/4 검증 요약 파일이 필요합니다."
    ]


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

    if not PROJECT.exists():
        print("FAIL: project/ 없음. python3 scripts/assemble_project.py 먼저 실행하세요.")
        return 1

    for dirname in REQUIRED_DIRS:
        if not (PROJECT / dirname).is_dir():
            errors.append(f"없음: project/{dirname}/")

    for rel in REQUIRED_DOCS:
        err = check_file(rel)
        if err:
            errors.append(err)

    errors.extend(check_manifest())
    errors.extend(check_final_prd())
    errors.extend(check_evidence())
    errors.extend(check_handoffs())

    if errors:
        print("Day 5 검증 FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("Day 5 검증 PASS")
    print("  - project/ 4층 + docs + evidence + manifest READY")
    print("  - 사람 승인·발표는 validate PASS와 별개입니다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
