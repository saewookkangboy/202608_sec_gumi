# Day 4 → Day 5 핸드오프 · HITL + Multi-agent

> Day 4에서 익힌 **역할 분리·HITL·HOTL**을 Day 5 최종 프로젝트의 **운영·거버넌스 층**으로 이식합니다.

---

## Day 4 산출 → Day 5 매핑

| Day 4 | Day 5 파일 |
|---|---|
| 4개 repo skill (역할 계약) | `project/agents/role-contracts.md` |
| HITL 상태 (`AWAITING_APPROVAL`) | `project/agents/hitl-policy.md` |
| `runs/*/events.jsonl` | `project/evidence/day4-demo.txt` |
| PRD 9·10 회고 | `project/docs/final-prd.md` §9·§10 |

---

## Multi-agent 역할 (실무 이식)

| 역할 | 실무 예시 | 금지 |
|---|---|---|
| Planner | 작업 범위·PASS 기준 정의 | 데이터 수정·승인 |
| Executor | 도구 호출·근거 수집 | PASS/FAIL 판정 |
| Verifier | 독립 검증 | 결과 수정 |
| Human | 최종 승인·반려 | 자동 승인 가정 |

---

## HITL 정책 템플릿 (Day 5)

`project/agents/hitl-policy.md`에 아래를 채웁니다:

1. **승인 게이트 위치** — 어떤 행동 직전에 멈추는가?
2. **승인 패킷 필드** — 결과, 근거, 검증, 불확실성
3. **이관 조건** — 동일 실패 N회, 임계치
4. **로그** — `events.jsonl`에 남길 항목 (자격증명 제외)

---

## Day 5 발표 시나리오 (4종 경로 중 2개 이상 시연 권장)

- A. 정상: VERIFIED → AWAITING_APPROVAL
- B. 결함 복구: REJECTED → 재실행
- C. 이관: 3회 동일 결함 → ESCALATED
- D. 승인: `--approve` → APPROVED

→ [Day 5 최종 프로젝트](../../mx-agentic-ai-day5-final-project/README.md)
