# MCP 외부 연동 계획

> Day 3 로컬 MCP에서 실무에 연결할 **외부 시스템**을 계획합니다.  
> 합성·가상 시스템명만 사용하세요.

## 1. 연동 대상 (가상)

| 시스템 | 용도 | 읽기/쓰기 | 민감도 |
|---|---|---|---|
| [예: 가상 MES API] | 설비 상태 조회 | 읽기 | 중 |
| [예: 가상 티켓 시스템] | 분석 보고서 저장 | 쓰기(승인 필요) | 중 |

## 2. 도구 매핑 (Day 3 로컬 → 외부)

| 로컬 도구 | 외부 대응 | 변경 사항 |
|---|---|---|
| `list_equipment_logs` | | |
| `get_equipment_errors` | | |
| `write_analysis_report` | | 승인 토큰: `APPROVE_WRITE` |

## 3. 연결 방식

- Transport: [ ] stdio  [ ] SSE  [ ] HTTP
- 호스트: Claude Code
- 설정 파일: `.mcp.json` (프로젝트) 또는 `claude mcp add`

## 4. 검증 계획

- [ ] tools/list 도구 수 확인
- [ ] 안전한 tools/call 1회
- [ ] 승인 없는 쓰기 dry-run
- [ ] 원본 데이터 불변

## 5. Day 5 발표 포인트

- 왜 이 시스템을 MCP로 열었는가?
- 읽기/쓰기를 어떻게 분리했는가?
- 실제 도입 시 남은 리스크는?
