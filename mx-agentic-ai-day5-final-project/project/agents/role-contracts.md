# 역할 계약 (Multi-agent)

> Day 4 4스킬 패턴을 팀 에이전트에 적용합니다.

| 역할 | skill (참조) | 입력 | 출력 | 금지 |
|---|---|---|---|---|
| Planner | plan-maintenance-analysis | 목표 | plan.json | 실행·승인 |
| Executor | execute-evidence-plan | plan | evidence.json | PASS/FAIL |
| Verifier | verify-maintenance-report | evidence | verification.json | 결과 수정 |
| Human | request-human-approval | verification PASS | approval.json | 자동 승인 |

## 팀 변형

[팀 업무에 맞게 역할명·산출물 파일명 조정]

## 상태 전이

```text
PLANNED → EXECUTED → VERIFIED → AWAITING_APPROVAL → APPROVED
                ↓ REJECTED (max 3) → ESCALATED
```
