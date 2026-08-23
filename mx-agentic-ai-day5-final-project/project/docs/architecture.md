# 아키텍처 · 4층 에이전트 스택

> Harness → Knowledge → MCP → Agents 순으로 의존합니다.

```text
┌─────────────────────────────────────────────┐
│  Layer 4 · HITL + Multi-agent (Day 4)       │
│  Planner → Executor → Verifier → Human      │
├─────────────────────────────────────────────┤
│  Layer 3 · MCP (Day 3)                      │
│  list_* · get_* · write_*(dry-run)          │
├─────────────────────────────────────────────┤
│  Layer 2 · LLMWiki + GraphRAG* (Day 2)      │
│  knowledge/ · WIKI.md · relations.json*     │
├─────────────────────────────────────────────┤
│  Layer 1 · Harness (Day 2)                │
│  AGENTS.md · 상태 파일 · validate           │
└─────────────────────────────────────────────┘
```

## 층별 책임

| 층 | 담당 | 실패 시 |
|---|---|---|
| Harness | 원본 보호, 재개, 완료 검증 | ingest/도구 실행 차단 |
| Knowledge | 근거 있는 검색·관계 탐색 | UNKNOWN, Top-3 미달 |
| MCP | 도구 계약, E2E, 외부 연동* | 구조화 오류, dry-run |
| Agents | 역할 분리, HITL, HOTL | AWAITING_APPROVAL, ESCALATED |

## 데이터 흐름 (참조 시나리오)

```text
ECO (Wiki) ──equipment──▶ MCP 설비 로그 ──join──▶ 품질 fixtures
                              │
                              ▼
                    Multi-agent pipeline → Human approve
```

## 팀 프로젝트 변형

[여기에 팀 Day 1 PRD 기준으로 위 4층을 어떻게 채웠는지 5~10문장으로 설명]
