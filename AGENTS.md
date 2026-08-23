# 202608_sec_gumi

삼성 MX 구미 에이전틱 AI **5일** 실습 모노레포입니다. **AI PRD Canvas**와 **4대 기술 기둥**(Harness · LLMWiki/GraphRAG · MCP · HITL/Multi-agent)으로 Day 1 정의, Day 2~4 실습, **Day 5 최종 프로젝트 발표**까지 진행합니다.

전체 구조: [`docs/curriculum-5day.md`](docs/curriculum-5day.md) · 기술 기둥: [`docs/tech-pillars.md`](docs/tech-pillars.md) · 참조 PRD: [`docs/reference-prd.md`](docs/reference-prd.md)

- Day 1 AI PRD 정의: `mx-agentic-ai-day1-prd/`
- Day 2 Harness + LLMWiki/GraphRAG (Canvas 8): `mx-agentic-ai-day2-knowledge-harness/`
- Day 3 MCP 제작·외부 연동 (Canvas 5·6): `mx-agentic-ai-day3-mcp-tools/`
- Day 4 HITL + Multi-agent (Canvas 9·10): `mx-agentic-ai-day4-multi-agent-hitl/`
- Day 5 최종 프로젝트 발표: `mx-agentic-ai-day5-final-project/`

## 공통 규칙

- 합성 데이터만 사용한다. 실제 사업장 정보, 개인정보, API 키, 자격증명을 넣지 않는다.
- 원본 입력(`data/raw/`, `data/`, `fixtures/`)을 수정하지 않는다.
- 문서에 없는 값은 추정하지 않고 `UNKNOWN` 또는 구조화 실패로 남긴다.
- 검증 PASS를 사람 승인으로 간주하지 않는다.
- **일차 간 이동:** 전일 `request_handoff.py` + `approve_handoff.py` 로 **사람 승인(APPROVED)** 후 `check_day_gate.py --enter-day N` 으로 다음 일차에 진입한다. 가이드: [`docs/handoffs/README.md`](docs/handoffs/README.md)
- 완료 전 해당 일자 검증을 실행한다 (Day 1: `validate_day1.py`, Day 5: `assemble_project.py` + `validate_day5.py`, Day 2~4: 각 테스트).

**실습 실행 환경은 Claude Code**입니다. 일자 폴더의 `CLAUDE.md`가 하네스 지침이고, repo skill 본문은 `.agents/skills/<name>/SKILL.md`에 둡니다. Claude Code는 `.claude/skills/` 브리지로 같은 skill을 `/skill-name`으로 호출합니다.

## 비주얼 스킬

| 스킬 | 출처 | 산출물 |
|---|---|---|
| `beautify-github-readme` | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | `assets/readme/` |
| `diagram-design` | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) v2.6 | `assets/diagrams/` |

토큰: `.agents/skills/diagram-design/references/style-guide.md` (`samsung-mx-gumi`).
