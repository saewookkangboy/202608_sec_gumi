#!/usr/bin/env python3
"""
assemble_project.py (202608_sec_gumi 레포 버전)

레포의 실제 폴더 구조(Day1~4가 서로 다른 최상위 폴더)에 맞춰,
각 Day 산출물을 mx-agentic-ai-day5-final-project/project/ 로 모아
발표용 패키지를 만들어요.

- 원본 파일은 건드리지 않고 복사만 해요.
- 각 레이어의 존재 여부와 개수를 manifest.json에 기록해요.
- integration-map.md를 자동 생성해 Day2~4 산출물과 완료 상태를 한눈에 보여줘요.

사용법 (mx-agentic-ai-day5-final-project/ 안에서 실행):
    python3 scripts/assemble_project.py
    (레포 루트는 스크립트 위치 기준으로 자동 계산돼요. 다른 위치를 쓰려면
     python3 scripts/assemble_project.py --repo-root [경로] 로 지정해요)
"""

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


LAYERS = {
    "knowledge": {
        "path": "mx-agentic-ai-day2-knowledge-harness/knowledge",
        "glob": "*.md",
        "min_count": 10,
        "label": "Day2 지식그래프",
    },
    "mcp": {
        "path": "mx-agentic-ai-day3-mcp-tools/mcp",
        "glob": "*/contract.json",
        "min_count": 2,
        "label": "Day3 MCP 계약",
    },
    "agents": {
        "path": "mx-agentic-ai-day4-multi-agent-hitl/agents",
        "glob": "*.md",
        "min_count": 3,
        "label": "Day4 에이전트 역할",
    },
}

# (레포 루트 기준 상대경로, project/docs/ 안에서 쓸 파일명)
SUPPORT_FILES = [
    ("mx-agentic-ai-day1-prd/docs/prd.md", "prd.md"),
    ("CLAUDE.md", "CLAUDE.md"),
    ("mx-agentic-ai-day2-knowledge-harness/relations.json", "relations.json"),
    ("mx-agentic-ai-day2-knowledge-harness/eval-top3.md", "eval-top3.md"),
    ("mx-agentic-ai-day4-multi-agent-hitl/gate-log.md", "gate-log.md"),
]


def check_layer(repo_root: Path, name: str, spec: dict) -> dict:
    layer_path = repo_root / spec["path"]
    files = sorted(layer_path.glob(spec["glob"])) if layer_path.exists() else []
    status = "PASS" if len(files) >= spec["min_count"] else "INCOMPLETE"
    return {
        "layer": name,
        "label": spec["label"],
        "count": len(files),
        "required": spec["min_count"],
        "status": status,
        "files": [str(f.relative_to(repo_root)) for f in files],
    }


def copy_layer(repo_root: Path, project_dir: Path, name: str, spec: dict):
    src = repo_root / spec["path"]
    if src.exists():
        dst = project_dir / name
        shutil.copytree(src, dst, dirs_exist_ok=True)


def build_integration_map(project_docs: Path, results: list):
    lines = ["# Integration Map", "", f"생성 시각: {datetime.now().isoformat(timespec='seconds')}", ""]
    lines.append("| 레이어 | 원본 경로 (레포 루트 기준) | 산출물 수 | 기준 | 상태 |")
    lines.append("|---|---|---|---|---|")
    for r in results:
        origin = LAYERS[r["layer"]]["path"]
        lines.append(f"| {r['label']} | `{origin}` | {r['count']} | {r['required']}건 이상 | {r['status']} |")
    lines.append("")
    lines.append("## 상세 파일 목록")
    for r in results:
        lines.append(f"\n### {r['label']}")
        if r["files"]:
            for f in r["files"]:
                lines.append(f"- {f}")
        else:
            lines.append("- (없음)")
    (project_docs / "integration-map.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo-root",
        default=None,
        help="레포 루트 경로. 지정하지 않으면 스크립트 위치 기준으로 자동 계산돼요.",
    )
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    day5_dir = script_path.parent.parent  # scripts/의 부모 = mx-agentic-ai-day5-final-project/
    repo_root = Path(args.repo_root).resolve() if args.repo_root else day5_dir.parent

    project_dir = day5_dir / "project"
    project_docs = project_dir / "docs"
    project_evidence = project_dir / "evidence"
    project_docs.mkdir(parents=True, exist_ok=True)
    project_evidence.mkdir(parents=True, exist_ok=True)

    # 1) 레이어 점검 + 복사
    results = []
    for name, spec in LAYERS.items():
        result = check_layer(repo_root, name, spec)
        results.append(result)
        copy_layer(repo_root, project_dir, name, spec)

    # 2) 지원 파일 복사
    for rel_src, dst_name in SUPPORT_FILES:
        src = repo_root / rel_src
        if src.exists():
            shutil.copy2(src, project_docs / dst_name)

    # 3) integration-map.md 생성
    build_integration_map(project_docs, results)

    # 4) manifest.json 생성
    manifest = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "repo_root": str(repo_root),
        "layers": results,
        "overall_status": "READY" if all(r["status"] == "PASS" for r in results) else "NOT_READY",
    }
    (project_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # 5) 결과 출력
    print(f"레포 루트: {repo_root}")
    print(f"project/ 생성 완료 -> {project_dir}")
    for r in results:
        origin = LAYERS[r["layer"]]["path"]
        print(f"  [{r['status']}] {r['label']} <- {origin}: {r['count']}/{r['required']}")
    print(f"전체 상태: {manifest['overall_status']}")
    if manifest["overall_status"] != "READY":
        print("-> INCOMPLETE 레이어를 보강한 뒤 다시 실행해 주세요. (project/는 최신 상태로 다시 덮어써요)")


if __name__ == "__main__":
    main()
