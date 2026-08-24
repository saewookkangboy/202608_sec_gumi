# Day 4 → Day 5 핸드오프

## 연결 개념

| Day 4 | Day 5 |
|---|---|
| Canvas **9·10** | `project/docs/final-prd.md` §9·§10 완성 |
| `agents/*.md` | `project/agents/` 복사 |
| `gate-log.md` | `project/docs/gate-log.md` · HITL 데모 |
| A2A / 상태도 | E2E 시뮬레이션 · 발표 스크립트 |

Day 1 팀 PRD는 조립 프롬프트가 `project/docs/prd.md`로 복사한 뒤, final-prd 프롬프트로 §8·9·10을 실습 결과로 채웁니다.

## 승인 전 체크리스트

- [ ] Day4 승인 조건 충족 (역할≥3 · HITL · HOTL)
- [ ] Day5 진입 게이트 통과
- [ ] 팀 PRD + 참조 실습 매핑 합의
- [ ] Day 5 발표 담당·일정 합의

```bash
cd mx-agentic-ai-day4-multi-agent-hitl
python3 ../scripts/request_handoff.py --day 4
python3 ../scripts/approve_handoff.py --day 4 --reviewer "이름" --role instructor
python3 ../scripts/check_day_gate.py --enter-day 5

cd ../mx-agentic-ai-day5-final-project
claude
# README 예제 1) project/ 조립 프롬프트부터 순서대로
```

→ [Day 5 README](../../mx-agentic-ai-day5-final-project/README.md) · [Day 4 상세](../../mx-agentic-ai-day4-multi-agent-hitl/docs/day5-handoff.md)
