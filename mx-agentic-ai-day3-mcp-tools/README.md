# Day 3 · MCP 연동과 도구 확장

외부 계정이나 API 키 없이 실행되는 교육용 로컬 MCP 서버입니다. 합성 설비 로그를 읽고 오류를 집계하며, 승인 토큰이 있을 때만 `outputs/`에 리포트를 씁니다.

## 빠른 시작

```bash
npm test
npm run smoke
```

Claude Code 프로젝트 MCP로 연결하려면 저장소를 신뢰한 뒤 `.mcp.json`을 확인합니다. 수동 등록 예시는 다음과 같습니다.

```bash
claude mcp add --scope project --transport stdio equipment-log -- node src/server.mjs
claude mcp list
```

## 제공 도구

- `list_equipment_logs`: 날짜 범위의 설비·레코드 수 조회
- `get_equipment_errors`: 설비 ID와 날짜 범위별 오류 코드 집계
- `write_analysis_report`: 승인 토큰이 있을 때만 Markdown 리포트 생성

## 참고 자료

MCP, Loop Engineering, E2E Check, Claude/Codex MCP 호스트, JSON-RPC stdio, 도구 계약과 승인 게이트의 기술 배경 및 공식 URL은 [skill·기술 참고 자료](./docs/skill-and-tech-reference.md)를 참고합니다.

## 실습 순서

1. `npm test`로 도메인 로직을 검증한다.
2. `npm run smoke`로 MCP initialize → tools/list → tools/call을 확인한다.
3. 존재하지 않는 설비, 역전된 날짜, 승인 없는 쓰기를 테스트한다.
4. `.agents/skills/`의 스킬을 사용해 도구 계약과 결과를 점검한다.
