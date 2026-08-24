# Day 4 — Multi-agent (E2E → A2A) + HITL/HOTL

> 레포 경로: `mx-agentic-ai-day4-multi-agent-hitl/README.md`
>
> ⚠️ 참고: 레포의 기존 Day4는 실제 동작하는 Node 데모(`npm test && npm run demo`)를 사용했어요. 이 버전은 역할·A2A·게이트를 먼저 문서로 설계하는 데 집중해요. 기존 데모 코드가 있다면 [선택] 단계에서 이어서 활용해도 돼요.

**교육 질문**: 내 PRD를 혼자 처리하기 버거운 지점을 역할로 나누고, 그 역할들이 서로 직접 대화해야 하는 곳은 어디고, 사람은 언제 멈춰야 할까요?

---

## 이론

**E2E vs A2A**
- E2E(End-to-End): 하나의 파이프라인이 순서대로 실행돼요 — 요청 → 처리 → 응답.
- A2A(Agent-to-Agent): 에이전트들이 서로에게 직접 요청을 보내고 응답을 주고받아요. 예를 들어 Verifier가 문제를 발견하면 Executor에게 "이 부분만 다시 실행해 줘"라고 직접 요청해요. E2E가 "일렬로 선 사람들"이라면 A2A는 "필요할 때 서로 되묻는 팀"이에요.

**HITL (Human-In-The-Loop)**
자동 검증을 통과해도, 사람이 최종 승인해야 다음 단계로 넘어가는 게이트예요. 되돌릴 수 없는 행동(쓰기, 발송, 발주) 앞에 둬요.

**HOTL (Human-On/Out-The-Loop)**
같은 문제가 반복되면(예: 3회) 매번 사람에게 묻지 않고 별도 처리 경로(`ESCALATED`)로 이관해요. 사람이 루프 "안"이 아니라 "밖"에서 예외만 처리하는 구조예요.

**상태 머신**
```
정상 흐름: VERIFIED → AWAITING_APPROVAL → APPROVED
예외 흐름: (반복 실패 N회) → ESCALATED
```

---

## 사용법

1. 레포 루트에서 `cd mx-agentic-ai-day4-multi-agent-hitl` 후 Claude Code를 열어요.
2. Day3 도구 계약은 `../mx-agentic-ai-day3-mcp-tools/mcp/`를, Day1 PRD는 `../mx-agentic-ai-day1-prd/docs/prd.md`를 참조해요 (모두 읽기 전용).
3. 최소 3역할(Planner / Executor / Verifier) + Human으로 시작해요. A2A는 이 중 실제로 서로 대화가 필요한 지점 1~2곳만 먼저 정의해요 — 처음부터 모든 역할 쌍을 연결하지 않아요.

---

## 저장소 구조

```
202608_sec_gumi/
├── mx-agentic-ai-day1-prd/docs/prd.md          # 참조만
├── mx-agentic-ai-day3-mcp-tools/
│   └── mcp/                                    # 참조만
└── mx-agentic-ai-day4-multi-agent-hitl/
    ├── README.md
    ├── (기존 Node 데모 코드 — 있다면 유지)
    ├── agents/
    │   ├── planner.md
    │   ├── executor.md
    │   ├── verifier.md
    │   ├── a2a-protocol.md                     # 발신자→수신자, 메시지 타입, 트리거 조건
    │   └── state-diagram.md
    └── gate-log.md                              # HITL 승인 기록 + HOTL 이관 조건
```

---

## 예제 (오늘 쓸 프롬프트 — 순서대로)

**1) 확산 — 역할 분리**
```
../mx-agentic-ai-day1-prd/docs/prd.md 실행을 한 에이전트가
처음부터 끝까지 다 하면 어디서 문제가 생길까요? 계획/실행/검증
역할로 나누도록 나한테 물어봐 주세요. 각 역할이
agents/[역할명].md로 저장되도록 정리해 주세요.
```

**2) A2A 설계**
```
이 역할들이 서로 "직접" 요청을 주고받아야 하는 지점이
있나요? (예: 검증 담당이 실행 담당에게 재실행을 요청)
누가 누구에게, 어떤 조건에서, 어떤 내용을 보내는지
나한테 하나씩 확인해서 a2a-protocol.md로 정리해 주세요.
```

**3) HITL 게이트**
```
이 흐름에서 자동 검증이 통과해도 사람이 반드시 멈춰서
확인해야 하는 지점이 어디인가요? 왜 거기여야 하는지
물어보고, gate-log.md에 VERIFIED → AWAITING_APPROVAL
→ APPROVED 형식으로 기록해 주세요.
```

**4) HOTL 이관**
```
같은 문제가 반복되면(예: 같은 오류 3회) 매번 사람에게
묻지 않고 다른 처리 경로로 넘겨야 할까요? 그 기준(횟수,
심각도)을 나한테 물어봐서 gate-log.md에 ESCALATED
조건으로 추가해 주세요.
```

**5) 메타 — 상태도**
```
지금까지 정한 역할-A2A-게이트-이관 규칙을 state-diagram.md에
상태 흐름도로 그려 주세요. 빠진 상태가 없는지 나한테
하나씩 확인시켜 주세요.
```

---

## 실행

1. 역할을 분리해요 (3개 이상)
2. A2A 메시지 규칙을 정의해요 (발신-수신-조건-내용)
3. HITL 게이트 지점을 확정해요
4. HOTL 이관 조건을 확정해요 (반복 횟수 기준)
5. 상태도를 작성해요
6. `../mx-agentic-ai-day1-prd/docs/prd.md`의 Canvas 9·10을 갱신해요
7. 모든 역할·게이트 정의가 끝나면, 임시 환경(`mx-agentic-ai-day4-multi-agent-hitl/_sandbox/`)에서 가상 테스트를 진행해도 되는지 나한테 먼저 물어봐 주세요. 승인을 받으면 아래 [테스트 조건]에 따라 진행해요
8. 가상 테스트 결과가 안정적이면 강사·멘토에게 최종 승인을 요청해요 (레포의 `approve_handoff.py --day 4`로 기록해요)

**Day4 승인 조건**: 역할 3개 이상 / A2A 메시지 규칙 1개 이상 / HITL 게이트 1곳 이상 / HOTL 이관 조건 정의

---

## 테스트 조건 (가상 테스트 — 임시 환경)

| 조건 | 내용 |
|---|---|
| 실행 위치 | `mx-agentic-ai-day4-multi-agent-hitl/_sandbox/`에서만 진행해요. `agents/`, `gate-log.md` 원본은 건드리지 않아요 |
| 데이터 | 합성 데이터로 만든 흐름만 사용해요 |
| 테스트 범위 | (1) 정상 흐름 1회 — `VERIFIED → AWAITING_APPROVAL → APPROVED` / (2) 예외 흐름 1회 — 같은 오류를 반복시켜 `ESCALATED`(HOTL)로 이관되는지 확인해요 |
| 되돌리기 | `_sandbox/` 폴더만 삭제하면 원상 복구돼요 |
| 시간 | 15분 안에 끝내요 (정상·예외 흐름을 각각 확인하므로 조금 더 걸릴 수 있어요) |
| 결과 반영 | 게이트 위치나 이관 조건에 문제가 있으면 승인 후 `gate-log.md`를 수정해요 |

---

## 문제 해결

| 상황 | 대응 |
|---|---|
| 역할이 너무 잘게 쪼개짐 | 3~4개로 제한하고, 그 이상은 "같은 역할 안의 단계"로 처리해요 |
| A2A 메시지가 애매함 | "누가 / 무엇을 근거로 / 무엇을 요청하는가" 3항목만 채우면 충분해요 |
| HITL 게이트를 너무 많이 넣고 싶어짐 | "되돌릴 수 없는 행동에만 게이트를 둔다"는 기준으로 좁혀요 |
| HOTL 기준(횟수)을 못 정함 | 우선 3회로 시작하고, Day5 데모 결과를 보고 조정해도 돼요 |
| 기존 Node 데모 코드와 충돌 | `agents/`는 역할 설계 전용 폴더로 새로 두고, 기존 데모는 [선택] 확장 시에만 건드려요 |
