#!/usr/bin/env python3
"""Copy a built-in Day 1 example into the standard deliverable layout."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

DAY1_ROOT = Path(__file__).resolve().parent.parent

EXAMPLES: dict[str, Path] = {
    "quotation-bot": DAY1_ROOT / "docs" / "examples" / "quotation-bot",
}

COPY_PLAN: list[tuple[str, str]] = [
    ("proposal.md", "docs/proposal.md"),
    ("prd.md", "docs/prd.md"),
    ("prd.pdf", "docs/prd.pdf"),
]


def _copy_tree(src_dir: Path, dest_dir: Path, force: bool) -> list[str]:
    copied: list[str] = []
    if not src_dir.exists():
        return copied

    dest_dir.mkdir(parents=True, exist_ok=True)
    for src in sorted(src_dir.iterdir()):
        if not src.is_file() or src.name == ".gitkeep":
            continue
        dest = dest_dir / src.name
        if dest.exists() and not force:
            raise FileExistsError(f"already exists: {dest.relative_to(DAY1_ROOT)}")
        shutil.copy2(src, dest)
        copied.append(str(dest.relative_to(DAY1_ROOT)))
    return copied


def bootstrap(example: str, force: bool = False) -> list[str]:
    src_root = EXAMPLES[example]
    if not src_root.is_dir():
        raise FileNotFoundError(f"example not found: {src_root}")

    copied: list[str] = []
    for src_rel, dest_rel in COPY_PLAN:
        src = src_root / src_rel
        dest = DAY1_ROOT / dest_rel
        if not src.exists():
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and not force:
            raise FileExistsError(f"already exists: {dest_rel}")
        shutil.copy2(src, dest)
        copied.append(dest_rel)

    copied.extend(_copy_tree(src_root / "sample-data", DAY1_ROOT / "sample-data", force))
    copied.extend(
        _copy_tree(src_root / "expected-output", DAY1_ROOT / "expected-output", force)
    )
    return copied


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy a built-in example into docs/, sample-data/, expected-output/."
    )
    parser.add_argument(
        "example",
        nargs="?",
        choices=sorted(EXAMPLES),
        help="복사할 예제 이름 (기본: quotation-bot)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="기존 산출물을 덮어씁니다.",
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

    example = args.example or "quotation-bot"
    try:
        copied = bootstrap(example, force=args.force)
    except FileExistsError as exc:
        print(f"FAIL · {exc}", file=sys.stderr)
        print("기존 파일을 유지하려면 --force 없이 중단되었습니다.", file=sys.stderr)
        print(f"덮어쓰려면: python3 scripts/bootstrap_example.py {example} --force", file=sys.stderr)
        return 1
    except FileNotFoundError as exc:
        print(f"FAIL · {exc}", file=sys.stderr)
        return 1

    if not copied:
        print("FAIL · 복사할 파일이 없습니다.", file=sys.stderr)
        return 1

    print(f"OK · {example} 예제를 표준 산출물 위치로 복사했습니다.")
    for rel in copied:
        print(f"  - {rel}")
    print()
    print("검증: python3 scripts/validate_day1.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
