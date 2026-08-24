# 상태 흐름도 (Day 4)

```text
정상:  PLANNED → EXECUTED → VERIFIED → AWAITING_APPROVAL → APPROVED
예외:  (동일 사유 반려 N회, 기본 3) → ESCALATED
```

| 상태 | 의미 | 다음으로 가는 조건 |
|---|---|---|
| VERIFIED | 자동 검증 통과 | HITL 게이트에서 사람 검토 |
| AWAITING_APPROVAL | 사람 승인 대기 | 승인 / 반려 / 수정 요청 |
| APPROVED | 최종 확정 | (종료) |
| ESCALATED | HOTL 이관 | 별도 처리 경로 |
