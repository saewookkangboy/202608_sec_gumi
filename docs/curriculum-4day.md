> Day 1~4만 다루는 예전 버전입니다. Day 5까지 포함한 전체 과정은 [`curriculum-5day.md`](./curriculum-5day.md)와 [`tech-pillars.md`](./tech-pillars.md)에 있습니다.

# 삼성 MX 구미 · 에이전틱 AI 4일 커리큘럼 (Day 5 미포함)

> **AI PRD Canvas 10칸**을 뼈대로 Day 1은 정의, Day 2는 평가와 지식, Day 3은 도구와 루프, Day 4는 거버넌스와 운영을 차례로 다룹니다.  
> 자세한 가이드는 [3_AI PRD 가이드 (Notion)](https://adorable-hail-415.notion.site/3_AI-PRD-3c4137efedf680f7a491f3bd50c832c9)에 있습니다.

---

## 4일 흐름

```text
Day 1  PRD 정의          "무엇을, 어떻게 일하게 할까요?"
  │    (Canvas 1~7)       → docs/prd.md · sample-data · expected-output
  ▼
Day 2  지식·평가         "데이터를 어떻게 믿고 측정할까요?"  ← Canvas 8
  │    (Harness·Eval)   → source_id · Top-3 eval · 하네스
  ▼
Day 3  도구·루프         "AI가 실제로 무엇에 접근할까요?"    ← Canvas 5·6 구현
  │    (MCP·E2E)        → 읽기/쓰기 분리 · evidence_id · smoke
  ▼
Day 4  통제·운영         "언제 멈추고, 누가 승인할까요?"    ← Canvas 9·10
       (HITL·HOTL)      → AWAITING_APPROVAL · ESCALATED · events
```

| 일차 | PRD Canvas | 교육 질문 | 실습 저장소 | 산출물 |
|---|---|---|---|---|
| **Day 1** | 1~7 (+ 8·9·10 예약) | AI를 어떻게 일하게 할까요? | `mx-agentic-ai-day1-prd/` | `docs/prd.md`, `docs/prd.pdf`, `sample-data/`, `expected-output/` |
| **Day 2** | **8** 평가 기준 | 답이 맞는지 어떻게 반복해서 확인할까요? | `mx-agentic-ai-day2-knowledge-harness/` | 지식 자산 12건, Top-3 eval, 하네스 검증 |
| **Day 3** | **5·6** 역할·데이터 (도구화) | AI가 어떤 도구로 데이터에 닿을까요? | `mx-agentic-ai-day3-mcp-tools/` | MCP 도구 3개, smoke E2E, 승인 없는 쓰기 차단 |
| **Day 4** | **9·10** 안전·운영 | 누가 최종 승인하고, 어떻게 운영할까요? | `mx-agentic-ai-day4-multi-agent-hitl/` | 역할 분리, HITL 정지, HOTL 이관, 이벤트 로그 |

---

## AI PRD Canvas 10칸 × 4일 매핑

| # | Canvas 항목 | Day 1 | Day 2 | Day 3 | Day 4 |
|---|---|:---:|:---:|:---:|:---:|
| 1 | 배경 | ✅ 기획서 이관 | — | — | — |
| 2 | 목표 (측정 가능) | ✅ | eval로 검증 | smoke로 계약 검증 | 운영 지표 연결 |
| 3 | 사용자 | ✅ | — | — | 승인자·검토자 |
| 4 | 업무 흐름 | ✅ | ingest→검색 | 조회→집계→보고 | Plan→Execute→Verify→Approve |
| 5 | AI 역할 + **하면 안 되는 일** | 🔥 정의 | 하네스로 고정 | MCP 도구로 구현 | 역할 스킬로 분리 |
| 6 | 데이터·컨텍스트 + **누락 시 규칙** | 🔥 정의 | `source_id`·`UNKNOWN` | `data/` 불변·`evidence_id` | `fixtures/`·조인 검증 |
| 7 | 출력 명세 + **fallback** | 🔥 정의 | Top-3 + 근거 경로 | 구조화 오류·dry-run | `verification.json`·승인 패킷 |
| 8 | 평가 기준 | 🔒 예약 메모 | **🔥 실습** | 단위·smoke 테스트 | 결함 주입 테스트 |
| 9 | 안전·거버넌스 | 🔒 예약 메모 | 원본 잠금 | `APPROVE_WRITE` | `AWAITING_APPROVAL`·`--approve` |
| 10 | 운영 지표 | 🔒 예약 메모 | `progress.md`·해시 | `events`·stderr 로그 | `events.jsonl`·`ESCALATED` |

**Day 1 원칙:** 8·9·10은 비워 두고 *"지금 아는 것 / 아직 모르는 것"*만 적습니다. 완벽한 PRD보다, **무엇을 아직 모르는지**가 드러나는 PRD가 훨씬 쓸모 있습니다.

---

## 공통 시나리오: "생산 설비·금형 변경 연계 분석"

Day 2~4는 **같은 합성 제조 시나리오**로 기술을 익힙니다. 팀별 Day 1 PRD(예: 견적요청 초안봇)와 개념을 하나씩 짝지어 보면 됩니다.

```text
[Day 2 지식]  ECO-001..012  ──equipment──▶  PRESS-01, PRESS-03, MILL-02
       │                                              │
       │  part_id · drawing · UNKNOWN 규칙            │  LOG-* evidence
       ▼                                              ▼
[Day 3 MCP]   knowledge/catalog.json          equipment_logs.csv
       │         (읽기 전용 지식)                    (조회·집계 도구)
       └──────────────────┬──────────────────────────┘
                          ▼
[Day 4 HITL]   설비 오류 + 품질 결함 연관 분석 → 검증 PASS → 사람 승인 대기
```

참조 PRD 전문은 [`reference-prd.md`](./reference-prd.md)에서 볼 수 있습니다.

| Day 1 (팀 PRD) | Day 2~4 (참조 구현) |
|---|---|
| `sample-data/`의 가상 입력 | `data/raw/eco_documents.jsonl`, `data/equipment_logs.csv` |
| `expected-output/`의 목표 출력 | `eval/questions.jsonl`의 정답, `outputs/`의 보고서 |
| "[확인 필요]" fallback | `UNKNOWN`, 구조화 오류, dry-run |
| 하면 안 되는 일 (발송·추측) | 원본 수정 금지, 승인 없는 쓰기 금지 |
| 8번 "아직 모르는 것" | Top-3 eval, smoke, 결함 주입으로 채웁니다 |
| 9·10번 "아직 모르는 것" | HITL 게이트, `events.jsonl`, 이관 규칙으로 채웁니다 |

---

## 일차별 상세

### Day 1 · AI PRD 정의 (약 35~45분)

**목표:** 오전 기획서를 AI가 그대로 실행할 수 있는 PRD로 옮깁니다.

| 단계 | 내용 | 시간 |
|---|---|---|
| STEP 1 | `mx-agentic-ai-day1-prd/`를 열고 복사용 프롬프트 실행하기 | 2분 |
| STEP 2 | Canvas 1~4에 기획서가 잘 옮겨졌는지 확인하기 | 2분 |
| STEP 3 | **5·6·7 인터뷰** — AI 역할, 데이터, 출력 정하기 | 15분 |
| STEP 4 | 8·9·10 예약석 채우기 (아는 것 / 모르는 것) | 3분 |
| STEP 5 | AI 자가 점검 8항목 확인하기 | 5분 |
| STEP 6 | `docs/prd.md`, `docs/prd.pdf`, 샘플 파일 만들고 제출하기 | 10분 |

**완료 체크:**
- 5번에 "하면 안 되는 일"이 2개 이상 (발송·삭제·승인·숫자 임의 수정 등)
- 6번에 누락 시 규칙 (`[확인 필요]` / `UNKNOWN`)
- 7번에 출력 구조와 fallback
- `sample-data/`와 `expected-output/` 생성

→ [Day 1 README](../mx-agentic-ai-day1-prd/README.md) · [Notion 가이드](https://adorable-hail-415.notion.site/3_AI-PRD-3c4137efedf680f7a491f3bd50c832c9)

---

### Day 2 · 지식 자산화와 평가 (Canvas 8)

**교육 질문:** "PRD 6번 데이터를 AI가 믿을 수 있는 지식으로 만들고, 8번 평가로 품질을 언제든 다시 잴 수 있게 하려면 어떻게 해야 할까요?"

| PRD 항목 | 실습 매핑 |
|---|---|
| 6 데이터·컨텍스트 | `data/raw/eco_documents.jsonl` → `knowledge/eco/*.md` |
| 누락 시 규칙 | `drawing: UNKNOWN`, `equipment: UNKNOWN`을 그대로 둡니다 |
| 7 출력·근거 | 모든 답에 `source_id`와 `source_path`를 붙입니다 |
| **8 평가 기준** | `eval/questions.jsonl` Top-3, `validate_repo.py`, unittest |

**Day 1 되돌아보기 (10분):** 팀 PRD 8번을 아래 형식으로 채워 넣습니다.

```text
평가 기준 (Day 2 완료 후)
- PASS: [expected-output과 일치하는 조건]
- FAIL 유형: [근거 누락 / 환각 / 형식 오류 / 누락 필드 미표시]
- 회귀: [고정 샘플 N건, 재실행 시 동일 결과]
```

```bash
cd mx-agentic-ai-day2-knowledge-harness
python3 scripts/validate_repo.py && python3 -m unittest discover -s tests -v
```

→ [Day 2 README](../mx-agentic-ai-day2-knowledge-harness/README.md)

---

### Day 3 · MCP 도구와 실행 루프 (Canvas 5·6 구현)

**교육 질문:** "PRD 5번 AI 역할을 도구 계약으로 쪼개고, 6번 데이터 접근을 안전한 MCP로 연결하려면 어떻게 해야 할까요?"

| PRD 항목 | 실습 매핑 |
|---|---|
| 5 AI 역할 (조회) | `list_equipment_logs`, `get_equipment_errors` |
| 5 하면 안 되는 일 (무단 쓰기) | `write_analysis_report`를 dry-run으로 처리 |
| 6 데이터 권한 | `data/`는 읽기 전용, 쓰기는 `outputs/`에만 |
| 7 evidence | `evidence_id`는 `LOG-*` |
| 8 E2E 평가 | `npm test`와 `npm run smoke` |

**시나리오 연결:** Day 2 ECO의 `equipment` 필드(`PRESS-01` 등)가 Day 3 설비 ID와 이어지는 조인 키입니다.

**Day 1 되돌아보기:** 팀 PRD에 "필요한 도구 목록" 초안을 덧붙입니다 (읽기 도구 몇 개, 쓰기 도구 1개, 승인 토큰).

```bash
cd mx-agentic-ai-day3-mcp-tools
npm test && npm run smoke
```

→ [Day 3 README](../mx-agentic-ai-day3-mcp-tools/README.md)

---

### Day 4 · 멀티 에이전트와 HITL/HOTL (Canvas 9·10)

**교육 질문:** "PRD 9번 승인 게이트를 어디에 두고, 10번 운영 지표는 어떻게 남길까요?"

| PRD 항목 | 실습 매핑 |
|---|---|
| 9 승인 게이트 | `VERIFIED`는 `APPROVED`가 아니며, `--approve` 전에는 멈춥니다 |
| 9 활동 로그 | `runs/<id>/events.jsonl`에 기록 |
| 10 이관·임계치 | 같은 결함이 3번 반복되면 `ESCALATED` (HOTL) |
| 5 역할 분리 | Planner / Executor / Verifier / Human |
| 2 목표 측정 | 분석 초안을 쓰는 시간 단축 (교육용 합성 지표) |

**파이프라인:** Day 3 MCP(설비 로그)와 Day 4 fixtures(품질) → 연관 분석 → 검증 → **사람 승인 대기**

**Day 1 되돌아보기:** 팀 PRD 9·10번을 채웁니다.

```text
9 안전·거버넌스
- 승인 게이트: [최종 발송/실행 직전]
- 로그: [누가·언제·무엇을 승인/반려했는지]

10 운영 지표
- 성공: [30분→5분 등 Day 1 목표와 동일 지표]
- 비용·ROI: [측정 방법 초안]
```

```bash
cd mx-agentic-ai-day4-multi-agent-hitl
npm test && npm run demo && npm run demo:approve
```

→ [Day 4 README](../mx-agentic-ai-day4-multi-agent-hitl/README.md)

---

## 4일이 공유하는 5가지 계약

1. **원본은 건드리지 않는다** — Day 2 `data/raw/`, Day 3 `data/`, Day 4 `fixtures/`
2. **없는 값은 추측하지 않는다** — `[확인 필요]`, `UNKNOWN`, 빈 집계로 남긴다
3. **근거 ID가 없으면 결과가 아니다** — `ECO-*`, `LOG-*`, `QUALITY-*`
4. **검증 PASS는 사람 승인이 아니다** — dry-run, `AWAITING_APPROVAL`
5. **되돌릴 수 없는 행동은 토큰과 플래그로 막는다** — `APPROVE_WRITE`, `--approve`

---

## 강사용 타임라인 (1일 8시간 기준)

| 시간 | Day 1 | Day 2 | Day 3 | Day 4 |
|---|---|---|---|---|
| 오전 1 | 기획서 워크숍 | Harness 개념 + ECO 실습 | MCP 개념 + 도구 계약 | 역할·상태 머신 |
| 오전 2 | **PRD Canvas (1~7)** | 정규화·검색 실습 | smoke E2E | 결함 주입 데모 |
| 오후 1 | 자가 점검·제출 | eval + 하네스 감사 | 팀 MCP 시나리오 | 4종 종료 경로 |
| 오후 2 | Day 2 예고 | **PRD 8번 회고** | **PRD 도구 목록 회고** | **PRD 9·10 완성** |

---

## 저장소 구조

```text
202608_sec_gumi/
├── docs/
│   ├── curriculum-4day.md          ← 이 문서
│   ├── reference-prd.md            ← Day 2~4 참조 PRD
│   └── github-deployment-and-quickstart.md
├── mx-agentic-ai-day1-prd/        ← Day 1 PRD 실습
├── mx-agentic-ai-day2-knowledge-harness/
├── mx-agentic-ai-day3-mcp-tools/
└── mx-agentic-ai-day4-multi-agent-hitl/
```

---

## 참고 링크

- [3_AI PRD 가이드 (Notion)](https://adorable-hail-415.notion.site/3_AI-PRD-3c4137efedf680f7a491f3bd50c832c9)
- [GitHub 배포·코드복사 가이드](./github-deployment-and-quickstart.md)
- [skill·기술 참고 목차](./README.md)
