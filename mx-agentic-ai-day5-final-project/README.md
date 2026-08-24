# Day 5 — 최종 프로젝트 통합 및 데모

> 레포 경로: `mx-agentic-ai-day5-final-project/README.md`
> 스크립트: `mx-agentic-ai-day5-final-project/scripts/assemble_project.py`

**교육 질문**: Day1~4를 내 업무 에이전트로 어떻게 통합하고, 실제로 동작하는 것을 어떻게 증명할까요?

---

## 이론

- Day1~4는 레포 안의 서로 다른 최상위 폴더에 흩어져 있어요. Day5는 새로 만드는 날이 아니라 **그 4개 폴더의 산출물을 모으고, 실행해서, 증명하는 날**이에요.
- 4층 구조: `mx-agentic-ai-day1-prd/(정의)` → `mx-agentic-ai-day2-knowledge-harness/(신뢰)` → `mx-agentic-ai-day3-mcp-tools/(실행)` → `mx-agentic-ai-day4-multi-agent-hitl/(거버넌스)`. `project/` 폴더가 이 4층을 하나로 모아 보여줘요.
- **"검증 PASS ≠ 완성"** — 각 Day의 자동 체크리스트를 통과했어도, 실제로 데모 데이터를 흘려보내서 처음부터 끝까지 동작하는 모습을 사람이 직접 봐야 완성이에요.

---

## 사용법

1. `cd mx-agentic-ai-day5-final-project` 후 `python3 scripts/assemble_project.py`를 실행해서 `project/` 폴더를 만들어요. 레포 루트는 스크립트 위치 기준으로 자동 계산되니 별도 인자는 필요 없어요.
2. 이후 [예제] 섹션의 프롬프트를 순서대로 Claude Code에 붙여넣어 **데모 데이터 생성 → E2E 실행 → 발표 스크립트 작성**까지 진행해요.
3. 스크립트는 Day1~4 원본 파일을 건드리지 않고 `project/`에만 복사·생성해요 — 몇 번을 다시 실행해도 안전해요.

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
    ├── scripts/
    │   └── assemble_project.py
    └── project/                        # 오늘 생성되는 발표 패키지
        ├── manifest.json
        ├── docs/
        │   ├── prd.md · CLAUDE.md · relations.json · eval-top3.md · gate-log.md   # Day1~4에서 복사
        │   ├── final-prd.md
        │   ├── architecture.md
        │   ├── integration-map.md      # 스크립트가 자동 생성
        │   └── demo-script.md
        ├── evidence/
        │   ├── demo-data.json
        │   └── demo-run-[날짜].json
        ├── knowledge/  (복사본)
        ├── mcp/        (복사본)
        └── agents/     (복사본)
```

---

## 예제

### 1) project/ 생성
```bash
cd mx-agentic-ai-day5-final-project
python3 scripts/assemble_project.py
```
`project/manifest.json`의 `overall_status`가 `READY`가 아니면, 어떤 레이어가 부족한지 콘솔 출력에 나와요. 그 Day 폴더로 돌아가 보강한 뒤 다시 실행해요 — 안전하게 덮어써요.

### 2) 데모 데이터 생성 (그대로 붙여넣기)
```
project/docs/prd.md의 배경/사용자/데이터 섹션을 읽고,
이 도메인에 맞는 합성 데모 데이터를 5~10건 만들어 주세요.
실제 회사명·개인정보는 절대 쓰지 말고, 근거 ID 형식은
project/knowledge/*.md에서 쓰던 방식과 통일해 주세요.
project/evidence/demo-data.json으로 저장해 주세요.
```

### 3) E2E 실행 시뮬레이션 (그대로 붙여넣기)
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

### 4) HITL 게이트 실행 (그대로 붙여넣기)
```
검증까지 끝났으면 project/docs/gate-log.md에 정의한 승인
지점에서 멈추고, 내가 승인·반려를 선택할 수 있는 형태로
결과를 보여 주세요. 내가 승인하면 최종 상태를 APPROVED로
project/evidence/demo-run-*.json에 기록해 주세요.
```

### 5) 아키텍처 문서 (그대로 붙여넣기)
```
project/docs/architecture.md에 PRD → Knowledge → MCP →
Agents 4층이 서로 어떻게 연결되는지 mermaid 다이어그램으로
그려 주세요. 각 층에서 어떤 파일이 다음 층의 입력이 되는지도
같이 표시해 주세요.
```

### 6) 최종 PRD 완성 (그대로 붙여넣기)
```
project/docs/prd.md의 Canvas 1~10 전체를 지금까지 쌓은
산출물(지식, MCP 계약, 에이전트 역할, 승인 게이트)을
반영해서 project/docs/final-prd.md로 완성해 주세요.
빠진 칸이 있으면 나한테 물어봐 주세요.
```

### 7) 발표 스크립트 (그대로 붙여넣기)
```
지금까지의 project/ 전체 내용(final-prd, architecture,
integration-map, demo-run)을 바탕으로 5~7분 발표
스크립트를 "문제 → 구현 → 검증 → 한계" 순서로
project/docs/demo-script.md에 작성해 주세요. 심사자가
반박할 만한 지점도 "한계" 섹션에 미리 넣어 주세요.
```

---

## 실행

1. `python3 scripts/assemble_project.py`를 실행하고, `project/manifest.json`에서 `overall_status: READY`를 확인해요
2. E2E 실행에 들어가기 전에, 임시 환경(`project/evidence/`)에서 가상 테스트를 진행해도 되는지 나한테 먼저 물어봐 주세요. 승인을 받으면 아래 [테스트 조건]에 따라 3~7단계를 진행해요
3. 데모 데이터 생성 프롬프트를 실행해요 → `project/evidence/demo-data.json`을 확인해요
4. E2E 실행 프롬프트를 실행해요 → Planner → Executor(mcp 호출, mock) → Verifier 순서로 `demo-run-*.json` 생성을 확인해요
5. HITL 게이트 프롬프트를 실행해요 → 승인/반려를 선택하고, 최종 상태 기록을 확인해요
6. 아키텍처 문서 프롬프트를 실행해요
7. 최종 PRD 프롬프트를 실행해요 → `final-prd.md` Canvas 1~10이 모두 채워졌는지 확인해요
8. 발표 스크립트 프롬프트를 실행해요
9. 강사에게 최종 승인을 요청해요 → 발표해요 (5~7분)

**Day5 완료 조건**: `manifest.json` READY / `demo-run-*.json`에 근거 ID 포함 전 단계 기록 / HITL 승인 기록 존재 / `demo-script.md` 완성

---

## 테스트 조건 (가상 테스트 — 임시 환경)

| 조건 | 내용 |
|---|---|
| 실행 위치 | `project/evidence/` 안에만 결과를 남겨요. 실제 사내 시스템·운영 데이터베이스에는 어떤 것도 연결하지 않아요 |
| 데이터 | Day1 PRD 도메인에 맞춘 합성 데이터만 사용해요. 실제 회사명·개인정보는 절대 넣지 않아요 |
| 테스트 범위 | 3~7단계(데모 데이터 생성 → E2E 실행 → HITL 게이트 → 문서화)를 한 세트로 진행해요 |
| 되돌리기 | 문제가 생기면 `project/`만 삭제하고 `assemble_project.py`를 다시 실행하면 재생성돼요. Day1~4 원본은 영향받지 않아요 |
| 시간 | 전체 세트를 20분 안에 끝내요. 길어지면 발표 스크립트는 다음 세션으로 미뤄요 |
| 결과 반영 | 가상 테스트 결과(`demo-run-*.json`)가 승인되면 그대로 발표 자료로 사용해요 |

---

## 문제 해결

| 상황 | 대응 |
|---|---|
| `assemble_project.py`가 레이어를 못 찾음 | Day2~4 폴더(`mx-agentic-ai-day2-knowledge-harness/knowledge`, `mx-agentic-ai-day3-mcp-tools/mcp`, `mx-agentic-ai-day4-multi-agent-hitl/agents`)가 스크립트 기준 경로와 정확히 일치하는지 확인해요 |
| 레포를 다른 위치로 옮겨서 경로가 안 맞음 | `python3 scripts/assemble_project.py --repo-root [실제 레포 루트 경로]`로 직접 지정해요 |
| 데모 데이터가 PRD 도메인과 안 맞음 | `project/docs/prd.md`의 "배경/사용자" 섹션을 다시 읽게 하고 재생성을 요청해요 |
| E2E 실행 중 mock 응답이 계약과 안 맞음 | Day3 `mcp/[도구명]/contract.json`을 먼저 열어 필드명을 맞추게 해요 |
| 발표 시간이 넘침 | `demo-script.md`에서 "문제→구현→검증" 3단만 남기고 "한계"는 QA 시간으로 이동해요 |
| 팀원마다 산출물 완성도가 다름 | `manifest.json`의 레이어별 status를 팀 회의에서 먼저 공유하고 부족한 레이어부터 보강해요 |
