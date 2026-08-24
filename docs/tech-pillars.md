# 기술 기둥 × Day 1~5 매핑

> 4대 기술 기둥은 Day 1~4 실습과 Day 5 최종 프로젝트에 매핑합니다.

---

## 4대 기술 기둥

| 기둥 | 실무 질문 | Day | 저장소 증거 | Day 5 산출물 |
|---|---|:---:|---|---|
| **Harness Engineering** | 에이전트를 어떤 규칙·상태·검증으로 감싸나? | 2 | `AGENTS.md`, 상태 파일, `validate_repo.py` | `project/harness/` |
| **LLMWiki + GraphRAG** | 지식을 어떻게 구조화·검색·관계 탐색하나? | 2 | `knowledge/`, `WIKI.md`, `relations.json`* | `project/knowledge/` |
| **MCP 제작·외부 연동** | AI가 어떤 도구로 내부·외부 시스템에 닿나? | 3 | 로컬 stdio MCP, smoke E2E | `project/mcp/` |
| **HITL + Multi-agent** | 역할을 어떻게 나누고 언제 사람이 승인하나? | 4 | 역할 스킬, 상태 머신 | `project/agents/` |

\* GraphRAG는 Day 2 Advanced (`knowledge/relations.json` 2-hop). Standard는 LLMWiki(추적 가능 위키형 지식)까지.

---

## Day 1~5 한 줄 흐름

```text
Day 1  PRD 정의        → 무엇을 만들지 (Canvas 1~7)
Day 2  Harness + Wiki  → 지식을 어떻게 믿을지 (Canvas 8 + GraphRAG*)
Day 3  MCP 연동        → 도구로 어떻게 실행할지 (Canvas 5·6)
Day 4  HITL·Multi      → 언제 멈추고 누가 승인할지 (Canvas 9·10)
Day 5  최종 프로젝트   → 실제 업무 결과물로 통합·발표
```

---

## Day 간 핸드오프 (Day 5 입력)

| 출발 | 산출물 | Day 5에서 쓰는 곳 |
|---|---|---|
| Day 1 | `docs/prd.md`, `sample-data/`, `expected-output/` | `project/docs/final-prd.md` |
| Day 2 | `knowledge/`, eval PASS, harness 상태 | `project/knowledge/`, `project/harness/` |
| Day 3 | MCP 도구 계약, smoke PASS, 연동 계획 | `project/mcp/` |
| Day 4 | 역할 계약, HITL 정책, demo run | `project/agents/`, `project/evidence/` |

---

## Standard vs Advanced

| 기둥 | Standard (필수) | Advanced (팀 과제) |
|---|---|---|
| Harness | 원본 잠금, 상태 파일, validate | 하네스 감사 스킬 확장 |
| LLMWiki + GraphRAG | Markdown 지식 + Top-3 eval | `relations.json` 2-hop GraphRAG |
| MCP | 로컬 3도구 + smoke | 외부 MCP 서버 1개 연동 계획·PoC |
| HITL + Multi-agent | 4역할 + AWAITING_APPROVAL | A2A Agent Card, HOTL 이관 |

---

## Day 5 최종 결과물 체크리스트

발표 전 `mx-agentic-ai-day5-final-project/`에서 Claude Code로 확인:

1. **예제 1)** `project/` 조립 → `manifest.json` READY
2. **final-prd.md** — Day 1 PRD + Day 2~4에서 채운 8·9·10번 완성
3. **architecture.md** — Knowledge / MCP / Agents 4층 구조도
4. **integration-map.md** — Day 2~4 증거 파일 경로·PASS 여부
5. **demo-script.md** — 5~7분 발표 시나리오 (문제→구현→검증→한계)
6. **evidence/** — demo-data · demo-run · self/final-check

```bash
cd mx-agentic-ai-day5-final-project
claude
# README 예제 1)~9) 순서대로 (자연어 프롬프트)
```

→ [5일 커리큘럼](./curriculum-5day.md) · [참조 PRD](./reference-prd.md) · [Day 5 README](../mx-agentic-ai-day5-final-project/README.md)
