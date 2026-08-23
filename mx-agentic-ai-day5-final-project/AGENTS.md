# Repository Instructions

## 목적

Day 1~4 산출물을 통합해 **최종 프로젝트**를 만들고 Day 5 발표를 준비한다.

## 4대 기술 기둥 통합

| 기둥 | Day | Day 5 위치 |
|---|---|---|
| Harness Engineering | 2 | `project/harness/` |
| LLMWiki + GraphRAG | 2 | `project/knowledge/` |
| MCP 제작·외부 연동 | 3 | `project/mcp/` |
| HITL + Multi-agent | 4 | `project/agents/` |

## 안전 규칙

- 합성·가상 데이터만 사용한다. 실제 사업장 정보, API 키, 자격증명을 커밋하지 않는다.
- `project/evidence/`에는 테스트 요약만 넣고, raw 로그에 민감 정보를 남기지 않는다.
- Day 1~4 원본 입력 폴더는 수정하지 않는다.
- 완료 전 `python3 scripts/assemble_project.py`와 `python3 scripts/validate_day5.py`를 실행한다.

## 작업 순서

1. `assemble_project.py`로 Day 1~4 manifest·evidence 수집
2. `project/docs/` 템플릿 작성 (final-prd, architecture, integration-map, demo-script)
3. `project/harness|knowledge|mcp|agents/` 각 층 문서 완성
4. `validate_day5.py` 통과 후 발표

Claude Code는 같은 폴더의 `CLAUDE.md`가 이 파일을 가져온다.
