# 202608_sec_gumi

삼성 MX 구미 에이전틱 AI 3일 실습 모노레포입니다. 루트에서 구현하지 말고, 해당 일자 폴더로 이동한 뒤 그 폴더의 `AGENTS.md`를 따릅니다.

- Day 2 지식 자산화·하네스: `mx-agentic-ai-day2-knowledge-harness/`
- Day 3 로컬 MCP 도구: `mx-agentic-ai-day3-mcp-tools/`
- Day 4 멀티 에이전트 HITL: `mx-agentic-ai-day4-multi-agent-hitl/`

## 공통 규칙

- 합성 데이터만 사용한다. 실제 사업장 정보, 개인정보, API 키, 자격증명을 넣지 않는다.
- 원본 입력(`data/raw/`, `data/`, `fixtures/`)을 수정하지 않는다.
- 문서에 없는 값은 추정하지 않고 `UNKNOWN` 또는 구조화 실패로 남긴다.
- 검증 PASS를 사람 승인으로 간주하지 않는다.
- 완료 전 해당 일자의 테스트(Day 3는 smoke 포함)를 실행한다.

레이아웃은 Codex(`AGENTS.md`, `.agents/skills/`)입니다. Claude Code는 같은 폴더의 `CLAUDE.md`가 이 지침을 가져옵니다.
