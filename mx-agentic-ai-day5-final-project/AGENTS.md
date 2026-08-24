# Repository Instructions

## 목적

Day 1~4 산출물을 통합해 **최종 프로젝트**를 만들고 Day 5 발표를 준비한다.
교육생 기본 경로는 **자연어 프롬프트**(README 예제 1~9, `/final-project-assembler`)이다.

## 4대 기술 기둥 통합

| 기둥 | Day | Day 5 위치 |
|---|---|---|
| Harness Engineering | 2 | `project/docs/CLAUDE.md` 등 |
| LLMWiki + GraphRAG | 2 | `project/knowledge/` · `docs/relations.json` · `eval-top3.md` |
| MCP 제작·외부 연동 | 3 | `project/mcp/` |
| HITL + Multi-agent | 4 | `project/agents/` · `docs/gate-log.md` |

## 안전 규칙

- 합성·가상 데이터만 사용한다. 실제 사업장 정보, API 키, 자격증명을 커밋하지 않는다.
- `project/evidence/`에는 데모·점검 요약만 넣고, raw 로그에 민감 정보를 남기지 않는다.
- Day 1~4 원본 입력 폴더는 수정하지 않는다. 쓰기는 `project/`에만 한다.
- 근거 없는 값은 `UNKNOWN`으로 남긴다.
- `scripts/*.py`는 **선택(강사·자동화)** 경로이다. 교육생에게 기본으로 실행시키지 않는다.

## 작업 순서

1. README 예제 1)로 `project/` 조립 + `manifest.json`
2. 예제 2) 자가 점검 → `evidence/day5-self-check.md`
3. 예제 3)~5) 데모 데이터 · E2E · HITL
4. 예제 6)~8) architecture · final-prd · demo-script
5. 예제 9) 최종 점검 → 발표 (PASS ≠ 사람 승인)

Claude Code는 같은 폴더의 `CLAUDE.md`가 이 파일을 가져온다.
