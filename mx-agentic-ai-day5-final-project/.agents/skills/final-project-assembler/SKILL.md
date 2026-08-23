---
name: final-project-assembler
description: Assemble Day 1-4 lab artifacts into the Day 5 project folder, fill integration-map from manifest, and prepare presentation deliverables.
---

# Final Project Assembler

Use when completing Day 5: integrate Harness, LLMWiki/GraphRAG, MCP, and HITL/Multi-agent into `project/`.

## Workflow

1. Run `python3 scripts/assemble_project.py` — manifest + evidence
2. Copy Day 1 `docs/prd.md` insights into `project/docs/final-prd.md` (complete sections 8-10)
3. Fill `project/docs/architecture.md` with team's 4-layer stack
4. Update `project/docs/integration-map.md` PASS checkboxes from manifest
5. Write `project/docs/demo-script.md` for 5-7 min presentation
6. Complete `project/harness/`, `knowledge/`, `mcp/`, `agents/` layer docs
7. Run `python3 scripts/validate_day5.py`

## Rules

- Synthetic data only. No credentials in evidence or docs.
- Do not modify Day 1-4 raw inputs.
- Verifier PASS is not human approval — document both in hitl-policy.md.

## Tech pillars mapping

| Pillar | project path |
|---|---|
| Harness Engineering | `project/harness/` |
| LLMWiki + GraphRAG | `project/knowledge/` |
| MCP | `project/mcp/` |
| HITL + Multi-agent | `project/agents/` |

Reference: `../../docs/tech-pillars.md`, `../../docs/curriculum-5day.md`
