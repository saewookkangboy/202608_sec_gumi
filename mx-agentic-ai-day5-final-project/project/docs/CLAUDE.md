# 202608_sec_gumi

삼성 MX 구미 에이전틱 AI 5일 실습 모노레포입니다. **모든 실습은 Claude Code**에서 진행합니다.

## 실행 방법

1. 해당 일자 폴더로 이동 (`cd mx-agentic-ai-dayN-...`)
2. `claude` 실행
3. `/skill-name`을 입력하거나 README·배포 가이드의 완성형 프롬프트를 붙여넣기
4. 완료 전 해당 일자 README의 **실행·테스트 조건**과 검증 스크립트를 확인

## Repo skill (Claude Code)

| Day | Skill | 용도 |
|:---:|---|---|
| 1 | `/prd-canvas-builder` | AI PRD Canvas 1~7, sample-data |
| 2 | `/eco-knowledge-builder` · `/repo-harness-auditor` | 지식 정규화, 하네스 감사 |
| 3 | `/mcp-tool-designer` · `/mcp-smoke-test` | MCP 도구 계약, E2E smoke |
| 4 | `/plan-maintenance-analysis` · `/execute-evidence-plan` · `/verify-maintenance-report` · `/request-human-approval` | 역할 분리, HITL |
| 5 | `/final-project-assembler` | `project/` 통합·발표 |

Day README 공통 섹션: **이론 → 사용법 → 저장소 구조 → 예제 → 실행 → 테스트 조건 → 문제 해결**

Day 3 MCP는 `mcp/` 계약·mock이 기본이고, (선택) `.mcp.json`의 `equipment-log` stdio 서버를 사용합니다. 연결 확인: `claude mcp list`

일차 간 이동은 사람 승인 후 `check_day_gate.py --enter-day N`입니다. 가이드: [`docs/handoffs/README.md`](docs/handoffs/README.md)

@AGENTS.md
