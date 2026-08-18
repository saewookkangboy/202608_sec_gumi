# Day 3 · MCP 연동과 도구 확장

외부 계정이나 API 키 없이 실행되는 교육용 로컬 MCP 서버입니다. 합성 설비 로그를 읽고 오류를 집계하며, 승인 토큰이 있을 때만 `outputs/`에 리포트를 씁니다.

## 빠른 시작

```bash
cd mx-agentic-ai-day3-mcp-tools
npm test
npm run smoke
```

정상 완료 시 정확히 3개 도구, 오류 집계의 `evidence_id`, 구조화 오류, 승인 없는 dry-run, 원본 CSV 불변을 확인합니다.

## Claude Code로 적용

저장소의 `.mcp.json`은 `equipment-log` stdio 서버를 프로젝트 단위로 공유합니다.

```bash
claude mcp list
claude
```

연결이 보이지 않을 때만 다시 등록합니다.

```bash
claude mcp add --scope project --transport stdio equipment-log -- node src/server.mjs
claude mcp get equipment-log
```

Claude Code에 다음 프롬프트를 복사합니다.

```text
/mcp-tool-designer를 사용해 src/server.mjs의 세 도구 계약을 감사해줘.
단일 책임, 입력 스키마, evidence_id, 오류 형식, 읽기/쓰기 권한을 정리해.
write_analysis_report는 outputs/에만 쓰고 APPROVE_WRITE가 없으면 dry-run이어야 해.
stdout은 JSON-RPC 전용이고 진단은 stderr인지 확인하고, 코드를 바꾸기 전에
변경 계약과 추가할 테스트부터 제안해줘.
```

```text
/mcp-smoke-test를 실행해 initialize -> tools/list -> tools/call을 검증해줘.
정확히 3개 도구, 오류 집계와 evidence_id, 역전 날짜의 구조화 오류,
승인 없는 write의 dry-run, data/equipment_logs.csv 불변성을 확인해줘.
```

## Codex로 적용

Day 3 폴더에서 절대 경로로 로컬 MCP를 등록합니다.

```bash
DAY3_DIR="$(pwd)"
codex mcp add equipment-log -- node "$DAY3_DIR/src/server.mjs"
codex mcp get equipment-log
codex
```

이미 같은 이름이 있다면 `codex mcp get equipment-log`로 명령을 먼저 확인하고, 다른 서버를 가리킬 때만 해당 항목을 정리한 뒤 다시 등록합니다.

```text
$mcp-tool-designer로 equipment-log MCP의 세 도구 계약을 점검해줘.
읽기와 쓰기를 분리하고, write_analysis_report는 APPROVE_WRITE 없이는
파일을 만들지 않는 dry-run이어야 해. 입력·출력·실패 사례와 필요한 테스트를
먼저 명시한 뒤 승인된 범위만 수정하고 npm test와 npm run smoke를 실행해.
```

```text
$mcp-smoke-test로 initialize, tools/list, 안전한 tools/call, 역전 날짜 오류,
승인 없는 쓰기를 E2E 검증해줘. stdout JSON-RPC 오염과 원본 CSV 변경도
확인하고, 실패 method와 교정 조치를 정확히 보고해줘.
```

## 제공 도구

- `list_equipment_logs`: 날짜 범위의 설비·레코드 수 조회
- `get_equipment_errors`: 설비 ID와 날짜 범위별 오류 코드 집계
- `write_analysis_report`: 승인 토큰이 있을 때만 Markdown 리포트 생성

## 참고 자료

- 전체 배포와 코드복사 절차: [GitHub 배포와 Day 2~4 실습 가이드](../docs/github-deployment-and-quickstart.md)
- 기술 배경과 공식 URL: [skill·기술 참고 자료](./docs/skill-and-tech-reference.md)

## 실습 순서

1. `npm test`로 도메인 로직을 검증한다.
2. `npm run smoke`로 MCP initialize → tools/list → tools/call을 확인한다.
3. 존재하지 않는 설비, 역전된 날짜, 승인 없는 쓰기를 테스트한다.
4. `.agents/skills/`의 스킬을 사용해 도구 계약과 결과를 점검한다.

핵심 시나리오를 에이전트에 복사합니다.

```text
equipment-log MCP를 사용해 다음을 순서대로 수행해줘.
1. 2026-08-11~2026-08-15 로그의 설비별 레코드 수를 조회한다.
2. 같은 기간 오류 코드를 집계하고 모든 수치에 evidence_id를 붙인다.
3. 시작일이 종료일보다 늦은 요청으로 구조화 오류를 확인한다.
4. write_analysis_report를 승인 없이 호출해 dry-run과 파일 미생성을 확인한다.
5. 사람의 명시적 승인 전에는 실제 쓰기를 수행하지 않는다.
각 단계의 도구명, 입력, 핵심 출력, 검증 결과를 표로 정리해줘.
```

교육 진행자가 실제 쓰기를 승인한 경우에만 사용합니다.

```text
APPROVE_WRITE를 승인 토큰으로 사용해 앞서 검증한 분석만 outputs/에 저장해줘.
저장 경로, 포함된 evidence_id, 원본 CSV 해시 불변 여부를 확인해줘.
```

## 검증과 팀 브랜치 제출

```bash
npm test
npm run smoke
git status --short
git diff --check
git add src/ scripts/ test/ outputs/ README.md
git commit -m "feat(day3): complete MCP E2E lab"
git push -u origin HEAD
```
