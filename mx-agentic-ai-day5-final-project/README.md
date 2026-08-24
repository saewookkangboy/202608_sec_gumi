# Day 5 — 최종 프로젝트 통합 및 데모

> 레포 경로: `mx-agentic-ai-day5-final-project/README.md`

**교육 질문**: Day 1~4를 내 업무 에이전트로 어떻게 통합하고, 실제로 동작한다는 걸 어떻게 증명할까요?

---

## 이론

- Day 1~4 결과물은 레포 안 여러 폴더에 흩어져 있어요. Day 5는 새로 만드는 날이 아니라 **그 네 폴더의 산출물을 모으고, 실행해 보고, 증명하는 날**이에요.
- 4층 구조는 `mx-agentic-ai-day1-prd/(정의)` → `mx-agentic-ai-day2-knowledge-harness/(신뢰)` → `mx-agentic-ai-day3-mcp-tools/(실행)` → `mx-agentic-ai-day4-multi-agent-hitl/(거버넌스)` 순서예요. `project/` 폴더가 이 4층을 하나로 모아서 보여 줍니다.
- **검증이 PASS라고 완성은 아니에요.** 체크리스트를 다 통과했어도, 데모 데이터를 흘려보내 처음부터 끝까지 도는 모습을 사람이 직접 봐야 비로소 완성이에요.
- 오늘은 **Claude Code에 자연어 프롬프트를 붙여넣는 방식**으로 진행해요. Day 1~4 원본은 읽기만 하고, 쓰기는 `project/` 안에서만 합니다.

---

## 사용법

1. 레포 루트에서 `cd mx-agentic-ai-day5-final-project` 후 `claude`를 열어요.
2. 아래 [예제] 프롬프트를 **1번부터 순서대로** 하나씩 붙여넣어요. 대괄호 `[ ]` 안만 본인 상황에 맞게 바꾸면 돼요.
3. 단계를 건너뛰거나 한꺼번에 시키지 마세요. 뒤 단계가 앞 단계의 `project/` 결과를 그대로 쓰거든요.
4. Day 1~4 원본 폴더는 고치지 않아요. 복사와 생성은 `project/` 안에서만 합니다.

---

## 저장소 구조

```
202608_sec_gumi/
├── CLAUDE.md
├── mx-agentic-ai-day1-prd/docs/prd.md
├── mx-agentic-ai-day2-knowledge-harness/{knowledge/, relations.json, eval-top3.md}
├── mx-agentic-ai-day3-mcp-tools/mcp/
├── mx-agentic-ai-day4-multi-agent-hitl/{agents/, gate-log.md}
└── mx-agentic-ai-day5-final-project/
    ├── README.md
    ├── scripts/                        # [선택] 자동화 보조 (교육생 기본 경로 아님)
    └── project/                        # 오늘 프롬프트로 만드는 발표 패키지
        ├── manifest.json               # overall_status: READY | NOT_READY
        ├── docs/
        │   ├── prd.md · CLAUDE.md · relations.json · eval-top3.md · gate-log.md
        │   ├── final-prd.md · architecture.md · integration-map.md · demo-script.md
        ├── evidence/
        │   ├── demo-data.json
        │   └── demo-run-[날짜].json
        ├── knowledge/  (Day2 복사본)
        ├── mcp/        (Day3 복사본)
        └── agents/     (Day4 복사본)
```

---

## 예제 (오늘 쓸 프롬프트 — 순서대로)

### 1) project/ 조립 — 레이어 복사 + manifest

```
레포 루트(이 폴더의 부모)를 기준으로 Day 1~4 산출물을
mx-agentic-ai-day5-final-project/project/ 로 모아 주세요.

규칙은 다음과 같아요.
- Day 1~4 원본은 고치거나 지우지 말고, project/에만 복사·생성해 주세요.
- 아래 폴더를 복사해 주세요.
  · ../mx-agentic-ai-day2-knowledge-harness/knowledge/ → project/knowledge/
  · ../mx-agentic-ai-day3-mcp-tools/mcp/ → project/mcp/
  · ../mx-agentic-ai-day4-multi-agent-hitl/agents/ → project/agents/
- 아래 지원 파일이 있으면 project/docs/로 복사해 주세요.
  · ../mx-agentic-ai-day1-prd/docs/prd.md → project/docs/prd.md
  · ../CLAUDE.md → project/docs/CLAUDE.md
  · ../mx-agentic-ai-day2-knowledge-harness/relations.json → project/docs/relations.json
  · ../mx-agentic-ai-day2-knowledge-harness/eval-top3.md → project/docs/eval-top3.md
  · ../mx-agentic-ai-day4-multi-agent-hitl/gate-log.md → project/docs/gate-log.md
- project/docs/와 project/evidence/ 폴더가 없으면 만들어 주세요.
- project/docs/integration-map.md를 표로 작성해 주세요.
  열은 레이어 | 원본 경로 | 산출물 수 | 기준 | 상태 로 잡아 주세요.
  기준은 knowledge md 10개 이상, mcp/*/contract.json 2개 이상,
  agents/*.md 3개 이상(README 제외)이에요.
- project/manifest.json도 만들어 주세요.
  generated_at, layers(레이어별 count/required/status/files), overall_status를 담고,
  세 레이어가 모두 PASS면 overall_status를 READY로, 아니면 NOT_READY로 해 주세요.
- NOT_READY라면 어떤 Day 폴더를 보강해야 하는지 알려 주세요.
- 이미 project/가 있어도 위 규칙대로 덮어써도 괜찮아요.
```

### 2) Day5 자가 점검 (검증 프롬프트)

```
방금 만든 project/를 발표 전에 점검해 주세요. 파이썬 스크립트는
쓰지 말고, 파일을 직접 읽어서 판정해 주세요.

확인할 것은 다음과 같아요.
1) project/manifest.json 의 overall_status 가 READY 인지
2) project/knowledge/, mcp/, agents/, docs/, evidence/ 폴더가 있는지
3) project/docs/ 에 integration-map.md 가 있는지
4) 부족한 항목이 있으면 PASS/FAIL 표로 보여 주시고, 어떤 Day로
   돌아가 무엇을 채우면 되는지만 알려 주세요
5) 결과는 project/evidence/day5-self-check.md 에 요약해서 저장해 주세요

근거 없는 값은 UNKNOWN으로 남겨 주세요.
```

### 3) 데모 데이터 생성

```
project/docs/prd.md의 배경·사용자·데이터 섹션을 읽고,
이 도메인에 맞는 합성 데모 데이터를 5~10건 만들어 주세요.
실제 회사명이나 개인정보는 절대 쓰지 마시고, 근거 ID 형식은
project/knowledge/ 에서 쓰던 방식과 똑같이 맞춰 주세요.
결과는 project/evidence/demo-data.json 으로 저장해 주세요.
```

### 4) E2E 실행 시뮬레이션

```
방금 만든 project/evidence/demo-data.json을 입력으로,
project/agents/planner.md 역할이 계획을 세우고,
project/agents/executor.md 역할이 project/mcp/[도구명]/contract.json에
따라 도구를 호출한다고 가정해서 mock 응답을 만들고,
project/agents/verifier.md 역할이 그 결과를 검증하는 과정을
순서대로 실행해 주세요. 각 단계 결과는 근거 ID와 함께
project/evidence/demo-run-[오늘날짜].json 에 기록해 주세요.
근거 없는 값은 지어내지 말고 UNKNOWN으로 남겨 주세요.
```

### 5) HITL 게이트 실행

```
검증까지 끝났으면 project/docs/gate-log.md에 정해 둔 승인
지점에서 멈추고, 제가 승인이나 반려를 고를 수 있는 형태로
결과를 보여 주세요. 제가 승인하면 최종 상태를 APPROVED로
project/evidence/demo-run-*.json 에 기록해 주세요.
```

### 6) 아키텍처 문서

```
project/docs/architecture.md 에 PRD → Knowledge → MCP →
Agents 4층이 서로 어떻게 이어지는지 mermaid 다이어그램으로
그려 주세요. 각 층의 어떤 파일이 다음 층의 입력이 되는지도
함께 표시해 주세요.
```

### 7) 최종 PRD 완성

```
지금까지 쌓은 산출물(지식, MCP 계약, 에이전트 역할, 승인 게이트)을
반영해서 project/docs/prd.md의 Canvas 1~10 전체를
project/docs/final-prd.md 로 완성해 주세요.
빠진 칸이 있으면 저에게 물어봐 주세요.
```

### 8) 발표 스크립트

```
지금까지 만든 project/ 전체 내용(final-prd, architecture,
integration-map, demo-run)을 바탕으로 5~7분짜리 발표 대본을
"문제 → 구현 → 검증 → 한계" 순서로
project/docs/demo-script.md 에 써 주세요. 심사자가
반박할 만한 지점도 "한계" 섹션에 미리 담아 주세요.
```

### 9) 발표 직전 최종 점검

```
발표 직전에 project/를 한 번 더 점검해 주세요.
- manifest 의 overall_status 가 READY 인지
- demo-data.json, demo-run-*.json, HITL 승인 기록이 있는지
- final-prd.md 의 Canvas 1~10 이 다 채워졌는지
- architecture.md 와 demo-script.md 가 있는지
빠진 것이 있으면 표로 보여 주시고, 다 갖춰졌으면 "발표 가능"이라고
알려 주세요. 결과는 project/evidence/day5-final-check.md 에
저장해 주세요.
```

---

## 실행

1. `cd mx-agentic-ai-day5-final-project` 후 `claude`를 열어요
2. **예제 1)** project/ 조립 프롬프트를 실행해요 → `manifest.json`의 `overall_status: READY`를 확인해요. NOT_READY면 해당 Day로 돌아가 보강한 뒤 1)을 다시 실행해요
3. **예제 2)** 자가 점검 프롬프트를 실행해요
4. E2E에 들어가기 전에 `project/evidence/`에서 가상 테스트를 해도 되는지 강사에게 먼저 확인해요. 승인을 받으면 아래 [테스트 조건]에 따라 진행해요
5. **예제 3)~5)** 데모 데이터 → E2E → HITL 순서로 실행해요
6. **예제 6)~8)** 아키텍처 → final-prd → 발표 대본 순서로 실행해요
7. **예제 9)** 최종 점검을 실행해요
8. 강사에게 최종 승인을 요청하고 5~7분 동안 발표해요

**Day 5 완료 조건**: `manifest.json`이 READY / `demo-run-*.json`에 모든 단계가 근거 ID와 함께 기록됨 / HITL 승인 기록 있음 / `demo-script.md` 완성 / 최종 점검 PASS

Repo skill: `/final-project-assembler` (위 프롬프트와 순서가 같아요)

---

## 테스트 조건 (가상 테스트 — 임시 환경)

| 조건 | 내용 |
|---|---|
| 실행 위치 | 쓰기는 `project/` 안에서만 해요. 실제 사내 시스템이나 운영 DB에는 연결하지 않아요 |
| 데이터 | Day 1 PRD 도메인에 맞춘 합성 데이터만 사용해요. 실제 회사명이나 개인정보는 절대 넣지 않아요 |
| 테스트 범위 | 예제 3~8(데모 데이터 → E2E → HITL → 문서화)을 한 세트로 진행해요 |
| 되돌리기 | 문제가 생기면 `project/`만 지우고 **예제 1)** 조립 프롬프트를 다시 실행해요. Day 1~4 원본은 그대로 남아요 |
| 시간 | 전체 세트를 20분 안에 끝내요. 길어지면 발표 대본은 다음 세션으로 미뤄요 |
| 결과 반영 | 가상 테스트 결과(`demo-run-*.json`)가 승인되면 그대로 발표 자료로 써요 |

---

## 문제 해결

| 상황 | 대응 |
|---|---|
| 레이어를 못 찾거나 NOT_READY가 나와요 | Day 2 `knowledge/`, Day 3 `mcp/*/contract.json`, Day 4 `agents/*.md`의 경로와 개수를 확인한 뒤 예제 1)을 다시 실행해요 |
| 한 번에 복사할 게 너무 많아 헷갈려요 | "knowledge만 먼저"처럼 한 레이어씩 나눠서 요청하세요 |
| 데모 데이터가 PRD 도메인과 안 맞아요 | `project/docs/prd.md`의 배경과 사용자를 다시 읽게 한 뒤 새로 만들어 달라고 하세요 |
| E2E mock이 계약과 안 맞아요 | `project/mcp/[도구명]/contract.json`의 필드명부터 맞추게 하세요 |
| 발표 시간이 넘어가요 | `demo-script.md`에서 "문제 → 구현 → 검증"만 남기고 "한계"는 QA 시간으로 미루세요 |
| 팀원마다 완성도가 달라요 | `manifest.json`의 레이어별 status를 먼저 공유하고, 가장 부족한 Day부터 채우세요 |
