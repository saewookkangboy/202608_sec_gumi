---
name: prd-canvas-builder
description: Guide the user through AI PRD Canvas v1 from a morning proposal, creating prd.md, virtual sample-data, expected-output, and prd.pdf without using real business data.
---

# PRD Canvas Builder

Use this skill when the user asks to complete Day 1 AI PRD Canvas work in `mx-agentic-ai-day1-prd/`.

## Inputs

- `docs/proposal.pdf` or `docs/proposal.md` (read-only source)
- User interview answers for sections 5, 6, 7

## Outputs

- `docs/prd.md` — full Canvas 1-10 (8-10 reserved with known/unknown notes)
- `docs/prd.pdf` — single-page canvas via `python3 scripts/generate_canvas_pdf.py docs/prd.md`
- `sample-data/` — synthetic input files only
- `expected-output/` — target output example

## Rules

- Ask one question at a time during interview.
- Never request real customer, plant, or personal data.
- Sections 8, 9, 10: only "지금 아는 것 / 아직 모르는 것" — do not fully fill.
- Run self-check 8 items before file generation.
- Finish with `python3 scripts/validate_day1.py`.
- To verify the built-in example only: `python3 scripts/validate_day1.py --example quotation-bot`.
- To seed the standard layout from the example: `python3 scripts/bootstrap_example.py quotation-bot`.

## Workflow

1. Read proposal and migrate sections 1-4.
2. Interview sections 5, 6, 7 (create sample files immediately when structure is known).
3. Reserve sections 8, 9, 10.
4. Self-check table (strict pass/fail).
5. Write files and generate PDF.
6. Run validate_day1.py and report results.

Reference example: `docs/examples/quotation-bot/`. Full prompt: `docs/prompt.md`.
