#!/usr/bin/env python3
"""Validate Day 1 PRD deliverables."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

DAY1_ROOT = Path(__file__).resolve().parent.parent

EXAMPLES: dict[str, Path] = {
    "quotation-bot": DAY1_ROOT / "docs" / "examples" / "quotation-bot",
}


@dataclass(frozen=True)
class DeliverablePaths:
    root: Path
    proposal_md: Path | None
    proposal_pdf: Path | None
    prd_md: Path
    prd_pdf: Path
    sample_dir: Path
    output_dir: Path

    @classmethod
    def from_root(cls, root: Path) -> DeliverablePaths:
        docs = root / "docs"
        proposal_md = docs / "proposal.md" if (docs / "proposal.md").exists() else None
        if proposal_md is None and (root / "proposal.md").exists():
            proposal_md = root / "proposal.md"

        proposal_pdf = docs / "proposal.pdf" if (docs / "proposal.pdf").exists() else None
        if proposal_pdf is None and (root / "proposal.pdf").exists():
            proposal_pdf = root / "proposal.pdf"

        if (docs / "prd.md").exists():
            prd_md = docs / "prd.md"
            prd_pdf = docs / "prd.pdf"
        else:
            prd_md = root / "prd.md"
            prd_pdf = root / "prd.pdf"

        return cls(
            root=root,
            proposal_md=proposal_md,
            proposal_pdf=proposal_pdf,
            prd_md=prd_md,
            prd_pdf=prd_pdf,
            sample_dir=root / "sample-data",
            output_dir=root / "expected-output",
        )


def _read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def check_proposal(paths: DeliverablePaths) -> list[str]:
    errors: list[str] = []
    if paths.proposal_pdf is None and paths.proposal_md is None:
        errors.append("proposal.pdf 또는 proposal.md 가 없습니다.")
    return errors


def check_prd_md(paths: DeliverablePaths) -> list[str]:
    errors: list[str] = []
    prd = paths.prd_md
    if not prd.exists():
        rel = prd.relative_to(paths.root)
        return [f"{rel} 가 없습니다."]

    text = _read(prd)
    for num in range(1, 11):
        if not re.search(rf"##\s*{num}\.", text):
            errors.append(f"prd.md에 {num}번 섹션이 없습니다.")

    if not re.search(r"(하지 않는 일|하면 안 되는 일|✕)", text):
        errors.append("5번 AI 역할에 '하지 않는 일'이 없습니다.")
    else:
        dont_count = len(re.findall(r"^-\s+", text, re.MULTILINE))
        if dont_count < 2:
            errors.append("5번 '하지 않는 일' 항목이 2개 미만입니다.")

    if not re.search(r"(누락|확인 필요|UNKNOWN|\[확인 필요\])", text, re.IGNORECASE):
        errors.append("6번 또는 7번에 누락/fallback 규칙이 없습니다.")

    for reserved in ("8", "9", "10"):
        block = re.search(rf"##\s*{reserved}\..*?(?=\n##\s*\d+\.|\Z)", text, re.DOTALL)
        if block and not re.search(r"(모르는|아직|Day 2|Day 4)", block.group(0)):
            errors.append(f"{reserved}번에 '아직 모르는 것' 또는 Day 예약 표시가 없습니다.")

    return errors


def check_samples(paths: DeliverablePaths) -> list[str]:
    errors: list[str] = []
    samples = [
        p for p in paths.sample_dir.glob("*") if p.is_file() and p.name != ".gitkeep"
    ]
    outputs = [
        p for p in paths.output_dir.glob("*") if p.is_file() and p.name != ".gitkeep"
    ]

    if not samples:
        errors.append("sample-data/ 에 파일이 없습니다.")
    if not outputs:
        errors.append("expected-output/ 에 파일이 없습니다.")

    return errors


def check_pdf(paths: DeliverablePaths) -> list[str]:
    pdf = paths.prd_pdf
    rel = pdf.relative_to(paths.root)
    if not pdf.exists():
        return [
            f"{rel} 가 없습니다. "
            f"python3 scripts/generate_canvas_pdf.py {paths.prd_md.relative_to(paths.root)} 로 생성하세요."
        ]
    if pdf.stat().st_size < 1000:
        return [f"{rel} 파일이 너무 작습니다."]
    return []


def validate(paths: DeliverablePaths, label: str | None = None) -> int:
    checks = [
        ("기획서", check_proposal),
        ("PRD 본문", check_prd_md),
        ("샘플 파일", check_samples),
        ("PRD PDF", check_pdf),
    ]

    if label:
        print(f"[{label}]")

    failed = False
    for name, fn in checks:
        errors = fn(paths)
        if errors:
            failed = True
            print(f"FAIL · {name}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"PASS · {name}")

    return 1 if failed else 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Day 1 PRD deliverables.")
    parser.add_argument(
        "--example",
        choices=sorted(EXAMPLES),
        help="검증할 내장 예제 이름 (예: quotation-bot)",
    )
    parser.add_argument(
        "--list-examples",
        action="store_true",
        help="사용 가능한 예제 목록을 출력합니다.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if args.list_examples:
        for name, path in sorted(EXAMPLES.items()):
            rel = path.relative_to(DAY1_ROOT)
            print(f"{name}\t{rel}")
        return 0

    if args.example:
        root = EXAMPLES[args.example]
        if not root.is_dir():
            print(f"FAIL · 예제 경로 없음: {root}", file=sys.stderr)
            return 1
        return validate(DeliverablePaths.from_root(root), label=args.example)

    return validate(DeliverablePaths.from_root(DAY1_ROOT))


if __name__ == "__main__":
    raise SystemExit(main())
