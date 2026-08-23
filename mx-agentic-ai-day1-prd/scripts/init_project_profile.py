#!/usr/bin/env python3
"""Initialize trainee project profile from Day 1 PRD."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAB = ROOT / ".lab"
PROFILE = LAB / "project-profile.json"
PRD = ROOT / "docs" / "prd.md"
REFERENCE_PRD = ROOT.parent / "docs" / "reference-prd.md"


def _extract_title(text: str) -> str:
    match = re.search(r"^#\s*AI PRD[·\s]+(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else "UNKNOWN"


def _extract_mvp(text: str) -> str:
    match = re.search(r"\*\*MVP 한 문장:\*\*\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else "UNKNOWN"


def build_profile() -> dict:
    if not PRD.exists():
        raise FileNotFoundError("docs/prd.md 가 없습니다. Day 1 PRD를 먼저 작성하세요.")

    text = PRD.read_text(encoding="utf-8")
    now = datetime.now(timezone.utc).isoformat()

    return {
        "schema_version": 1,
        "project_title": _extract_title(text),
        "agent_name": _extract_title(text),
        "prd_path": "docs/prd.md",
        "mvp_sentence": _extract_mvp(text),
        "reference_prd_path": "../../docs/reference-prd.md",
        "canvas_focus": {
            "day2": "section_8_eval_harness",
            "day3": "sections_5_6_mcp_tools",
            "day4": "sections_9_10_hitl_governance",
            "day5": "sections_8_9_10_complete",
        },
        "mapping_notes": (
            "Day 2~4 참조 실습은 docs/reference-prd.md 의 ECO·설비·품질 시나리오로 "
            "4대 기술 기둥을 익힙니다. 본 프로필의 PRD는 Day 5 final-prd.md 에 통합합니다."
        ),
        "initialized_at": now,
        "updated_at": now,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Create .lab/project-profile.json from docs/prd.md")
    parser.add_argument("--force", action="store_true", help="기존 프로필 덮어쓰기")
    args = parser.parse_args()

    if PROFILE.exists() and not args.force:
        print(f"FAIL · {PROFILE} 이미 존재합니다. --force 로 덮어쓰세요.")
        return 1

    try:
        profile = build_profile()
    except FileNotFoundError as exc:
        print(f"FAIL · {exc}")
        return 1

    LAB.mkdir(parents=True, exist_ok=True)
    PROFILE.write_text(json.dumps(profile, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("OK · project-profile.json 생성")
    print(f"  - project_title: {profile['project_title']}")
    print(f"  - mvp: {profile['mvp_sentence']}")
    print()
    print("다음:")
    print("  python3 scripts/validate_day1.py")
    print("  python3 ../scripts/request_handoff.py --day 1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
