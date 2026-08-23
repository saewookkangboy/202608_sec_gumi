# Day 3 → Day 4 핸드오프

## 연결 개념

| Day 3 | Day 4 |
|---|---|
| Canvas **5·6** 도구화 | Planner/Executor가 도구 호출 |
| `APPROVE_WRITE` dry-run | HITL `AWAITING_APPROVAL` |
| smoke E2E | 파이프라인 전체 + 사람 승인 |

외부 MCP 연동 계획(`mcp/integration-plan.md`)은 Day 5 `project/mcp/`로 이식합니다.

## 승인 전 체크리스트

- [ ] `npm test` + `npm run smoke` PASS
- [ ] 승인 없는 쓰기 차단 시연 가능
- [ ] 팀 PRD §6 데이터 소스 ↔ MCP 도구 매핑 문서화
- [ ] Day 4 역할(Planner/Verifier/Human) 담당 합의

```bash
cd mx-agentic-ai-day3-mcp-tools
python3 ../scripts/request_handoff.py --day 3
python3 ../scripts/approve_handoff.py --day 3 --reviewer "이름" --role instructor
python3 ../scripts/check_day_gate.py --enter-day 4
```
