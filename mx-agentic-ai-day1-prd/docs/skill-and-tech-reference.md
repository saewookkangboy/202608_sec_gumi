<p align="center">
  <img src="../../assets/readme/day1-prd.svg" width="100%" alt="Day 1 PRD Canvas — 기획서에서 1~7칸을 채우고 8~10은 Day 2·4 예약">
</p>

오전 **기획서**를 AI가 실행 가능한 **PRD**로 바꿉니다. Day 2~4 실습의 계약(평가·도구·승인)은 5·6·7·8·9·10번에 매핑합니다.

## PRD Canvas × 4일

| Canvas | Day 1 | 이후 실습 |
|---|---|---|
| 1~4 배경·목표·사용자·흐름 | 기획서 이관 | — |
| 5 AI 역할 | 🔥 정의 | Day 3 MCP 도구 |
| 6 데이터 | 🔥 정의 | Day 2 `source_id` |
| 7 출력·fallback | 🔥 정의 | evidence ID |
| 8 평가 | 예약 | Day 2 eval |
| 9 안전 | 예약 | Day 4 HITL |
| 10 운영 | 예약 | Day 4 HOTL |

## 검증

```bash
python3 scripts/generate_canvas_pdf.py docs/prd.md docs/prd.pdf
python3 scripts/validate_day1.py

# 예제만 검증
python3 scripts/validate_day1.py --example quotation-bot

# 예제를 내 산출물 위치로 복사
python3 scripts/bootstrap_example.py quotation-bot
```

| 검사 | PASS 조건 |
|---|---|
| 기획서 | `docs/proposal.pdf` 또는 `proposal.md` |
| PRD 본문 | 1~10 섹션, 하지 않는 일 ≥2, fallback 규칙 |
| 샘플 | `sample-data/`, `expected-output/` 비어 있지 않음 |
| PDF | `docs/prd.pdf` A4 1장 |

## Repo skill

### `/prd-canvas-builder`

| 항목 | 내용 |
|---|---|
| 입력 | `docs/proposal.*`, 사용자 인터뷰 |
| 출력 | `prd.md`, `prd.pdf`, `sample-data/`, `expected-output/` |
| 금지 | 실데이터, 8·9·10 억지 작성 |

오프라인 프롬프트: [`docs/prompt.md`](../prompt.md)  
예시 산출물: [`docs/examples/quotation-bot/`](../examples/quotation-bot/)

## Day 1 → Day 2 연결

| Day 1 | Day 2 참조 구현 |
|---|---|
| `sample-data/` | `data/raw/eco_documents.jsonl` |
| `expected-output/` | `eval/questions.jsonl` 정답 |
| PRD 8번 "모르는 것" | Top-3 eval, harness |

→ [4일 커리큘럼](../../docs/curriculum-4day.md) · [참조 PRD](../../docs/reference-prd.md)
