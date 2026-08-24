---
name: final-project-assembler
description: Assemble Day 1-4 lab artifacts into project/ using natural-language steps, then prepare demo evidence and presentation docs without requiring Python scripts.
---

# Final Project Assembler

Use when completing Day 5: integrate Harness, LLMWiki/GraphRAG, MCP, and HITL/Multi-agent into `project/` **via Claude Code prompts** (no Python required for the trainee path).

## Workflow (prompt order)

Follow `README.md` 예제 1)~9) in order. Do not skip ahead.

1. **Assemble `project/`** — copy Day2 `knowledge/`, Day3 `mcp/`, Day4 `agents/`; copy support files into `project/docs/`; write `integration-map.md` and `manifest.json` (`READY` / `NOT_READY`).
2. **Self-check** — inspect files and write `project/evidence/day5-self-check.md` (no Python).
3. **Demo data** — `project/evidence/demo-data.json` (synthetic only).
4. **E2E simulation** — Planner → Executor(mock MCP) → Verifier → `demo-run-*.json` with evidence IDs.
5. **HITL gate** — pause for human approve/reject; record `APPROVED` in demo-run.
6. **Architecture** — mermaid 4-layer map in `project/docs/architecture.md`.
7. **Final PRD** — complete Canvas 1~10 in `project/docs/final-prd.md`.
8. **Demo script** — 5~7 min, 문제→구현→검증→한계.
9. **Final check** — `project/evidence/day5-final-check.md`.

## Rules

- Synthetic data only. No credentials in evidence or docs.
- Do not modify Day 1–4 raw inputs (`data/raw/`, `data/`, `fixtures/`). Write only under `project/`.
- Missing values → `UNKNOWN`. Never invent evidence IDs.
- Verifier PASS is not human approval — HITL must be explicit.
- Python under `scripts/` is optional instructor tooling only; do not tell trainees to run it unless they ask.

## Tech pillars mapping

| Pillar | project path |
|---|---|
| Harness Engineering | `project/docs/CLAUDE.md` (+ harness notes if present) |
| LLMWiki + GraphRAG | `project/knowledge/` · `docs/relations.json` · `eval-top3.md` |
| MCP | `project/mcp/` |
| HITL + Multi-agent | `project/agents/` · `docs/gate-log.md` |

Reference: `README.md`, `../../docs/tech-pillars.md`, `../../docs/curriculum-5day.md`
