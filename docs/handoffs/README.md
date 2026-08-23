# 일차 간 핸드오프 · 사람 승인 게이트

> **자동 검증 PASS ≠ 다음 일차 진입 허가.**  
> 각 Day 종료 시 **사람 승인(APPROVED)** 이 있어야 다음 Day를 시작할 수 있습니다.

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
       sync_from_prd.py → assemble → validate_day5
```

| 구분 | 내용 |
|---|---|
| **팀 PRD** | `mx-agentic-ai-day1-prd/docs/prd.md` — 본인 업무 에이전트 정의 |
| **참조 PRD** | [`reference-prd.md`](../reference-prd.md) — Day 2~4 합성 데이터 실습 시나리오 |
| **연결** | Day 2~4는 참조 구현으로 기술 기둥을 익히고, Day 5에서 팀 PRD로 되돌아와 통합 |

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

승인 패킷 위치: `mx-agentic-ai-day{N}-*/.lab/handoff-approval.json`

---

## 일차별 핸드오프

| 문서 | 내용 |
|---|---|
| [day1-to-day2.md](./day1-to-day2.md) | PRD → Harness/Eval |
| [day2-to-day3.md](./day2-to-day3.md) | 지식 → MCP 도구화 |
| [day3-to-day4.md](./day3-to-day4.md) | MCP → HITL/Multi |
| [day4-to-day5.md](./day4-to-day5.md) | 운영 → 최종 프로젝트 |

체크리스트 템플릿: [`templates/`](./templates/)

---

## 승인자 역할

| role | 설명 |
|---|---|
| `instructor` | 강사 (권장) |
| `mentor` | 현업 멘토 |
| `team_lead` | 팀 리드 |
| `trainee_lead` | 교육생 대표 (자가 점검 후 강사 확인 병행 시) |

검증 PASS를 승인으로 간주하지 않습니다. `approve_handoff.py` 를 **사람이 직접** 실행해야 합니다.
