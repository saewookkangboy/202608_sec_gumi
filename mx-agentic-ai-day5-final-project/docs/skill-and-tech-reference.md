# Day 5 · 최종 프로젝트 · Skill + Tech

4대 기술 기둥을 `project/`에 통합합니다. **기본 경로는 자연어 프롬프트**입니다.

## Repo skill

### `/final-project-assembler`

README 예제와 동일한 순서:

1. `project/` 조립 (레이어 복사 · `manifest.json` · `integration-map.md`)
2. 자가 점검 (`day5-self-check.md`)
3. 데모 데이터 · E2E · HITL
4. `architecture.md` · `final-prd.md` · `demo-script.md`
5. 발표 직전 최종 점검 (`day5-final-check.md`)

파이썬 `scripts/assemble_project.py` · `validate_day5.py`는 **선택**입니다.

## 기술 기둥 요약

| 기둥 | Day | 검증(교육생) | 검증(선택) |
|---|---|---|---|
| Harness + LLMWiki | 2 | `eval-top3.md` · 근거 ID | `validate_repo.py` |
| MCP | 3 | `mcp/*/contract.json` · mock | `npm test` + smoke |
| HITL + Multi-agent | 4 | `agents/` · `gate-log.md` | `npm test` + demo |
| 통합 | 5 | README 예제 1~9 | (선택) assemble/validate 스크립트 |

→ [tech-pillars.md](../../docs/tech-pillars.md) · [presentation-rubric.md](./presentation-rubric.md) · [Day 5 README](../README.md)
