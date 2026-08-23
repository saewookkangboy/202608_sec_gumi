# ECO 지식 위키 (LLMWiki)

> **LLMWiki** = 에이전트가 읽을 수 있는, 근거 추적 가능한 위키형 지식 베이스.  
> Day 2 Standard 산출물. GraphRAG Advanced는 `relations.json`을 추가합니다.

## 인덱스

| 문서 ID | 제목 | 원본 | 설명 |
|---|---|---|---|
| ECO-001 | 후면 하우징 | `data/raw/eco_documents.jsonl` | P-100 체결부 균열 예방 |
| ECO-002 | 카메라 브래킷 | 동일 | P-101 조립 공차 |
| ECO-003 | 후면 하우징 | 동일 | P-100 표면 찍힘 |
| ECO-004 | 힌지 커버 | 동일 | P-102 마찰 소음 |
| ECO-005 | 배터리 트레이 | 동일 | P-103 낙하 강도 |
| ECO-006 | 사이드 키 | 동일 | P-104 키 감도 |
| ECO-007 | 센서 홀 | 동일 | drawing: UNKNOWN |
| ECO-008 | 카메라 브래킷 | 동일 | P-101 진동 내구 |
| ECO-009 | 스피커 그릴 | 동일 | P-105 음질 |
| ECO-010 | USB 포트 | 동일 | P-106 내구 |
| ECO-011 | 방열 플레이트 | 동일 | PRESS-03 연결 |
| ECO-012 | 센서 홀더 | 동일 | equipment: UNKNOWN |

전체 카탈로그: [`catalog.json`](./catalog.json)

## LLMWiki 규칙

1. 모든 페이지에 `source_id`, `source_path` 필수
2. 원본에 없는 값은 `UNKNOWN` — 채우지 않음
3. 검색 답변은 Top-3 + 근거 ID
4. GraphRAG Advanced: `relations.json`으로 2-hop (`part → eco → drawing`)

## Day 5 연결

Day 5 `project/knowledge/wiki-index.md`에 팀 도메인 위키 구조를 이식합니다.

→ [LLMWiki + GraphRAG 브리지](./docs/llmwiki-graphrag-bridge.md)
