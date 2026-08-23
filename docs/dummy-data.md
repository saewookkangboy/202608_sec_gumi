# Day 2~4 Dummy Data (합성 데이터) 가이드

GitHub clone만으로 Day 2~4 실습이 돌아가도록 **교육용 합성 데이터**를 저장소에 포함합니다. 실제 사업장·개인정보·API 키는 넣지 않습니다.

## 필요 여부 판단

| Day | Dummy Data 필요? | 이유 | 저장소 상태 |
|:---:|:---:|---|---|
| **2** | **필요** | ECO 원본·eval 질문 없이 정규화·Top-3 검증 불가 | `data/raw/` · `eval/` 포함 |
| **3** | **필요** | MCP가 CSV를 읽어 조회·집계·evidence_id 생성 | `data/equipment_logs.csv` 포함 |
| **4** | **필요** | Planner/Executor가 설비 오류·품질 요약을 조인 | `fixtures/*.json` 포함 |
| 1 | (별도) | 팀 `sample-data/` 또는 예제 `quotation-bot` | Day 1 README 참고 |
| 5 | (조립) | Day 1~4 산출물 통합 — 신규 원본 데이터 없음 | — |

**결론:** Day 2~4는 모두 Dummy Data가 필수이며, **이미 git에 커밋되어 있습니다.** clone 후 별도 다운로드·생성은 하지 않습니다. 원본을 임의로 다시 만들면 SHA-256·`evidence_id`·테스트 기대값이 깨집니다.

## clone 후 존재 확인

저장소 루트에서:

```bash
python3 scripts/verify_dummy_data.py
```

수동 확인:

```bash
test -f mx-agentic-ai-day2-knowledge-harness/data/raw/eco_documents.jsonl && echo OK-day2-raw
test -f mx-agentic-ai-day2-knowledge-harness/eval/questions.jsonl && echo OK-day2-eval
test -f mx-agentic-ai-day3-mcp-tools/data/equipment_logs.csv && echo OK-day3
test -f mx-agentic-ai-day4-multi-agent-hitl/fixtures/quality_summary.json && echo OK-day4-q
test -f mx-agentic-ai-day4-multi-agent-hitl/fixtures/equipment_errors.json && echo OK-day4-e
```

## 경로 일람 (모노레포 기준)

| Day | 역할 | 경로 (repo root 기준) | 형식 | 건수(대략) |
|:---:|---|---|---|---|
| 2 | ECO 원본 (읽기 전용) | `mx-agentic-ai-day2-knowledge-harness/data/raw/eco_documents.jsonl` | JSONL | 12 |
| 2 | 검색 평가 | `mx-agentic-ai-day2-knowledge-harness/eval/questions.jsonl` | JSONL | 4 |
| 3 | 설비 로그 (읽기 전용) | `mx-agentic-ai-day3-mcp-tools/data/equipment_logs.csv` | CSV | 15+header |
| 4 | 품질 요약 (읽기 전용) | `mx-agentic-ai-day4-multi-agent-hitl/fixtures/quality_summary.json` | JSON | 3 |
| 4 | 오류 집계 fixture | `mx-agentic-ai-day4-multi-agent-hitl/fixtures/equipment_errors.json` | JSON | 3 |

일자 폴더에 `cd`한 뒤에는 상대 경로만 씁니다.

```text
# Day 2 폴더에서
data/raw/eco_documents.jsonl
eval/questions.jsonl

# Day 3 폴더에서
data/equipment_logs.csv

# Day 4 폴더에서
fixtures/quality_summary.json
fixtures/equipment_errors.json
```

## 일차별 스키마·사용법

### Day 2 — ECO JSONL

**필드:** `source_id`, `date`, `part_id`, `part_name`, `reason`, `impact`, `drawing`, `equipment`

**샘플 (1줄):**

```json
{"source_id":"ECO-001","date":"2026-07-01","part_id":"P-100","part_name":"후면 하우징","reason":"체결부 균열 예방","impact":"금형 CAV-01 보강","drawing":"DRW-100-A","equipment":"PRESS-01"}
```

**실습에서 쓰는 법:**

```bash
cd mx-agentic-ai-day2-knowledge-harness
# 원본은 읽기만 — 수정 금지
python3 scripts/normalize_docs.py
python3 scripts/search_knowledge.py "P-100 하우징 변경과 관련된 ECO는?"
python3 scripts/validate_repo.py
```

Claude Code: `/eco-knowledge-builder` — `data/raw/eco_documents.jsonl`을 수정하지 말 것.

**조인 키 → Day 3:** `equipment` 값 (`PRESS-01`, `PRESS-03`, `MILL-02` 등).

---

### Day 3 — 설비 로그 CSV

**컬럼:** `timestamp`, `equipment_id`, `level`, `error_code`, `message`

**샘플:**

```csv
timestamp,equipment_id,level,error_code,message
2026-08-11T09:14:00,PRESS-01,ERR,ERR-204,pressure deviation
```

**실습에서 쓰는 법:**

```bash
cd mx-agentic-ai-day3-mcp-tools
# MCP 서버가 DATA = data/equipment_logs.csv 를 읽음
npm test
npm run smoke
```

도구 예: `list_equipment_logs` / `get_equipment_errors` (기간 `2026-08-11`~`2026-08-15` 권장).

Claude Code: `/mcp-smoke-test` — CSV 불변성 확인.

---

### Day 4 — fixtures (품질 + 오류 집계)

**quality_summary.json** — `equipment_id`, `inspected`, `defects`, `evidence_id` (`QUALITY-*`)

**equipment_errors.json** — `equipment_id`, `error_count`, `top_error`, `evidence_ids` (`LOG-*`)

Day 3 CSV를 다시 파싱하지 않고, **집계 결과를 fixture로 고정**해 Executor·Verifier가 동일 입력으로 재현합니다. Claude 실습에서는 `fixtures/` 또는 승인된 Day 3 MCP만 사용합니다.

**실습에서 쓰는 법:**

```bash
cd mx-agentic-ai-day4-multi-agent-hitl
npm test
npm run demo
# 코드: src/pipeline.mjs 가 fixtures/*.json 로드
```

Claude Code: `/execute-evidence-plan` — `fixtures/` 또는 승인 MCP만.

## 공통 조인 키 (참조 시나리오)

```text
PRESS-01  ← Day2 ECO-001/003 · Day3 ERR-204 · Day4 QUALITY-001
PRESS-03  ← Day2 ECO-005/011 · Day3 ERR-501 · Day4 QUALITY-002
MILL-02   ← Day2 ECO-002/008 · Day3 ERR-410 · Day4 QUALITY-003
```

근거 ID 체계: `ECO-*` (Day 2) · `LOG-*` (Day 3) · `QUALITY-*` (Day 4).

## 규칙

1. **원본 수정 금지** — `data/raw/`, `data/equipment_logs.csv`, `fixtures/`
2. **생성물만 쓰기** — Day 2 `knowledge/`, Day 3 `outputs/`, Day 4 `runs/`
3. **없는 값** — 추정하지 말고 `UNKNOWN`
4. **복구** — 실수로 수정했다면 `git checkout -- <경로>`

## 관련 문서

- [참조 PRD §6 데이터](./reference-prd.md)
- [GitHub 배포·빠른 시작](./github-deployment-and-quickstart.md)
- Day 2 [README](../mx-agentic-ai-day2-knowledge-harness/README.md) · Day 3 [README](../mx-agentic-ai-day3-mcp-tools/README.md) · Day 4 [README](../mx-agentic-ai-day4-multi-agent-hitl/README.md)
