#!/usr/bin/env python3
"""Shared helpers for the 5-day trainee journey and inter-day handoff gates."""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1

REPO_ROOT = Path(__file__).resolve().parent.parent

DAY_DIRS: dict[int, Path] = {
    1: REPO_ROOT / "mx-agentic-ai-day1-prd",
    2: REPO_ROOT / "mx-agentic-ai-day2-knowledge-harness",
    3: REPO_ROOT / "mx-agentic-ai-day3-mcp-tools",
    4: REPO_ROOT / "mx-agentic-ai-day4-multi-agent-hitl",
    5: REPO_ROOT / "mx-agentic-ai-day5-final-project",
}

HANDOFF_FILENAME = "handoff-approval.json"
PROFILE_FILENAME = "project-profile.json"


@dataclass(frozen=True)
class ValidateResult:
    ok: bool
    commands: list[list[str]]
    exit_codes: list[int]
    log: str


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def day_dir(day: int) -> Path:
    if day not in DAY_DIRS:
        raise ValueError(f"invalid day: {day}")
    return DAY_DIRS[day]


def lab_dir(day: int) -> Path:
    return day_dir(day) / ".lab"


def handoff_path(day: int) -> Path:
    return lab_dir(day) / HANDOFF_FILENAME


def profile_path(day: int = 1) -> Path:
    return lab_dir(day) / PROFILE_FILENAME


def ensure_lab_dir(day: int) -> Path:
    path = lab_dir(day)
    path.mkdir(parents=True, exist_ok=True)
    return path


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _run(cmd: list[str], cwd: Path) -> tuple[int, str]:
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=180,
        )
        out = (result.stdout or "") + (result.stderr or "")
        return result.returncode, out.strip()
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 1, str(exc)


def run_day_validate(day: int) -> ValidateResult:
    cwd = day_dir(day)
    commands: list[list[str]] = []
    exit_codes: list[int] = []
    logs: list[str] = []

    if day == 1:
        commands.append(["python3", "scripts/validate_day1.py"])
    elif day == 2:
        commands.append(["python3", "scripts/validate_repo.py"])
        commands.append(["python3", "-m", "unittest", "discover", "-s", "tests", "-v"])
    elif day == 3:
        commands.append(["npm", "test"])
        commands.append(["npm", "run", "smoke"])
    elif day == 4:
        commands.append(["npm", "test"])
    elif day == 5:
        # 교육생 기본 경로: README 자연어 조립·점검. 게이트는 manifest READY만 확인.
        commands.append(
            [
                "python3",
                "-c",
                (
                    "import json,sys; from pathlib import Path; "
                    "p=Path('project/manifest.json'); "
                    "sys.exit(0) if p.exists() and json.loads(p.read_text(encoding='utf-8')).get('overall_status')=='READY' "
                    "else (print('project/manifest.json missing or not READY — run Day5 README prompt 1~2'), sys.exit(1))"
                ),
            ]
        )
    else:
        raise ValueError(f"invalid day: {day}")

    ok = True
    for cmd in commands:
        code, out = _run(cmd, cwd)
        commands_repr = commands  # keep reference
        exit_codes.append(code)
        logs.append(f"$ {' '.join(cmd)}\nexit={code}\n{out[-1500:]}")
        if code != 0:
            ok = False

    return ValidateResult(ok=ok, commands=commands_repr, exit_codes=exit_codes, log="\n\n".join(logs))


def read_project_title(day: int = 1) -> str:
    profile = profile_path(day)
    if profile.exists():
        data = load_json(profile)
        title = str(data.get("project_title", "")).strip()
        if title:
            return title

    prd = day_dir(1) / "docs" / "prd.md"
    if prd.exists():
        text = prd.read_text(encoding="utf-8")
        match = re.search(r"^#\s*AI PRD[·\s]+(.+)$", text, re.MULTILINE)
        if match:
            return match.group(1).strip()
    return "UNKNOWN"


def load_handoff(day: int) -> dict[str, Any] | None:
    path = handoff_path(day)
    if not path.exists():
        return None
    return load_json(path)


def handoff_status(day: int) -> str:
    data = load_handoff(day)
    if not data:
        return "MISSING"
    return str(data.get("status", "UNKNOWN")).upper()


def is_day_approved(day: int) -> bool:
    return handoff_status(day) == "APPROVED"


def can_enter_day(day: int, *, recheck_previous: bool = False) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if day == 1:
        return True, errors

    previous = day - 1
    prev_handoff = load_handoff(previous)
    if not prev_handoff:
        errors.append(
            f"Day {previous} 승인 패킷이 없습니다. "
            f"먼저 Day {previous} 검증 후 request_handoff.py --day {previous} 를 실행하세요."
        )
    elif str(prev_handoff.get("status", "")).upper() != "APPROVED":
        errors.append(
            f"Day {previous} 승인 상태가 APPROVED 가 아닙니다 (현재: {prev_handoff.get('status')}). "
            f"approve_handoff.py --day {previous} 로 사람 승인을 기록하세요."
        )

    if recheck_previous:
        result = run_day_validate(previous)
        if not result.ok:
            errors.append(f"Day {previous} 재검증 FAIL. 승인 전 실습을 다시 완료하세요.")

    return not errors, errors


def build_handoff_request(
    day: int,
    *,
    requested_by: str,
    validate: ValidateResult,
) -> dict[str, Any]:
    profile_rel = None
    profile = profile_path(1)
    if profile.exists():
        profile_rel = str(profile.relative_to(REPO_ROOT))

    return {
        "schema_version": SCHEMA_VERSION,
        "day": day,
        "status": "PENDING",
        "project_title": read_project_title(),
        "project_profile": profile_rel,
        "requested_at": utc_now(),
        "requested_by": requested_by,
        "validate": {
            "commands": [" ".join(cmd) for cmd in validate.commands],
            "exit_codes": validate.exit_codes,
            "passed": validate.ok,
            "log_tail": validate.log[-3000:],
        },
        "approval": None,
        "next_day": day + 1 if day < 5 else None,
        "checklist_template": f"docs/handoffs/templates/day{day}-handoff-checklist.md",
    }


def approve_handoff(
    day: int,
    *,
    reviewer: str,
    reviewer_role: str,
    notes: str = "",
    checklist: dict[str, bool] | None = None,
) -> dict[str, Any]:
    path = handoff_path(day)
    if not path.exists():
        raise FileNotFoundError(f"handoff packet missing: {path}")

    data = load_json(path)
    if str(data.get("status", "")).upper() == "APPROVED":
        raise ValueError(f"Day {day} is already APPROVED")

    validate = data.get("validate", {})
    if not validate.get("passed"):
        raise ValueError(f"Day {day} validate.passed is false; fix tests before approval")

    data["status"] = "APPROVED"
    data["approval"] = {
        "status": "APPROVED",
        "reviewer": reviewer,
        "reviewer_role": reviewer_role,
        "approved_at": utc_now(),
        "notes": notes,
        "checklist": checklist or {},
    }
    save_json(path, data)
    return data


def journey_summary() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for day in range(1, 6):
        handoff = load_handoff(day)
        can_enter, _ = can_enter_day(day)
        rows.append(
            {
                "day": day,
                "path": str(day_dir(day).relative_to(REPO_ROOT)),
                "can_enter": can_enter,
                "handoff_status": handoff_status(day),
                "project_title": read_project_title() if day == 1 else read_project_title(),
                "approved_by": (handoff or {}).get("approval", {}) and (handoff or {}).get("approval", {}).get("reviewer"),
            }
        )
    return rows
