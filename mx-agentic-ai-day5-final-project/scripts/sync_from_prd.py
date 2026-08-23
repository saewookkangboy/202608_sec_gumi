#!/usr/bin/env python3
"""Seed Day 5 final-prd.md header from Day 1 trainee PRD and project profile."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parent
DAY1 = REPO / "mx-agentic-ai-day1-prd"
FINAL_PRD = ROOT / "project" / "docs" / "final-prd.md"
PROFILE = DAY1 / ".lab" / "project-profile.json"
DAY1_PRD = DAY1 / "docs" / "prd.md"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _title_from_prd(text: str) -> str:
    match = re.search(r"^#\s*AI PRD[·\s]+(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else "UNKNOWN"


def sync_header(*, force: bool = False) -> list[str]:
    changes: list[str] = []
    if not DAY1_PRD.exists():
        raise FileNotFoundError("Day 1 docs/prd.md 가 없습니다.")

    day1_text = _read(DAY1_PRD)
    title = _title_from_prd(day1_text)
    if PROFILE.exists():
        profile = json.loads(_read(PROFILE))
        title = profile.get("project_title", title)

    if not FINAL_PRD.exists():
        raise FileNotFoundError("project/docs/final-prd.md 가 없습니다.")

    final_text = _read(FINAL_PRD)
    new_header = f"# AI PRD · {title} (Day 5 완성본)"
    if final_text.startswith("# AI PRD"):
        final_text = re.sub(r"^# AI PRD.*$", new_header, final_text, count=1)
        changes.append("final-prd.md 제목")
    else:
        final_text = new_header + "\n\n" + final_text
        changes.append("final-prd.md 헤더 추가")

    stamp = (
        f"\n> Day 1 `mx-agentic-ai-day1-prd/docs/prd.md` 기반 · "
        f"동기화: {datetime.now(timezone.utc).date().isoformat()}\n"
    )
    if "Day 1 `mx-agentic-ai-day1-prd/docs/prd.md` 기반" not in final_text:
        final_text = final_text.replace(
            "> Day 1 `docs/prd.md`",
            "> Day 1 `mx-agentic-ai-day1-prd/docs/prd.md`",
            1,
        )
        if "> Day 1 `mx-agentic-ai-day1-prd/docs/prd.md`" not in final_text:
            final_text = new_header + stamp + final_text[len(new_header) :]

    if force or changes:
        FINAL_PRD.write_text(final_text, encoding="utf-8")

    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Day 5 final-prd title from Day 1 PRD.")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    try:
        changes = sync_header(force=True)
    except FileNotFoundError as exc:
        print(f"FAIL · {exc}")
        return 1

    if changes:
        print("OK · Day 5 final-prd 동기화")
        for item in changes:
            print(f"  - {item}")
    else:
        print("OK · 변경 없음")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
