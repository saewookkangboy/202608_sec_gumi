# Day 4 → Day 5 핸드오프

## 연결 개념

| Day 4 | Day 5 |
|---|---|
| Canvas **9·10** | `project/docs/final-prd.md`의 §9·§10을 완성합니다 |
| `agents/*.md` | `project/agents/`로 복사합니다 |
| `gate-log.md` | `project/docs/gate-log.md`가 되고 HITL 데모에 씁니다 |
| A2A와 상태도 | E2E 시뮬레이션과 발표 대본으로 이어집니다 |

Day 1 팀 PRD는 조립 프롬프트가 `project/docs/prd.md`로 복사해 줍니다. 그다음 final-prd 프롬프트로 §8·9·10을 실습 결과로 채웁니다.

## 승인 전 체크리스트

- [ ] Day 4 승인 조건 충족 (역할 3개 이상, HITL, HOTL)
- [ ] Day 5 진입 게이트 통과
- [ ] 팀 PRD와 참조 실습을 어떻게 짝지을지 합의
- [ ] Day 5 발표 담당자와 일정 합의

```bash
cd mx-agentic-ai-day4-multi-agent-hitl
python3 ../scripts/request_handoff.py --day 4
python3 ../scripts/approve_handoff.py --day 4 --reviewer "이름" --role instructor
python3 ../scripts/check_day_gate.py --enter-day 5

cd ../mx-agentic-ai-day5-final-project
claude
# README 예제 1) project/ 조립 프롬프트부터 순서대로 붙여넣어요
```

→ [Day 5 README](../../mx-agentic-ai-day5-final-project/README.md) · [Day 4 상세](../../mx-agentic-ai-day4-multi-agent-hitl/docs/day5-handoff.md)
