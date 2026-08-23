# HITL / HOTL 정책

> Day 4 `AWAITING_APPROVAL` · `ESCALATED` 패턴을 실무에 맞게 정의합니다.

## 승인 게이트

| 단계 | 자동 통과 | 사람 필요 |
|---|---|:---:|
| 검증 PASS | ☐ | |
| 최종 발송/실행 | ☐ | ✅ |
| 파일 쓰기 (MCP) | dry-run | `APPROVE_WRITE` |

## 승인 패킷 필수 필드

1. 추천안 / 결과 요약
2. 근거 ID 목록
3. 검증 결과 (PASS/REJECT)
4. 남은 불확실성
5. 면책 문구

## HOTL 이관

- 동일 결함 N회: 3
- 이관 대상: 파트장 / 온콜
- 로그: events.jsonl (자격증명·PII 제외)

## Day 4 증거

- `../evidence/day4-tests.txt`
