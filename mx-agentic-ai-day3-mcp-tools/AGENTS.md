# Repository Instructions

## 목적

PRD의 AI 역할을 MCP **계약(contract) + mock**으로 설계하고, (선택) 로컬 stdio 서버로 검증한다.

## 안전 규칙

- `data/`의 입력 파일을 수정하지 않는다.
- 계약·mock은 `mcp/`에만 둔다. 기존 `src/`는 [선택] 구현 단계에서만 수정한다.
- 파일 쓰기는 `outputs/` 또는 `_sandbox/`에만 허용한다.
- 쓰기 도구는 `APPROVE_WRITE` 승인 토큰이 없으면 dry-run으로 끝낸다.
- stdout은 JSON-RPC 프로토콜 전용이다. 로그는 stderr에 기록한다.
- 완료 전 계약≥2·근거 ID·`approval-rule.md`를 확인하고, (선택) `npm test`와 `npm run smoke`를 실행한다.

Claude Code는 같은 폴더의 `CLAUDE.md`가 이 파일을 가져온다.
