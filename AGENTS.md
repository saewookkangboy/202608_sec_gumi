# 202608_sec_gumi

삼성 MX 구미 **에이전틱 AI 5일** 실습 모노레포입니다.

- **Day 1** AI PRD Canvas로 정의  
- **Day 2~4** 4대 기술 기둥(Harness · LLMWiki/GraphRAG · MCP · HITL/Multi-agent) 실습  
- **Day 5** `project/` 통합·발표  

실행 환경은 **Claude Code**입니다. GitHub About·루트 README와 같은 스토리를 유지하세요.

| 문서 | 용도 |
|---|---|
| [`README.md`](README.md) | 저장소 소개·빠른 시작·일차 안내 |
| [`docs/curriculum-5day.md`](docs/curriculum-5day.md) | 5일 흐름·타임라인 |
| [`docs/tech-pillars.md`](docs/tech-pillars.md) | 4대 기술 기둥 |
| [`docs/reference-prd.md`](docs/reference-prd.md) | Day 2~4 참조 시나리오 |
| [`docs/handoffs/README.md`](docs/handoffs/README.md) | 사람 승인 게이트 |

## 일차 폴더

| Day | 경로 |
|:---:|---|
| 1 | `mx-agentic-ai-day1-prd/` |
| 2 | `mx-agentic-ai-day2-knowledge-harness/` |
| 3 | `mx-agentic-ai-day3-mcp-tools/` |
| 4 | `mx-agentic-ai-day4-multi-agent-hitl/` |
| 5 | `mx-agentic-ai-day5-final-project/` |

## 일차 README 공통 구성

1. **이론** · 2. **사용법** · 3. **저장소 구조** · 4. **예제** · 5. **실행** · 6. **테스트 조건** · 7. **문제 해결**

Day 2~4는 **PRD 연속형**(계약·문서·가상 테스트)이 기본이고, 기존 Node/Python 코드는 **[선택] 참조 트랙**입니다.

## 공통 규칙

- 합성 데이터만 사용한다. 실제 사업장 정보, 개인정보, API 키, 자격증명을 넣지 않는다.
- 원본 입력(`data/raw/`, `data/`, `fixtures/`)을 수정하지 않는다.
- 문서에 없는 값은 추정하지 않고 `UNKNOWN` 또는 구조화 실패로 남긴다.
- 가상 테스트는 `_sandbox/`(또는 Day 5 `project/evidence/`)에서만 한다.
- 검증 PASS를 사람 승인으로 간주하지 않는다.
- **일차 간 이동:** `request_handoff.py` + `approve_handoff.py`로 **사람 승인(APPROVED)** 후 `check_day_gate.py --enter-day N`.
- 완료 전 해당 일자 검증을 실행한다 (Day 1: `validate_day1.py`, Day 5: README 예제 1~9, Day 2~4: README 승인 조건 + 선택 테스트).

일자 폴더의 `CLAUDE.md`가 하네스 지침이고, skill 본문은 `.agents/skills/<name>/SKILL.md`에 둡니다. Claude Code는 `.claude/skills/` 브리지로 `/skill-name`을 호출합니다.

## 비주얼 스킬

| 스킬 | 출처 | 산출물 |
|---|---|---|
| `beautify-github-readme` | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | `assets/readme/` |
| `diagram-design` | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | `assets/diagrams/` |

토큰: `.agents/skills/diagram-design/references/style-guide.md` (`samsung-mx-gumi`).
