# Day 2 → Day 3 핸드오프

## 연결 개념

| Day 2 | Day 3 |
|---|---|
| Canvas **8** eval | MCP smoke가 E2E eval 역할 |
| `source_id` 근거 추적 | MCP tool 응답 evidence ID |
| Harness (`validate_repo.py`) | MCP 승인 토큰 (`APPROVE_WRITE`) |

팀 PRD §5·§6을 MCP 3도구로 쪼개는 연습을 `mcp/integration-plan.template.md`에 기록합니다.

## 승인 전 체크리스트

- [ ] `validate_repo.py` + unittest PASS
- [ ] `knowledge/WIKI.md` 인덱스 확인
- [ ] PRD §8 평가 초안을 팀 노트에 1문단 이상 작성
- [ ] Day 3 진입 목표(도구 3종) 합의

```bash
cd mx-agentic-ai-day2-knowledge-harness
python3 ../scripts/request_handoff.py --day 2
python3 ../scripts/approve_handoff.py --day 2 --reviewer "이름" --role instructor
python3 ../scripts/check_day_gate.py --enter-day 3
```
