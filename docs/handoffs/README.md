# 일차 간 핸드오프 · 사람 승인 게이트

> **자동 검증이 PASS라고 해서 다음 일차로 넘어갈 수 있는 건 아닙니다.**  
> 각 Day를 마칠 때 **사람 승인(APPROVED)** 을 받아야 다음 Day를 시작할 수 있습니다.

---

## 5일 여정 (교육생 본인 PRD)

```text
Day 1  본인 PRD (docs/prd.md) + sample-data + expected-output
       init_project_profile.py → .lab/project-profile.json
       validate_day1.py → request_handoff --day 1 → [사람 승인]
         ▼
Day 2  참조 실습(Harness/LLMWiki) + 팀 PRD Canvas 8번 회고
       validate + request_handoff --day 2 → [사람 승인]
         ▼
Day 3  MCP 3도구 + smoke + 연동 계획 (Canvas 5·6)
       request_handoff --day 3 → [사람 승인]
         ▼
Day 4  HITL + Multi-agent (Canvas 9·10)
       request_handoff --day 4 → [사람 승인]
         ▼
Day 5  project/ 통합 · final-prd.md · 발표
       Claude Code에서 README 예제 1)~9) (조립 → 점검 → 데모 → 발표 문서)
```

| 구분 | 내용 |
|---|---|
| **팀 PRD** | `mx-agentic-ai-day1-prd/docs/prd.md` — 본인 업무 에이전트를 정의한 문서 |
| **참조 PRD** | [`reference-prd.md`](../reference-prd.md) — Day 2~4에서 합성 데이터로 실습하는 시나리오 |
| **연결 방식** | Day 2~4는 참조 구현으로 기술 기둥을 익히고, Day 5에서 다시 팀 PRD로 돌아와 통합합니다 |

---

## 공통 명령 (저장소 루트)

```bash
# 현황
python3 scripts/check_day_gate.py --status

# Day N 진입 전 (N≥2)
python3 scripts/check_day_gate.py --enter-day 2

# Day N 완료 후
python3 scripts/request_handoff.py --day 1
python3 scripts/approve_handoff.py --day 1 --reviewer "강사명" --role instructor
```

승인 패킷은 `mx-agentic-ai-day{N}-*/.lab/handoff-approval.json`에 저장됩니다.

---

## 일차별 핸드오프

| 문서 | 내용 |
|---|---|
| [day1-to-day2.md](./day1-to-day2.md) | PRD를 Harness·Eval로 잇기 |
| [day2-to-day3.md](./day2-to-day3.md) | 지식을 MCP 도구로 만들기 |
| [day3-to-day4.md](./day3-to-day4.md) | MCP를 HITL·Multi-agent로 넘기기 |
| [day4-to-day5.md](./day4-to-day5.md) | 운영 결과를 최종 프로젝트로 모으기 |

체크리스트 템플릿은 [`templates/`](./templates/)에 있습니다.

---

## 승인자 역할

| role | 설명 |
|---|---|
| `instructor` | 강사 (권장) |
| `mentor` | 현업 멘토 |
| `team_lead` | 팀 리드 |
| `trainee_lead` | 교육생 대표 (자가 점검 후 강사 확인을 함께 받을 때) |

검증이 PASS라도 그것을 승인으로 보지 않습니다. `approve_handoff.py`는 **사람이 직접** 실행해야 합니다.
