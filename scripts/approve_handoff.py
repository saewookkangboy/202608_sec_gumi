#!/usr/bin/env python3
"""Record explicit human approval for a completed day (required before next day)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from day_journey_lib import approve_handoff, handoff_path, load_handoff


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Record human approval for a day handoff packet."
    )
    parser.add_argument("--day", type=int, choices=[1, 2, 3, 4, 5], required=True)
    parser.add_argument("--reviewer", required=True, help="승인자 이름 (합성/가명만)")
    parser.add_argument(
        "--role",
        choices=["instructor", "mentor", "team_lead", "trainee_lead"],
        default="instructor",
        help="승인자 역할",
    )
    parser.add_argument("--notes", default="", help="승인 메모 (선택)")
    parser.add_argument(
        "--reject",
        action="store_true",
        help="반려(REJECTED)로 기록합니다.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    day = args.day
    path = handoff_path(day)

    if not path.exists():
        print(f"FAIL · {path} 없음. request_handoff.py --day {day} 먼저 실행하세요.")
        return 1

    if args.reject:
        data = load_handoff(day)
        if data is None:
            return 1
        data["status"] = "REJECTED"
        data["approval"] = {
            "status": "REJECTED",
            "reviewer": args.reviewer,
            "reviewer_role": args.role,
            "notes": args.notes or "재실습 필요",
        }
        path.write_text(
            __import__("json").dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"REJECTED · Day {day} (reviewer={args.reviewer})")
        return 0

    try:
        data = approve_handoff(
            day,
            reviewer=args.reviewer,
            reviewer_role=args.role,
            notes=args.notes,
        )
    except (FileNotFoundError, ValueError) as exc:
        print(f"FAIL · {exc}")
        return 1

    print(f"APPROVED · Day {day}")
    print(f"  - reviewer: {args.reviewer} ({args.role})")
    print(f"  - project: {data.get('project_title', 'UNKNOWN')}")
    if day < 5:
        print(f"  - 다음: python3 scripts/check_day_gate.py --enter-day {day + 1}")
    else:
        print("  - Day 5 발표 준비 완료")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
