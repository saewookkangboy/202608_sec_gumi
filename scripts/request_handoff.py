#!/usr/bin/env python3
"""Create a PENDING handoff packet after automated validation passes."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from day_journey_lib import (
    REPO_ROOT,
    build_handoff_request,
    ensure_lab_dir,
    handoff_path,
    load_handoff,
    run_day_validate,
    save_json,
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run day validation and create a PENDING handoff approval packet."
    )
    parser.add_argument("--day", type=int, choices=[1, 2, 3, 4, 5], required=True)
    parser.add_argument(
        "--requested-by",
        default="trainee",
        help="승인 요청자 (기본: trainee)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="기존 APPROVED 패킷을 PENDING으로 덮어씁니다 (재실습 시).",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    day = args.day

    existing = load_handoff(day)
    if existing and str(existing.get("status", "")).upper() == "APPROVED" and not args.force:
        print(f"FAIL · Day {day} 는 이미 APPROVED 입니다.")
        print("  - 재요청하려면 --force 를 사용하세요.")
        return 1

    print(f"Running Day {day} validation...")
    result = run_day_validate(day)
    if not result.ok:
        print(f"FAIL · Day {day} 자동 검증")
        print(result.log)
        return 1

    ensure_lab_dir(day)
    packet = build_handoff_request(day, requested_by=args.requested_by, validate=result)
    out = handoff_path(day)
    try:
        rel = out.relative_to(REPO_ROOT)
    except ValueError:
        rel = out
    save_json(out, packet)

    print(f"PASS · Day {day} 자동 검증")
    print(f"Wrote {rel}")
    print(f"Status: PENDING (사람 승인 필요)")
    print()
    print("다음 단계 (강사 또는 팀 승인자):")
    print(
        f"  python3 scripts/approve_handoff.py --day {day} "
        f"--reviewer \"이름\" --role instructor"
    )
    if day < 5:
        print(f"  python3 scripts/check_day_gate.py --enter-day {day + 1}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
