# Day 5 — 최종 프로젝트 통합 및 데모

> 레포 경로: `mx-agentic-ai-day5-final-project/README.md`

**교육 질문**: Day1~4를 내 업무 에이전트로 어떻게 통합하고, 실제로 동작하는 것을 어떻게 증명할까요?

---

## 이론

- Day1~4는 레포 안의 서로 다른 최상위 폴더에 흩어져 있어요. Day5는 새로 만드는 날이 아니라 **그 4개 폴더의 산출물을 모으고, 실행해서, 증명하는 날**이에요.
- 4층 구조: `mx-agentic-ai-day1-prd/(정의)` → `mx-agentic-ai-day2-knowledge-harness/(신뢰)` → `mx-agentic-ai-day3-mcp-tools/(실행)` → `mx-agentic-ai-day4-multi-agent-hitl/(거버넌스)`. `project/` 폴더가 이 4층을 하나로 모아 보여줘요.
- **"검증 PASS ≠ 완성"** — 체크리스트를 통과했어도, 데모 데이터를 흘려보내 처음부터 끝까지 동작하는 모습을 사람이 직접 봐야 완성이에요.
- 오늘 작업은 **Claude Code에 자연어 프롬프트를 붙여넣는 방식**으로 진행해요. Day1~4 원본은 읽기만 하고, 쓰기는 `project/` 안에만 해요.

---

## 사용법

1. 레포 루트에서 `cd mx-agentic-ai-day5-final-project` 후 `claude`를 열어요.
2. 아래 [예제] 프롬프트를 **1번부터 순서대로** 하나씩 붙여넣어요. 대괄호 `[ ]` 안만 자기 상황으로 바꿔요.
3. 단계를 건너뛰거나 몰아서 시키지 않아요 — 뒤 단계는 앞 단계의 `project/` 결과를 참조해요.
4. Day1~4 원본 폴더는 수정하지 않아요. 복사·생성은 `project/`에만 해요.

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
레포 루트(이 폴더의 부모)를 기준으로 Day1~4 산출물을
mx-agentic-ai-day5-final-project/project/ 로 모아 주세요.

규칙:
- Day1~4 원본은 수정·삭제하지 말고, project/에만 복사·생성해요.
- 아래를 복사해요.
  · ../mx-agentic-ai-day2-knowledge-harness/knowledge/ → project/knowledge/
  · ../mx-agentic-ai-day3-mcp-tools/mcp/ → project/mcp/
  · ../mx-agentic-ai-day4-multi-agent-hitl/agents/ → project/agents/
- 아래 지원 파일이 있으면 project/docs/로 복사해요.
  · ../mx-agentic-ai-day1-prd/docs/prd.md → project/docs/prd.md
  · ../CLAUDE.md → project/docs/CLAUDE.md
  · ../mx-agentic-ai-day2-knowledge-harness/relations.json → project/docs/relations.json
  · ../mx-agentic-ai-day2-knowledge-harness/eval-top3.md → project/docs/eval-top3.md
  · ../mx-agentic-ai-day4-multi-agent-hitl/gate-log.md → project/docs/gate-log.md
- project/docs/, project/evidence/ 폴더가 없으면 만들어요.
- project/docs/integration-map.md를 표로 작성해요.
  열: 레이어 | 원본 경로 | 산출물 수 | 기준 | 상태
  기준: knowledge md ≥10, mcp/*/contract.json ≥2, agents/*.md ≥3(README 제외)
- project/manifest.json을 만들어 주세요.
  generated_at, layers(각 레이어 count/required/status/files), overall_status
  overall_status는 세 레이어가 모두 PASS면 READY, 아니면 NOT_READY
- NOT_READY면 어떤 Day 폴더를 보강해야 하는지 나한테 설명해 주세요.
- 이미 project/가 있어도 위 규칙으로 안전하게 덮어써도 돼요.
```

### 2) Day5 자가 점검 (검증 프롬프트)

```
방금 만든 project/를 발표 전에 점검해 주세요. 파이썬 스크립트는
쓰지 말고, 파일을 직접 읽고 판정해 주세요.

확인할 것:
1) project/manifest.json 의 overall_status 가 READY 인가
2) project/knowledge/, mcp/, agents/, docs/, evidence/ 폴더가 있는가
3) project/docs/ 에 integration-map.md 가 있는가
4) 부족한 항목이 있으면 PASS/FAIL 표로 보여주고, 어떤 Day로
   돌아가 무엇을 채우면 되는지만 알려 주세요
5) 결과를 project/evidence/day5-self-check.md 에 요약해 저장해 주세요

근거 없는 값은 UNKNOWN으로 남겨 주세요.
```

### 3) 데모 데이터 생성

```
project/docs/prd.md의 배경/사용자/데이터 섹션을 읽고,
이 도메인에 맞는 합성 데모 데이터를 5~10건 만들어 주세요.
실제 회사명·개인정보는 절대 쓰지 말고, 근거 ID 형식은
project/knowledge/ 에서 쓰던 방식과 통일해 주세요.
project/evidence/demo-data.json으로 저장해 주세요.
```

### 4) E2E 실행 시뮬레이션

```
방금 만든 project/evidence/demo-data.json을 입력으로,
project/agents/planner.md 역할이 계획을 세우고,
project/agents/executor.md 역할이 project/mcp/[도구명]/contract.json에
따라 도구를 호출한다고 가정해서 mock 응답을 만들고,
project/agents/verifier.md 역할이 그 결과를 검증하는 과정을
순서대로 실행해 주세요. 각 단계 결과를 근거 ID와 함께
project/evidence/demo-run-[오늘날짜].json에 기록해 주세요.
근거 없는 값은 만들지 말고 UNKNOWN으로 남겨 주세요.
```

### 5) HITL 게이트 실행

```
검증까지 끝났으면 project/docs/gate-log.md에 정의한 승인
지점에서 멈추고, 내가 승인·반려를 선택할 수 있는 형태로
결과를 보여 주세요. 내가 승인하면 최종 상태를 APPROVED로
project/evidence/demo-run-*.json에 기록해 주세요.
```

### 6) 아키텍처 문서

```
project/docs/architecture.md에 PRD → Knowledge → MCP →
Agents 4층이 서로 어떻게 연결되는지 mermaid 다이어그램으로
그려 주세요. 각 층에서 어떤 파일이 다음 층의 입력이 되는지도
같이 표시해 주세요.
```

### 7) 최종 PRD 완성

```
project/docs/prd.md의 Canvas 1~10 전체를 지금까지 쌓은
산출물(지식, MCP 계약, 에이전트 역할, 승인 게이트)을
반영해서 project/docs/final-prd.md로 완성해 주세요.
빠진 칸이 있으면 나한테 물어봐 주세요.
```

### 8) 발표 스크립트

```
지금까지의 project/ 전체 내용(final-prd, architecture,
integration-map, demo-run)을 바탕으로 5~7분 발표
스크립트를 "문제 → 구현 → 검증 → 한계" 순서로
project/docs/demo-script.md에 작성해 주세요. 심사자가
반박할 만한 지점도 "한계" 섹션에 미리 넣어 주세요.
```

### 9) 발표 직전 최종 점검

```
발표 직전에 project/를 한 번 더 점검해 주세요.
- manifest overall_status READY
- demo-data.json · demo-run-*.json · HITL 승인 기록
- final-prd.md Canvas 1~10
- architecture.md · demo-script.md
빠진 것이 있으면 표로 보여 주고, 있으면 "발표 가능"이라고
알려 주세요. 결과를 project/evidence/day5-final-check.md에
저장해 주세요.
```

---

## 실행

1. `cd mx-agentic-ai-day5-final-project` 후 `claude`를 열어요
2. **예제 1)** project/ 조립 프롬프트를 실행해요 → `manifest.json`의 `overall_status: READY`를 확인해요. NOT_READY면 해당 Day로 돌아가 보강한 뒤 1)을 다시 실행해요
3. **예제 2)** 자가 점검 프롬프트를 실행해요
4. E2E에 들어가기 전에, `project/evidence/`에서 가상 테스트를 진행해도 되는지 나한테 먼저 물어봐 주세요. 승인을 받으면 아래 [테스트 조건]에 따라 진행해요
5. **예제 3)~5)** 데모 데이터 → E2E → HITL 을 순서대로 실행해요
6. **예제 6)~8)** 아키텍처 → final-prd → 발표 스크립트를 실행해요
7. **예제 9)** 최종 점검을 실행해요
8. 강사에게 최종 승인을 요청해요 → 발표해요 (5~7분)

**Day5 완료 조건**: `manifest.json` READY / `demo-run-*.json`에 근거 ID 포함 전 단계 기록 / HITL 승인 기록 존재 / `demo-script.md` 완성 / 최종 점검 PASS

Repo skill: `/final-project-assembler` (위 프롬프트와 동일한 순서)

---

## 테스트 조건 (가상 테스트 — 임시 환경)

| 조건 | 내용 |
|---|---|
| 실행 위치 | 쓰기는 `project/` 안에만 해요. 실제 사내 시스템·운영 DB에는 연결하지 않아요 |
| 데이터 | Day1 PRD 도메인에 맞춘 합성 데이터만 사용해요. 실제 회사명·개인정보는 절대 넣지 않아요 |
| 테스트 범위 | 예제 3~8(데모 데이터 → E2E → HITL → 문서화)을 한 세트로 진행해요 |
| 되돌리기 | 문제가 생기면 `project/`만 지우고 **예제 1)** 조립 프롬프트를 다시 실행해요. Day1~4 원본은 영향받지 않아요 |
| 시간 | 전체 세트를 20분 안에 끝내요. 길어지면 발표 스크립트는 다음 세션으로 미뤄요 |
| 결과 반영 | 가상 테스트 결과(`demo-run-*.json`)가 승인되면 그대로 발표 자료로 사용해요 |

---

## 문제 해결

| 상황 | 대응 |
|---|---|
| 레이어를 못 찾음 / NOT_READY | Day2 `knowledge/`, Day3 `mcp/*/contract.json`, Day4 `agents/*.md` 경로·개수를 확인한 뒤 예제 1)을 다시 실행해요 |
| 복사가 너무 크거나 헷 | 한 레이어씩("knowledge만 먼저") 요청해요 |
| 데모 데이터가 PRD 도메인과 안 맞음 | `project/docs/prd.md`의 배경/사용자를 다시 읽게 하고 재생성을 요청해요 |
| E2E mock이 계약과 안 맞음 | `project/mcp/[도구명]/contract.json` 필드명을 먼저 맞추게 해요 |
| 발표 시간이 넘침 | `demo-script.md`에서 "문제→구현→검증"만 남기고 "한계"는 QA로 미뤄요 |
| 팀원마다 완성도가 다름 | `manifest.json` 레이어별 status를 먼저 공유하고 부족한 Day부터 보강해요 |
