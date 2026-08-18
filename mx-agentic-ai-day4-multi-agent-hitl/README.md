# Day 4 · 멀티 에이전트 협업과 HITL

계획자–실행자–검증자의 역할을 JSON 산출물과 상태 머신으로 구현하고, 검증 통과 후에도 사람 승인 전에는 최종 액션을 멈추는 실습입니다.

## 빠른 시작

```bash
npm test
npm run demo
npm run demo:approve
```

## 상태 흐름

```text
PLANNED → EXECUTED → REJECTED → EXECUTED → VERIFIED
                                      ↓
                           AWAITING_APPROVAL → APPROVED
                                      ↓
                                  ESCALATED
```

## 참고 자료

A2A, Agent Orchestration, Loop Engineering, Eval Check, 계획자·실행자·검증자 계약, HITL/HOTL의 기술 배경 및 공식 URL은 [skill·기술 참고 자료](./docs/skill-and-tech-reference.md)를 참고합니다.

## 핵심 실습

1. `.agents/skills/`에서 역할별 입력·출력·금지 행동을 확인한다.
2. `--fault missing-evidence`로 결함을 주입해 반려를 확인한다.
3. 동일 결함을 3회 유지해 `ESCALATED`를 확인한다.
4. 승인 없는 실행은 `AWAITING_APPROVAL`에서 멈추는지 확인한다.
5. `--approve`를 명시한 경우에만 `APPROVED`로 끝나는지 확인한다.

모든 실행은 `runs/<run-id>/`에 plan, evidence, verification, approval, events를 남깁니다.
