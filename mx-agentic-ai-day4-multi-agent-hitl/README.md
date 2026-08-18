# Day 4 · 멀티 에이전트 협업과 HITL

계획자–실행자–검증자의 역할을 JSON 산출물과 상태 머신으로 구현하고, 검증 통과 후에도 사람 승인 전에는 최종 액션을 멈추는 실습입니다.

## 빠른 시작

```bash
cd mx-agentic-ai-day4-multi-agent-hitl
npm test
npm run demo
npm run demo:approve
node src/cli.mjs --fault missing-evidence
node src/cli.mjs --fault missing-evidence --persistent-fault
```

기본 실행은 `AWAITING_APPROVAL`, `--approve` 실행만 `APPROVED`, 지속 결함은 재시도 한도 후 `ESCALATED`인지 확인합니다.

## 상태 흐름

```text
PLANNED → EXECUTED → REJECTED → EXECUTED → VERIFIED
                                      ↓
                           AWAITING_APPROVAL → APPROVED
                                      ↓
                                  ESCALATED
```

## 참고 자료

- 전체 배포와 코드복사 절차: [GitHub 배포와 Day 2~4 실습 가이드](../docs/github-deployment-and-quickstart.md)
- 기술 배경과 공식 URL: [skill·기술 참고 자료](./docs/skill-and-tech-reference.md)

## Claude Code로 적용

```bash
claude
```

역할을 섞지 않고 아래 순서로 복사해 실행합니다.

```text
/plan-maintenance-analysis로 설비 오류와 품질 결함의 연관 분석 계획을 만들어줘.
목표, 순서가 있는 단계, 필요한 LOG/QUALITY evidence, PASS 기준을 정의하되
도구 조회·계산·설비 추천·승인은 하지 마.
```

```text
/execute-evidence-plan으로 승인된 plan만 실행해 evidence.json을 만들어줘.
fixtures/ 또는 승인된 MCP 도구만 사용하고 모든 수치에 로그 evidence ID와
품질 evidence ID를 연결해. 검증이나 최종 승인은 하지 마.
```

```text
/verify-maintenance-report로 evidence를 독립 검증해줘.
source evidence, equipment join key, defect-rate 계산을 확인하고 PASS, REJECT,
ESCALATE 중 하나를 구체적 사유와 함께 반환해. 실행자 결과를 직접 고치지 마.
```

```text
/request-human-approval로 verifier PASS 이후의 승인 패킷을 만들어줘.
추천안, 근거 요약, 검증 결과, 남은 불확실성을 포함하고 명시적인
approve/reject/revise 입력 전에는 AWAITING_APPROVAL에서 멈춰.
```

## Codex로 적용

```bash
codex
```

```text
Day 4 역할 계약을 순서대로 실행해줘.
1. $plan-maintenance-analysis: 실행 없이 계획과 PASS 기준만 작성
2. $execute-evidence-plan: 승인된 계획을 근거 ID와 함께 실행
3. $verify-maintenance-report: 결과를 수정하지 않고 독립 검증
4. $request-human-approval: PASS 후 승인 패킷을 만들고 사람 입력까지 정지

역할별 입력·출력 파일을 섞지 말고, 동일 결함은 최대 3회까지만 복구한 뒤
ESCALATED로 전환해. verifier PASS를 사람 승인으로 간주하지 말고,
마지막에 npm test와 runs/<run-id>/ 이벤트 순서를 검증해줘.
```

## 핵심 실습

1. `.agents/skills/`에서 역할별 입력·출력·금지 행동을 확인한다.
2. `--fault missing-evidence`로 결함을 주입해 반려를 확인한다.
3. 동일 결함을 3회 유지해 `ESCALATED`를 확인한다.
4. 승인 없는 실행은 `AWAITING_APPROVAL`에서 멈추는지 확인한다.
5. `--approve`를 명시한 경우에만 `APPROVED`로 끝나는지 확인한다.

모든 실행은 `runs/<run-id>/`에 plan, evidence, verification, approval, events를 남깁니다.

네 가지 종료 경로를 비교하는 팀 과제 프롬프트:

```text
Day 4 팀 과제를 네 시나리오로 수행해줘.
A. 정상 근거: VERIFIED 후 AWAITING_APPROVAL에서 정지
B. missing-evidence: Verifier REJECT 후 Executor 재실행
C. persistent missing-evidence: 동일 결함 3회 후 ESCALATED
D. 명시적 --approve: 검증 PASS 이후에만 APPROVED

각 시나리오의 plan.json, evidence.json, verification.json, approval.json,
events.jsonl을 확인하고 상태 전이가 계약과 일치하는지 비교해줘.
HITL은 승인 전 정지, HOTL은 이벤트 감시와 임계치 이관으로 구분해 설명해줘.
```

최근 실행의 이벤트를 확인합니다.

```bash
LATEST_RUN="$(find runs -mindepth 1 -maxdepth 1 -type d | sort | tail -n 1)"
printf '%s\n' "$LATEST_RUN"
sed -n '1,200p' "$LATEST_RUN/events.jsonl"
```

## 검증과 팀 브랜치 제출

```bash
npm test
git status --short
git diff --check
git add src/ test/ README.md
git commit -m "feat(day4): complete multi-agent HITL lab"
git push -u origin HEAD
```

`runs/run-*/`는 기본적으로 Git에서 제외됩니다. 대표 실행 증거 제출이 필요하면 실제 업무 데이터나 자격증명이 없는지 확인한 뒤 교육 진행자의 정책에 따라 별도 제출합니다.
