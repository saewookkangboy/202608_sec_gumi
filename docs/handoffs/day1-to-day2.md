# Day 1 → Day 2 핸드오프

## 교육생이 가져가는 것 (본인 PRD)

| Day 1 산출물 | Day 2에서 쓰는 방법 |
|---|---|
| `docs/prd.md` §1~7 | 팀 에이전트 정의 (변경 없음) |
| `docs/prd.md` §8 예약 | **Canvas 8** — eval·Harness로 채움 |
| `sample-data/` | 평가 입력 설계 참고 (Day 2는 `data/raw/` 고정) |
| `expected-output/` | Top-3·PASS 기준 설계 참고 |
| `.lab/project-profile.json` | Day 5 통합 시 제목·MVP 연결 |

## Day 2 참조 실습 (reference-prd)

Day 2 코드는 [`reference-prd.md`](../reference-prd.md) 의 ECO 12건 시나리오입니다.  
팀 PRD와 1:1 데이터가 아니어도 됩니다. **같은 Canvas 구조**로 매핑하세요.

| Canvas | 팀 PRD (예: 견적봇) | 참조 PRD (ECO) |
|---|---|---|
| 8 평가 | 메일 초안 품질 기준 | Top-3 검색 + source_id |
| Harness | AGENTS.md 규칙 | validate_repo.py |

## 승인 전 체크리스트

- [ ] `validate_day1.py` PASS
- [ ] `init_project_profile.py` 실행
- [ ] §5 하지 않는 일 ≥ 2
- [ ] §8·9·10 예약 메모 존재
- [ ] 강사/멘토가 PRD 방향 확인

```bash
cd mx-agentic-ai-day1-prd
python3 scripts/init_project_profile.py
python3 scripts/validate_day1.py
python3 ../scripts/request_handoff.py --day 1
python3 ../scripts/approve_handoff.py --day 1 --reviewer "이름" --role instructor
python3 ../scripts/check_day_gate.py --enter-day 2
```
