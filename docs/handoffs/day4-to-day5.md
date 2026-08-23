# Day 4 → Day 5 핸드오프

## 연결 개념

| Day 4 | Day 5 |
|---|---|
| Canvas **9·10** | `project/docs/final-prd.md` §9·§10 완성 |
| 역할 스킬 4종 | `project/agents/role-contracts.md` |
| HITL 정책 | `project/agents/hitl-policy.md` |
| `runs/*/events.jsonl` | `project/evidence/day4-tests.txt` |

Day 1 팀 PRD는 `sync_from_prd.py`로 final-prd 제목·연결을 맞춘 뒤 §8·9·10을 실습 결과로 채웁니다.

## 승인 전 체크리스트

- [ ] `npm test` PASS (결함 주입·이관·승인 시나리오 이해)
- [ ] demo 2종 이상 재현 가능
- [ ] 팀 PRD + 참조 실습 매핑 표 초안
- [ ] Day 5 발표 담당·일정 합의

```bash
cd mx-agentic-ai-day4-multi-agent-hitl
python3 ../scripts/request_handoff.py --day 4
python3 ../scripts/approve_handoff.py --day 4 --reviewer "이름" --role instructor
python3 ../scripts/check_day_gate.py --enter-day 5

cd ../mx-agentic-ai-day5-final-project
python3 scripts/sync_from_prd.py
python3 scripts/assemble_project.py
```

→ [Day 4 상세](../../mx-agentic-ai-day4-multi-agent-hitl/docs/day5-handoff.md)
