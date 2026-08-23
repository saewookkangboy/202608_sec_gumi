# MCP 외부 연동 가이드

> Day 3 Standard는 **로컬 stdio MCP**입니다. Advanced와 Day 5에서는 **외부 MCP** 연동 계획·PoC를 작성합니다.

---

## 로컬 vs 외부

| 구분 | 로컬 MCP (Standard) | 외부 MCP (Advanced / Day 5) |
|---|---|---|
| 프로세스 | `node src/server.mjs` (stdio) | 원격 HTTP/SSE 또는 별도 호스트 |
| 데이터 | `data/equipment_logs.csv` | 사내 API, DB, 티켓 시스템 등 |
| 검증 | `npm test` + `npm run smoke` | smoke + 연동 계획서 |
| 자격증명 | 없음 (합성 데이터) | 환경 변수·승인 토큰 (실습은 계획만) |

---

## 외부 연동 4단계 (Day 5용)

1. **도구 목록** — 읽기 N개, 쓰기 1개, 승인 토큰 여부
2. **계약** — 입력 Schema, `evidence_id`, 오류 형식 (Day 3 `/mcp-tool-designer` 동일)
3. **연결** — Claude Code `claude mcp add` 또는 프로젝트 `.mcp.json`
4. **검증** — E2E smoke + dry-run 쓰기 차단

템플릿: [`mcp/integration-plan.template.md`](../mcp/integration-plan.template.md)  
예시 설정: [`mcp/external-servers.example.json`](../mcp/external-servers.example.json)

---

## Day 3 → Day 5 핸드오프

| Day 3 산출 | Day 5 위치 |
|---|---|
| 3개 도구 계약 표 | `project/mcp/tool-contracts.md` |
| smoke PASS 로그 | `project/evidence/day3-smoke.txt` |
| 외부 연동 계획 | `project/mcp/integration-plan.md` |

---

## 안전 규칙 (외부 연동 시)

- 실제 API 키·사업장 URL을 저장소에 커밋하지 않는다.
- `.env`는 `.gitignore`에 두고, 계획서에만 변수 **이름**을 적는다.
- 쓰기 도구는 Day 3와 동일하게 승인 토큰 없으면 dry-run.
