# 참조 PRD · 생산 설비·금형 변경 연계 분석 에이전트

> Day 2~4 공통 실습이 구현하는 **참조 AI PRD**입니다.  
> Day 1에서 팀별로 작성한 PRD와 개념을 1:1로 대응해 보세요.  
> Canvas 템플릿: [3_AI PRD 가이드](https://adorable-hail-415.notion.site/3_AI-PRD-3c4137efedf680f7a491f3bd50c832c9)

---

## 1. 배경

금형 ECO(설계변경) 이력, 설비 가동 로그, 품질 결함 데이터가 각각 다른 시스템·문서에 분산되어 있습니다. 설비 이상 발생 시 "어떤 ECO 변경과 연관될 수 있는지"를 사람이 수동으로 찾는 데 30분 이상 소요되며, 근거 없는 추측으로 잘못된 정비 우선순위가 정해질 위험이 있습니다.

## 2. 목표

| 우선순위 | 목표 | 측정 |
|---|---|---|
| 시간 | 연관 분석 초안 작성 | **30분 → 5분** |
| 품질 | 근거 ID가 붙은 초안 | 수정 없이 검토 가능한 수준 |
| 리스크 | 추측·환각 방지 | 누락·불확실 항목 명시적 표기 |

**MVP 한 문장:** 합성 ECO·설비 로그·품질 데이터를 넣으면, 근거 ID가 포함된 정비 연관 분석 초안이 나오는 **교육용 분석 에이전트**.

## 3. 사용자

| 역할 | 하는 일 |
|---|---|
| 주 사용자 | 생산기술·품질 담당 (분석 초안 요청) |
| 검토자 | 동일 팀 동료 (근거·수치 확인) |
| 승인자 | 파트장 (최종 정비 우선순위 확정) |

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
- ECO 지식에서 부품·설비·도면 정보 검색
- 설비 로그에서 기간별 오류 코드 집계
- 품질 결함과 설비 조인 후 불량률 계산
- 위 결과를 연결한 분석 초안 작성

**✕ 하면 안 되는 일:**
- 실제 설비 정지·MES 명령 실행
- 원본 데이터(`data/raw/`, `data/`, `fixtures/`) 수정
- 문서에 없는 값 추측·보간 (`UNKNOWN` 유지)
- 검증 PASS를 사람 승인으로 간주
- `APPROVE_WRITE` / `--approve` 없이 파일 저장·최종 확정

**사람이 계속 하는 일:** 최종 우선순위 확정, 민감 데이터 제공, 승인·반려 결정

## 6. 데이터 / 컨텍스트

| 소스 | 위치 | 항목 | 권한 |
|---|---|---|---|
| ECO 원본 | `day2/data/raw/eco_documents.jsonl` | part_id, equipment, drawing, reason | 읽기 전용 |
| ECO 지식 | `day2/knowledge/eco/*.md` | 정규화 + `source_id` | 생성만 (`knowledge/`) |
| 설비 로그 | `day3/data/equipment_logs.csv` | equipment_id, error_code, timestamp | 읽기 전용 |
| 품질 요약 | `day4/fixtures/quality_summary.json` | defect_rate, equipment_id | 읽기 전용 |
| 오류 fixture | `day4/fixtures/equipment_errors.json` | error_count, LOG-* | 읽기 전용 |

**민감도:** 실제 사업장·개인정보 없음. 교육용 합성 데이터만 사용. 경로·clone 확인: [`dummy-data.md`](./dummy-data.md)

**누락 시 규칙:**
- 필드 없음 → `UNKNOWN` (채우지 않음)
- 조인 실패 → 빈 결과 + 구조화 오류
- 근거 없는 수치 → `[확인 필요]` / 검증 REJECT

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

**근거:** 모든 수치·목록에 `ECO-*`, `LOG-*`, `QUALITY-*` ID 필수.

**Fallback:** 확신 없으면 추측하지 않고 `UNKNOWN` 또는 `[확인 필요]` 표기.

## 8. 평가 기준 → Day 2에서 구현

| 항목 | 방법 | PASS 조건 |
|---|---|---|
| 지식 정규화 | `normalize_docs.py` | ECO 12건, `source_id`·`source_path` 존재 |
| 원본 보호 | `raw.sha256` | 작업 전후 해시 동일 |
| 검색 품질 | `eval/questions.jsonl` | 정답 문서 Top-3 포함 |
| 회귀 | `unittest` + `validate_repo.py` | 3 tests PASS |

**Day 1에서 적었던 "아직 모르는 것" 예시:**
- ~~반복 검증 방법~~ → Top-3 eval + harness
- ~~실패 유형 분류~~ → UNKNOWN 유지, 조인 실패, Top-3 미달

## 9. 안전 / 거버넌스 → Day 4에서 구현

| 항목 | 구현 |
|---|---|
| 승인 게이트 | `VERIFIED` 후 `AWAITING_APPROVAL`, `--approve`만 `APPROVED` |
| 쓰기 게이트 (Day 3) | `APPROVE_WRITE` 없으면 dry-run |
| 활동 로그 | `runs/<run-id>/events.jsonl` |
| 역할 분리 | Planner / Executor / Verifier / Human 스킬 |
| 이관 | 동일 결함 3회 → `ESCALATED` |

**Day 1에서 적었던 "아직 모르는 것" 예시:**
- ~~승인 게이트 위치~~ → Verifier PASS 직후, Human 스킬 직전
- ~~활동 로그~~ → `events.jsonl` 상태 전이 기록

## 10. 운영 지표 → Day 4에서 연결

| 지표 | 정의 | 교육용 측정 |
|---|---|---|
| 시간 절감 | 분석 초안 작성 | 30분 → 5분 (Day 1 목표와 동일) |
| 품질 | 근거 누락률 | 결함 주입 테스트 통과율 |
| 안전 | 무단 쓰기 시도 | dry-run 100%, 승인 없는 저장 0건 |
| 이관 | 반복 실패 | 3회 동일 결함 → ESCALATED |

**ROI:** 교육 환경에서는 합성 데이터 기준으로만 논의. 실제 도입 시 API·인프라 비용은 별도 산정.

---

## Day 2~4 구현 매핑 요약

| PRD 섹션 | Day | 저장소 증거 |
|---|---|---|
| 6 데이터·지식 | 2 | `knowledge/eco/`, `catalog.json` |
| 8 평가 | 2 | `eval/`, `tests/`, `validate_repo.py` |
| 5·6 도구화 | 3 | `src/server.mjs`, 3 MCP tools |
| 8 E2E | 3 | `npm run smoke` |
| 9 거버넌스 | 4 | HITL 상태 머신, `--approve` |
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

4대 기술 기둥: [tech-pillars.md](./tech-pillars.md)
