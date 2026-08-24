# Day 3 → Day 4 핸드오프

## 연결 개념

| Day 3 | Day 4 |
|---|---|
| Canvas **5·6** 도구화 | Planner와 Executor가 그 도구를 호출합니다 |
| `APPROVE_WRITE` dry-run | HITL의 `AWAITING_APPROVAL`로 이어집니다 |
| smoke E2E | 파이프라인 전체와 사람 승인까지 넓어집니다 |

외부 MCP 연동 계획(`mcp/integration-plan.md`)은 Day 5의 `project/mcp/`로 옮겨 갑니다.

## 승인 전 체크리스트

- [ ] `npm test`와 `npm run smoke` 모두 PASS
- [ ] 승인 없는 쓰기가 막히는 걸 직접 보여 줄 수 있음
- [ ] 팀 PRD §6의 데이터 소스와 MCP 도구를 짝지어 문서화
- [ ] Day 4 역할(Planner/Verifier/Human) 담당자를 팀이 합의

```bash
cd mx-agentic-ai-day3-mcp-tools
python3 ../scripts/request_handoff.py --day 3
python3 ../scripts/approve_handoff.py --day 3 --reviewer "이름" --role instructor
python3 ../scripts/check_day_gate.py --enter-day 4
```
