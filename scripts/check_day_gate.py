#!/usr/bin/env python3
"""Check whether the trainee may enter a given day (requires previous-day human approval)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from day_journey_lib import can_enter_day, day_dir, journey_summary, run_day_validate


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check inter-day human approval gate before starting a day."
    )
    parser.add_argument(
        "--enter-day",
        type=int,
        choices=[1, 2, 3, 4, 5],
        help="진입하려는 일차 (1~5)",
    )
    parser.add_argument(
        "--recheck-previous",
        action="store_true",
        help="이전 일차 검증을 다시 실행합니다.",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Day 1~5 승인 게이트 현황을 출력합니다.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if args.status:
        print("Day | 진입 가능 | 승인 상태 | 경로")
        print("---:|---|---|---")
        for row in journey_summary():
            enter = "YES" if row["can_enter"] else "NO"
            print(
                f"{row['day']} | {enter} | {row['handoff_status']} | {row['path']}"
            )
        return 0

    if args.enter_day is None:
        print("FAIL · --enter-day 또는 --status 가 필요합니다.", file=sys.stderr)
        return 1

    day = args.enter_day
    ok, errors = can_enter_day(day, recheck_previous=args.recheck_previous)
    if not ok:
        print(f"FAIL · Day {day} 진입 불가")
        for err in errors:
            print(f"  - {err}")
        print()
        print("다음 단계:")
        if day > 1:
            prev = day - 1
            print(f"  1) cd {day_dir(prev).relative_to(day_dir(1).parents[1])}")
            print(f"  2) python3 ../scripts/request_handoff.py --day {prev}")
            print(
                f"  3) python3 ../scripts/approve_handoff.py --day {prev} "
                f"--reviewer \"이름\" --role instructor"
            )
        return 1

    print(f"PASS · Day {day} 진입 가능")
    if day == 1:
        print("  - Day 1은 선행 승인이 필요 없습니다.")
        print("  - PRD 작성 후: python3 scripts/init_project_profile.py")
    else:
        print(f"  - Day {day - 1} 사람 승인(APPROVED) 확인됨")
        if args.recheck_previous:
            result = run_day_validate(day - 1)
            if result.ok:
                print(f"  - Day {day - 1} 재검증 PASS")
            else:
                print(f"  - Day {day - 1} 재검증 FAIL (주의)")
    print(f"  - 작업 폴더: {day_dir(day)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
