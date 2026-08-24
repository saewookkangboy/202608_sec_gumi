# Day 3 MCP 계약·mock (PRD 연속형)

이 폴더는 **계약 설계 + 가상 응답** 전용입니다. 기존 `src/` Node 서버는 그대로 두고, 여기에는 도구별 계약을 쌓습니다.

```text
mcp/
├── README.md                 # 이 문서
├── approval-rule.md          # 승인 필요 도구 목록
├── [도구명]/
│   ├── contract.json         # 입력·출력·오류 스키마
│   └── mock-response.json    # 계약에 맞는 샘플 응답
└── (참조) integration-plan.template.md · external-servers.example.json
```

**승인 조건:** 도구 계약 최소 2개(읽기1+쓰기1) / 모든 mock에 근거 ID / `approval-rule.md` 작성
