#!/usr/bin/env python3
"""Collect Day 1~4 artifacts into Day 5 project manifest and evidence stubs."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parent
PROJECT = ROOT / "project"
EVIDENCE = PROJECT / "evidence"
MANIFEST = PROJECT / "manifest.json"

sys.path.insert(0, str(REPO / "scripts"))
from day_journey_lib import (  # noqa: E402
    handoff_path,
    handoff_status,
    load_json,
    profile_path,
)


def _run(cmd: list[str], cwd: Path) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=120,
        )
        out = (result.stdout or "") + (result.stderr or "")
        return result.returncode == 0, out.strip()[-2000:]
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, str(exc)


def check_day1() -> dict:
    day1 = REPO / "mx-agentic-ai-day1-prd"
    prd = day1 / "docs" / "prd.md"
    pdf = day1 / "docs" / "prd.pdf"
    example_prd = day1 / "docs" / "examples" / "quotation-bot" / "prd.md"
    validate_ok, validate_log = _run(["python3", "scripts/validate_day1.py"], day1)
    profile = profile_path(1)
    return {
        "path": str(day1.relative_to(REPO)),
        "prd_md": prd.exists() or example_prd.exists(),
        "prd_pdf": pdf.exists(),
        "sample_data": any(
            p.is_file() and p.name != ".gitkeep"
            for p in (day1 / "sample-data").glob("*")
        ),
        "expected_output": any(
            p.is_file() and p.name != ".gitkeep"
            for p in (day1 / "expected-output").glob("*")
        ),
        "validate_pass": validate_ok,
        "project_profile": profile.exists(),
        "handoff_status": handoff_status(1),
        "log_tail": validate_log,
    }


def check_day2() -> dict:
    day2 = REPO / "mx-agentic-ai-day2-knowledge-harness"
    ok, log = _run(["python3", "scripts/validate_repo.py"], day2)
    wiki = (day2 / "knowledge" / "WIKI.md").exists()
    return {
        "path": str(day2.relative_to(REPO)),
        "validate_pass": ok,
        "wiki_index": wiki,
        "knowledge_count": len(list((day2 / "knowledge" / "eco").glob("*.md"))),
        "handoff_status": handoff_status(2),
        "log_tail": log,
    }


def check_day3() -> dict:
    day3 = REPO / "mx-agentic-ai-day3-mcp-tools"
    test_ok, test_log = _run(["npm", "test"], day3)
    smoke_ok, smoke_log = _run(["npm", "run", "smoke"], day3)
    return {
        "path": str(day3.relative_to(REPO)),
        "npm_test_pass": test_ok,
        "smoke_pass": smoke_ok,
        "integration_plan_template": (
            day3 / "mcp" / "integration-plan.template.md"
        ).exists(),
        "handoff_status": handoff_status(3),
        "log_tail": smoke_log or test_log,
    }


def check_day4() -> dict:
    day4 = REPO / "mx-agentic-ai-day4-multi-agent-hitl"
    ok, log = _run(["npm", "test"], day4)
    return {
        "path": str(day4.relative_to(REPO)),
        "npm_test_pass": ok,
        "handoff_doc": (day4 / "docs" / "day5-handoff.md").exists(),
        "handoff_status": handoff_status(4),
        "log_tail": log,
    }


def write_evidence(name: str, content: str) -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    path = EVIDENCE / name
    path.write_text(content, encoding="utf-8")


def _load_profile_summary() -> dict:
    profile = profile_path(1)
    if not profile.exists():
        return {"exists": False}
    data = load_json(profile)
    return {
        "exists": True,
        "path": str(profile.relative_to(REPO)),
        "project_title": data.get("project_title", "UNKNOWN"),
        "mvp_sentence": data.get("mvp_sentence", "UNKNOWN"),
    }


def main() -> int:
    PROJECT.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)

    d1 = check_day1()
    d2 = check_day2()
    d3 = check_day3()
    d4 = check_day4()

    manifest = {
        "assembled_at": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(REPO),
        "days": {"day1": d1, "day2": d2, "day3": d3, "day4": d4},
        "handoffs": {
            f"day{n}": {
                "status": handoff_status(n),
                "path": str(handoff_path(n).relative_to(REPO)),
            }
            for n in range(1, 5)
        },
        "project_profile": _load_profile_summary(),
        "tech_pillars": {
            "harness_engineering": d2.get("validate_pass", False),
            "llmwiki_graphrag": d2.get("wiki_index", False),
            "mcp_integration": d3.get("smoke_pass", False),
            "hitl_multi_agent": d4.get("npm_test_pass", False),
        },
        "day5_outputs": {
            "final_prd": "project/docs/final-prd.md",
            "architecture": "project/docs/architecture.md",
            "integration_map": "project/docs/integration-map.md",
            "demo_script": "project/docs/demo-script.md",
        },
    }

    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    write_evidence(
        "day2-validate.txt",
        f"validate_pass={d2['validate_pass']}\nwiki={d2['wiki_index']}\n\n{d2.get('log_tail', '')}",
    )
    write_evidence(
        "day3-smoke.txt",
        f"test={d3['npm_test_pass']} smoke={d3['smoke_pass']}\n\n{d3.get('log_tail', '')}",
    )
    write_evidence(
        "day4-tests.txt",
        f"test={d4['npm_test_pass']}\n\n{d4.get('log_tail', '')}",
    )

    print(f"Wrote {MANIFEST.relative_to(ROOT)}")
    print(f"Wrote evidence/ (3 files)")
    for pillar, ok in manifest["tech_pillars"].items():
        status = "PASS" if ok else "PENDING"
        print(f"  {pillar}: {status}")
    for n in range(1, 5):
        status = manifest["handoffs"][f"day{n}"]["status"]
        print(f"  handoff_day{n}: {status}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
