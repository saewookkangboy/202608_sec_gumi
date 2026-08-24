# 참조 PRD · 생산 설비·금형 변경 연계 분석 에이전트

> Day 2~4 공통 실습에서 구현하는 **참조 AI PRD**입니다.  
> Day 1에 팀별로 쓴 PRD와 개념을 하나씩 짝지어 보세요.  
> Canvas 템플릿: [3_AI PRD 가이드](https://adorable-hail-415.notion.site/3_AI-PRD-3c4137efedf680f7a491f3bd50c832c9)

---

## 1. 배경

금형 ECO(설계변경) 이력과 설비 가동 로그, 품질 결함 데이터가 서로 다른 시스템과 문서에 흩어져 있습니다. 설비에 이상이 생겼을 때 "어떤 ECO 변경과 관련이 있을까"를 사람이 직접 찾으려면 30분이 넘게 걸리고, 근거 없는 추측 때문에 정비 우선순위가 잘못 정해질 위험도 있습니다.

## 2. 목표

| 우선순위 | 목표 | 측정 |
|---|---|---|
| 시간 | 연관 분석 초안을 쓰는 시간 | **30분 → 5분** |
| 품질 | 근거 ID가 붙은 초안 | 고치지 않고 바로 검토할 수 있는 수준 |
| 리스크 | 추측과 환각 막기 | 누락·불확실 항목을 빠짐없이 표시 |

**MVP 한 문장:** 합성 ECO와 설비 로그, 품질 데이터를 넣으면 근거 ID가 붙은 정비 연관 분석 초안을 만들어 주는 **교육용 분석 에이전트**입니다.

## 3. 사용자

| 역할 | 하는 일 |
|---|---|
| 주 사용자 | 생산기술·품질 담당자 — 분석 초안을 요청합니다 |
| 검토자 | 같은 팀 동료 — 근거와 수치를 확인합니다 |
| 승인자 | 파트장 — 최종 정비 우선순위를 확정합니다 |

## 4. 업무 흐름

```text
As-Is:  ECO 문서 검색 → 설비 로그 조회 → 품질 시트 확인 → 수동 연결 (30분+)

To-Be:  [ECO + 로그 + 품질 입력]
           → AI 분석 초안 (근거 ID 포함)
           → 사람 검토 (Verifier PASS)
           → 승인자 최종 확정
           → (선택) 보고서 저장
```

## 5. AI 역할

**할 일:**
- ECO 지식에서 부품·설비·도면 정보를 찾습니다
- 설비 로그에서 기간별 오류 코드를 집계합니다
- 품질 결함을 설비와 조인해 불량률을 계산합니다
- 위 결과를 엮어 분석 초안을 씁니다

**✕ 하면 안 되는 일:**
- 실제 설비를 멈추거나 MES 명령을 실행하는 일
- 원본 데이터(`data/raw/`, `data/`, `fixtures/`)를 고치는 일
- 문서에 없는 값을 추측하거나 채워 넣는 일 (`UNKNOWN`으로 남깁니다)
- 검증 PASS를 사람 승인으로 여기는 일
- `APPROVE_WRITE`나 `--approve` 없이 파일을 저장하거나 최종 확정하는 일

**사람이 계속 맡는 일:** 최종 우선순위 확정, 민감 데이터 제공, 승인·반려 결정

## 6. 데이터 / 컨텍스트

| 소스 | 위치 | 항목 | 권한 |
|---|---|---|---|
| ECO 원본 | `day2/data/raw/eco_documents.jsonl` | part_id, equipment, drawing, reason | 읽기 전용 |
| ECO 지식 | `day2/knowledge/eco/*.md` | 정규화 결과와 `source_id` | 생성만 (`knowledge/`) |
| 설비 로그 | `day3/data/equipment_logs.csv` | equipment_id, error_code, timestamp | 읽기 전용 |
| 품질 요약 | `day4/fixtures/quality_summary.json` | defect_rate, equipment_id | 읽기 전용 |
| 오류 fixture | `day4/fixtures/equipment_errors.json` | error_count, LOG-* | 읽기 전용 |

**민감도:** 실제 사업장 정보나 개인정보는 들어 있지 않고, 교육용 합성 데이터만 씁니다. 경로와 clone 확인 방법은 [`dummy-data.md`](./dummy-data.md)에 있습니다.

**누락 시 규칙:**
- 필드가 없으면 → `UNKNOWN`으로 두고 채우지 않습니다
- 조인에 실패하면 → 빈 결과와 구조화 오류를 돌려줍니다
- 근거 없는 수치는 → `[확인 필요]`로 표시하거나 검증에서 REJECT 합니다

## 7. 출력 명세

**형식:** 분석 초안 (Markdown 또는 JSON)

```text
1. 요약 (1문단)
2. 관련 ECO 목록 (source_id + source_path)
3. 설비 오류 집계 (equipment_id + evidence_id)
4. 품질 결함 연결 (QUALITY-* ID)
5. 불확실·누락 항목 목록
6. 면책: "합성 데이터 기반 교육 결과이며 실제 정비 지시가 아님"
```

**근거:** 모든 수치와 목록에 `ECO-*`, `LOG-*`, `QUALITY-*` ID를 반드시 붙입니다.

**Fallback:** 확신이 서지 않으면 추측하지 말고 `UNKNOWN`이나 `[확인 필요]`로 표시합니다.

## 8. 평가 기준 → Day 2에서 구현

| 항목 | 방법 | PASS 조건 |
|---|---|---|
| 지식 정규화 | `normalize_docs.py` | ECO 12건에 `source_id`와 `source_path`가 모두 있을 것 |
| 원본 보호 | `raw.sha256` | 작업 전후 해시가 같을 것 |
| 검색 품질 | `eval/questions.jsonl` | 정답 문서가 Top-3 안에 들 것 |
| 회귀 | `unittest`와 `validate_repo.py` | 테스트 3건 모두 PASS |

**Day 1에 적어 둔 "아직 모르는 것"이 이렇게 채워집니다:**
- ~~반복 검증 방법~~ → Top-3 eval과 harness로 해결
- ~~실패 유형 분류~~ → UNKNOWN 유지, 조인 실패, Top-3 미달로 정리

## 9. 안전 / 거버넌스 → Day 4에서 구현

| 항목 | 구현 |
|---|---|
| 승인 게이트 | `VERIFIED` 다음에 `AWAITING_APPROVAL`로 멈추고, `--approve`가 있을 때만 `APPROVED` |
| 쓰기 게이트 (Day 3) | `APPROVE_WRITE`가 없으면 dry-run |
| 활동 로그 | `runs/<run-id>/events.jsonl`에 기록 |
| 역할 분리 | Planner / Executor / Verifier / Human 스킬로 분리 |
| 이관 | 같은 결함이 3번 반복되면 `ESCALATED` |

**Day 1에 적어 둔 "아직 모르는 것"이 이렇게 채워집니다:**
- ~~승인 게이트 위치~~ → Verifier가 PASS한 직후, Human 스킬 바로 앞
- ~~활동 로그~~ → `events.jsonl`에 상태 전이를 기록

## 10. 운영 지표 → Day 4에서 연결

| 지표 | 정의 | 교육용 측정 |
|---|---|---|
| 시간 절감 | 분석 초안을 쓰는 시간 | 30분 → 5분 (Day 1 목표와 같습니다) |
| 품질 | 근거 누락률 | 결함 주입 테스트 통과율로 측정 |
| 안전 | 무단 쓰기 시도 | dry-run 100%, 승인 없는 저장 0건 |
| 이관 | 반복 실패 | 같은 결함 3회 → ESCALATED |

**ROI:** 교육 환경에서는 합성 데이터를 기준으로만 이야기합니다. 실제로 도입할 때 드는 API·인프라 비용은 따로 계산해야 합니다.

---

## Day 2~4 구현 매핑 요약

| PRD 섹션 | Day | 저장소 증거 |
|---|---|---|
| 6 데이터·지식 | 2 | `knowledge/eco/`, `catalog.json` |
| 8 평가 | 2 | `eval/`, `tests/`, `validate_repo.py` |
| 5·6 도구화 | 3 | `src/server.mjs`의 MCP 도구 3개 |
| 8 E2E | 3 | `npm run smoke` |
| 9 거버넌스 | 4 | HITL 상태 머신과 `--approve` |
| 10 운영 | 4 | `events.jsonl`, ESCALATED |

→ [5일 커리큘럼](./curriculum-5day.md) · [Day 5 최종 프로젝트](../mx-agentic-ai-day5-final-project/README.md)

---

## Day 5 · 최종 프로젝트 (통합)

| PRD 섹션 | Day 5 산출물 |
|---|---|
| 1~7 (Day 1) | `project/docs/final-prd.md` |
| 8 평가 | `project/knowledge/` + evidence |
| 9·10 거버넌스·운영 | `project/agents/hitl-policy.md` |
| 아키텍처 | `project/docs/architecture.md` |
| 발표 | `project/docs/demo-script.md` |

4대 기술 기둥은 [tech-pillars.md](./tech-pillars.md)에 정리돼 있습니다.
