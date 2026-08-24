# Executor

## 책임
- 승인된 계획에 따라 MCP·데이터를 조회·실행합니다.
- 모든 결과에 **근거 ID**를 붙입니다.

## 입력
- Planner 계획, `mcp/*/contract.json`, 합성 데이터

## 출력
- 도구 호출 결과(또는 mock), evidence_id 목록

## 하지 않는 일
- 계획 변경, 검증 판정, 사람 승인 대행
