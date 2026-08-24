# Day 1 → Day 2 핸드오프

## 교육생이 가져가는 것 (본인 PRD)

| Day 1 산출물 | Day 2에서 쓰는 방법 |
|---|---|
| `docs/prd.md` §1~7 | 팀 에이전트 정의를 그대로 씁니다 (수정 없음) |
| `docs/prd.md` §8 예약 칸 | **Canvas 8** — eval과 Harness로 채웁니다 |
| `sample-data/` | 평가 입력을 설계할 때 참고합니다 (Day 2는 `data/raw/`로 고정) |
| `expected-output/` | Top-3와 PASS 기준을 설계할 때 참고합니다 |
| `.lab/project-profile.json` | Day 5에서 통합할 때 제목과 MVP를 이어 줍니다 |

## Day 2 참조 실습 (reference-prd)

Day 2 코드는 [`reference-prd.md`](../reference-prd.md)에 있는 ECO 12건 시나리오를 씁니다.  
팀 PRD와 데이터가 똑같지 않아도 괜찮습니다. **같은 Canvas 구조**에 맞춰 짝지어 보세요.

| Canvas | 팀 PRD (예: 견적봇) | 참조 PRD (ECO) |
|---|---|---|
| 8 평가 | 메일 초안의 품질 기준 | Top-3 검색과 source_id |
| Harness | AGENTS.md 규칙 | validate_repo.py |

## 승인 전 체크리스트

- [ ] `validate_day1.py` PASS
- [ ] `init_project_profile.py` 실행 완료
- [ ] §5 하지 않는 일 2개 이상
- [ ] §8·9·10에 예약 메모 작성
- [ ] 강사나 멘토가 PRD 방향을 확인

```bash
cd mx-agentic-ai-day1-prd
python3 scripts/init_project_profile.py
python3 scripts/validate_day1.py
python3 ../scripts/request_handoff.py --day 1
python3 ../scripts/approve_handoff.py --day 1 --reviewer "이름" --role instructor
python3 ../scripts/check_day_gate.py --enter-day 2
```
