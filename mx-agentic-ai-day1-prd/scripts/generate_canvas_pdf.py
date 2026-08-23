#!/usr/bin/env python3
"""Generate AI PRD Canvas PDF (A4 single page) from prd.md metadata."""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path


def _extract_field(text: str, pattern: str, default: str = "") -> str:
    match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    if not match:
        return default
    return re.sub(r"\s+", " ", match.group(1).strip())


def parse_prd_md(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s*AI PRD[·\s]+(.+)$", text, re.MULTILINE)
    agent_name = title_match.group(1).strip() if title_match else "에이전트"

    sections: dict[str, str] = {}
    for num, label in [
        ("1", "배경"),
        ("2", "목표"),
        ("3", "사용자"),
        ("4", "업무 흐름"),
        ("5", "AI 역할"),
        ("6", "데이터"),
        ("7", "출력"),
        ("8", "평가"),
        ("9", "안전"),
        ("10", "운영"),
    ]:
        pattern = rf"##\s*{num}\.\s*[^\n]*\n(.*?)(?=\n##\s*\d+\.|\Z)"
        sections[num] = _extract_field(text, pattern)

    donts = re.findall(r"(?:✕|하지 않는 일|하면 안 되는 일)[^\n]*\n((?:- .+\n?)+)", text)
    dont_lines = donts[0] if donts else ""
    dont_items = [
        line.lstrip("- ").strip()
        for line in dont_lines.splitlines()
        if line.strip().startswith("-")
    ]

    sample_files = sorted(
        str(p.name)
        for p in (path.parent.parent / "sample-data").glob("*")
        if p.is_file() and p.name != ".gitkeep"
    )
    output_files = sorted(
        str(p.name)
        for p in (path.parent.parent / "expected-output").glob("*")
        if p.is_file() and p.name != ".gitkeep"
    )

    return {
        "agent_name": agent_name,
        "author": "구매팀 (합성 예시)",
        "date": "2026-08-24",
        "sections": sections,
        "dont_items": dont_items[:4],
        "sample_files": sample_files,
        "output_files": output_files,
    }


def _shorten(value: str, limit: int = 180) -> str:
    clean = re.sub(r"[*`#\[\]]", "", value)
    clean = re.sub(r"\s+", " ", clean).strip()
    if len(clean) <= limit:
        return clean
    return clean[: limit - 1] + "…"


def build_html(data: dict[str, object]) -> str:
    sections = data["sections"]
    dont_items = data["dont_items"]
    sample_files = data["sample_files"]
    output_files = data["output_files"]

    def cell(num: str, title: str, body: str, *, highlight: bool = False, locked: str = "") -> str:
        cls = "cell highlight" if highlight else "cell"
        if locked:
            cls += " locked"
        badge = f'<span class="lock-badge">{locked}</span>' if locked else ""
        return f"""
        <div class="{cls}">
          <div class="cell-head"><span class="num">{num}</span> {html.escape(title)} {badge}</div>
          <div class="cell-body">{html.escape(_shorten(body))}</div>
        </div>"""

    dont_html = ""
    if dont_items:
        dont_html = "<div class='dont'>✕ 하면 안 되는 일: " + html.escape("; ".join(dont_items)) + "</div>"

    sec5 = sections.get("5", "") + dont_html
    chips = "".join(f"<span class='chip'>{html.escape(f)}</span>" for f in sample_files + output_files)

    cells = [
        cell("1", "배경", sections.get("1", "")),
        cell("2", "목표", sections.get("2", "")),
        cell("3", "사용자", sections.get("3", "")),
        cell("4", "업무 흐름", sections.get("4", "")),
        cell("5", "AI 역할", sec5, highlight=True),
        cell("6", "데이터 / 컨텍스트", sections.get("6", ""), highlight=True),
        cell("7", "출력 명세", sections.get("7", ""), highlight=True),
        cell("8", "평가 기준", sections.get("8", ""), locked="🔒 DAY 2"),
        cell("9", "안전 / 거버넌스", sections.get("9", ""), locked="🔒 DAY 4"),
        cell("10", "운영 지표", sections.get("10", ""), locked="🔒 DAY 4"),
    ]

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<style>
@page {{ size: A4; margin: 10mm; }}
* {{ box-sizing: border-box; }}
body {{
  font-family: "Malgun Gothic", "Apple SD Gothic Neo", sans-serif;
  color: #1a1a1a;
  margin: 0;
  padding: 8mm;
  font-size: 9.5px;
  line-height: 1.35;
}}
.header {{
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-bottom: 2.5px solid #1428A0;
  padding-bottom: 6px;
  margin-bottom: 8px;
}}
.samsung {{ font-family: Arial, sans-serif; font-weight: 800; color: #1428A0; font-size: 16px; }}
.canvas-label {{ color: #1428A0; font-weight: 700; font-size: 11px; }}
.title-row {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 6px 0 8px;
}}
.title-row h1 {{ margin: 0; font-size: 18px; color: #1428A0; }}
.meta {{ color: #555; font-size: 9px; }}
.badge {{
  background: #1428A0; color: #fff; border-radius: 999px;
  padding: 3px 10px; font-size: 9px; font-weight: 700;
}}
.intent {{
  background: #E8ECFA; color: #1428A0; font-weight: 700;
  font-size: 8.5px; padding: 4px 8px; border-radius: 6px; margin-bottom: 6px;
}}
.grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
}}
.cell {{
  border: 1px solid #ccd3e0;
  border-radius: 6px;
  padding: 6px 8px;
  min-height: 62px;
}}
.cell.highlight {{
  background: #E8ECFA;
  border-color: #1428A0;
}}
.cell.locked {{
  background: #f3f4f6;
  border: 1px dashed #9aa3b2;
}}
.cell-head {{ font-weight: 700; margin-bottom: 3px; font-size: 9px; }}
.num {{ color: #1428A0; }}
.cell-body {{ color: #333; }}
.dont {{ color: #B42318; font-weight: 700; margin-top: 3px; font-size: 8.5px; }}
.lock-badge {{ font-size: 8px; color: #666; }}
.files {{
  border: 1px solid #ccd3e0; border-radius: 6px; padding: 6px 8px; margin-top: 6px;
}}
.files-title {{ font-weight: 700; margin-bottom: 4px; }}
.chip {{
  display: inline-block; background: #e9edf3; border-radius: 999px;
  padding: 2px 8px; margin: 2px 3px 0 0; font-size: 8px;
}}
.note {{
  border-left: 3px solid #1428A0; padding-left: 8px; margin-top: 6px;
  color: #1428A0; font-size: 8.5px;
}}
.footer {{
  margin-top: 6px; text-align: center; color: #666; font-size: 8px;
}}
</style>
</head>
<body>
  <div class="header">
    <div class="samsung">SAMSUNG</div>
    <div class="canvas-label">AI PRD CANVAS · DAY 1</div>
  </div>
  <div class="title-row">
    <div>
      <h1>{html.escape(str(data["agent_name"]))}.</h1>
      <div class="meta">{html.escape(str(data["author"]))} | {html.escape(str(data["date"]))}</div>
    </div>
    <div class="badge">v1 — Day 1</div>
  </div>
  <div class="intent">▸ INTENT 5요소 파생 — AI PRD의 핵심 3칸</div>
  <div class="grid">
    {''.join(cells)}
  </div>
  <div class="files">
    <div class="files-title">📁 함께 만든 파일</div>
    {chips or '<span class="chip">sample-data/</span><span class="chip">expected-output/</span>'}
  </div>
  <div class="note">
    완벽한 PRD보다 '무엇을 아직 모르는지'가 드러나는 PRD가 더 유용합니다.
    — 8·9·10은 Day 2·4에서 채웁니다.
  </div>
  <div class="footer">SAMSUNG ELECTRONICS · AI 에이전트 실무 교육 · Day 1 결과물 ② — AI PRD (v1)</div>
</body>
</html>"""


def render_pdf(html_content: str, output_path: Path) -> None:
    from playwright.sync_api import sync_playwright

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.set_content(html_content, wait_until="networkidle")
        page.pdf(
            path=str(output_path),
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        browser.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate AI PRD Canvas PDF from prd.md")
    parser.add_argument("input", type=Path, help="Path to docs/prd.md")
    parser.add_argument("output", type=Path, nargs="?", help="Path to docs/prd.pdf")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: input not found: {args.input}", file=sys.stderr)
        return 1

    output = args.output or args.input.with_suffix(".pdf")
    data = parse_prd_md(args.input)
    html_content = build_html(data)
    render_pdf(html_content, output)
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
