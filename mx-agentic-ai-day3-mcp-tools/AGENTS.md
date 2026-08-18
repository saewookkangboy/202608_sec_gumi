# Repository Instructions

## 목적

합성 설비 로그를 안전하게 조회하는 로컬 stdio MCP 서버를 구현한다.

## 안전 규칙

- `data/`의 입력 파일을 수정하지 않는다.
- 파일 쓰기는 `outputs/`에만 허용한다.
- 쓰기 도구는 `APPROVE_WRITE` 승인 토큰이 없으면 dry-run으로 끝낸다.
- stdout은 JSON-RPC 프로토콜 전용이다. 로그는 stderr에 기록한다.
- 완료 전 `npm test`와 `npm run smoke`를 실행한다.

Claude Code는 같은 폴더의 `CLAUDE.md`가 이 파일을 가져온다.

