# Day 2 → Day 3 핸드오프

## 연결 개념

| Day 2 | Day 3 |
|---|---|
| Canvas **8** eval | MCP smoke가 E2E eval 역할을 합니다 |
| `source_id`로 근거 추적 | MCP 도구 응답의 evidence ID로 이어집니다 |
| Harness (`validate_repo.py`) | MCP 승인 토큰(`APPROVE_WRITE`)으로 이어집니다 |

팀 PRD의 §5와 §6을 MCP 도구 3개로 쪼개 보고, 그 결과를 `mcp/integration-plan.template.md`에 적어 둡니다.

## 승인 전 체크리스트

- [ ] `validate_repo.py`와 unittest 모두 PASS
- [ ] `knowledge/WIKI.md` 인덱스 확인
- [ ] PRD §8 평가 초안을 팀 노트에 한 문단 이상 작성
- [ ] Day 3에서 만들 도구 3종에 대해 팀이 합의

```bash
cd mx-agentic-ai-day2-knowledge-harness
python3 ../scripts/request_handoff.py --day 2
python3 ../scripts/approve_handoff.py --day 2 --reviewer "이름" --role instructor
python3 ../scripts/check_day_gate.py --enter-day 3
```
