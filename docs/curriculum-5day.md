# 삼성 MX 구미 · 에이전틱 AI 5일 커리큘럼

> **AI PRD Canvas**와 **4대 기술 기둥**으로 Day 1 정의, Day 2~4 실습, **Day 5 결과물·발표**까지 진행합니다.  
> 기술 기둥 매핑: [`tech-pillars.md`](./tech-pillars.md)

---

## 5일 흐름

```text
Day 1  PRD 정의              Canvas 1~7 · sample-data · expected-output
  ▼ [사람 승인: handoff day1]
Day 2  Harness + LLMWiki     Harness Engineering · eval · GraphRAG*
  ▼ [사람 승인: handoff day2]
Day 3  MCP 제작·연동         로컬 MCP · 외부 연동 계획 · smoke E2E
  ▼ [사람 승인: handoff day3]
Day 4  HITL + Multi-agent    역할 분리 · 승인 게이트 · HOTL 이관
  ▼ [사람 승인: handoff day4]
Day 5  최종 프로젝트 발표    실제 업무 결과물 통합 · demo · evidence
```

> 일차 간 승인: [`handoffs/README.md`](./handoffs/README.md) · `scripts/check_day_gate.py` · `scripts/approve_handoff.py`

| 일차 | 기술 기둥 | PRD Canvas | 실습 저장소 | 산출물 |
|---|---|---|---|---|
| **Day 1** | (정의) | 1~7 (+ 8·9·10 예약) | `mx-agentic-ai-day1-prd/` | `prd.md`, `prd.pdf`, 샘플 |
| **Day 2** | Harness + LLMWiki/GraphRAG | **8** | `mx-agentic-ai-day2-knowledge-harness/` | `knowledge/`, `relations.json`, `eval-top3.md` |
| **Day 3** | MCP 제작·외부 연동 | **5·6** | `mx-agentic-ai-day3-mcp-tools/` | `mcp/*/contract.json`, mock, 승인 규칙 |
| **Day 4** | HITL + Multi-agent | **9·10** | `mx-agentic-ai-day4-multi-agent-hitl/` | `agents/`, `gate-log.md` |
| **Day 5** | **통합** | 8·9·10 완성 | `mx-agentic-ai-day5-final-project/` | `project/` 전체, 발표 자료 |

> 각 Day README는 **이론 → 사용법 → 저장소 구조 → 예제 → 실행 → 테스트 조건 → 문제 해결** 순서로 통일되어 있습니다. Day 2~4는 PRD 연속형(문서·계약·가상 테스트)이 기본이고, 기존 자동 테스트/서버는 [선택] 참조 트랙입니다.


---

## 기술 기둥 × 일차 상세

### Day 2 · Harness Engineering + LLMWiki + GraphRAG

**교육 질문:** "지식을 에이전트가 믿을 수 있는 자산으로 만들고, 관계 질의까지 확장하려면?"

| 개념 | Standard | Advanced |
|---|---|---|
| Harness Engineering | `AGENTS.md`, 상태 파일 3종, `validate_repo.py` | `/repo-harness-auditor` 확장 |
| LLMWiki | `knowledge/eco/*.md` + `knowledge/WIKI.md` 인덱스 | 팀 도메인 위키 구조 설계 |
| GraphRAG | Top-3 키워드 검색 + `source_id` | `knowledge/relations.json` 2-hop |

```bash
cd mx-agentic-ai-day2-knowledge-harness
python3 scripts/validate_repo.py && python3 -m unittest discover -s tests -v
```

**Day 5 연결:** `project/harness/`, `project/knowledge/wiki-index.md`

---

### Day 3 · MCP 간편 제작 및 연동(외부)

**교육 질문:** "PRD의 AI 역할을 도구로 쪼개고, 외부 시스템까지 어떻게 연결할까?"

| 개념 | Standard | Advanced |
|---|---|---|
| MCP 제작 | `src/server.mjs` 3도구, JSON Schema | 도구 1개 추가 설계 |
| 로컬 연동 | stdio + `npm run smoke` | Claude Code `.mcp.json` |
| 외부 연동 | `docs/external-mcp-integration.md` 계획 | `mcp/external-servers.example.json` PoC |

```bash
cd mx-agentic-ai-day3-mcp-tools
npm test && npm run smoke
```

**Day 5 연결:** `project/mcp/integration-plan.md`

---

### Day 4 · HITL + Multi-agent

**교육 질문:** "검증 통과 후에도 왜 멈추고, 역할을 왜 코드로 나누나?"

| 개념 | Standard | Advanced |
|---|---|---|
| Multi-agent | Planner / Executor / Verifier / Human | A2A Agent Card 초안 |
| HITL | `AWAITING_APPROVAL`, `--approve` | 승인 패킷 필드 확장 |
| HOTL | 3회 동일 결함 → `ESCALATED` | `events.jsonl` 운영 대시보드 |

```bash
cd mx-agentic-ai-day4-multi-agent-hitl
npm test && npm run demo
```

**Day 5 연결:** `project/agents/role-contracts.md`, `project/agents/hitl-policy.md`

---

### Day 5 · 최종 프로젝트 발표

**교육 질문:** "Day 1~4를 내 업무 에이전트로 어떻게 통합·발표할까?"

| 산출물 | 설명 |
|---|---|
| `project/docs/final-prd.md` | Canvas 1~10 완성본 (Day 1 + 2~4 회고 반영) |
| `project/docs/architecture.md` | 4층 아키텍처 (Harness / Knowledge / MCP / Agents) |
| `project/docs/integration-map.md` | Day 2~4 증거·PASS·파일 경로 |
| `project/docs/demo-script.md` | 5~7분 발표 스크립트 |
| `project/evidence/` | 테스트·실행 요약 |

```bash
cd mx-agentic-ai-day5-final-project
claude
# README 예제 1)~9) — project/ 조립 → 점검 → 데모 → 발표 문서
# (선택) /final-project-assembler
```

**Day 5 연결:** 전 Day 산출물이 `project/`에 모여 발표 패키지가 됩니다.

Repo skill: `/final-project-assembler`

---

## 공통 시나리오 (Day 2~4 참조 구현)

```text
[Day 2 LLMWiki]  ECO-001..012 + WIKI.md  ──equipment──▶  PRESS-01..
       │  GraphRAG*: relations.json 2-hop
       ▼
[Day 3 MCP]  list · aggregate · write(dry-run)  ──▶  equipment_logs.csv
       │  외부 MCP*: 연동 계획
       ▼
[Day 4 Multi]  Plan → Execute → Verify → Human  ──▶  AWAITING_APPROVAL
       ▼
[Day 5]  팀별 Day 1 PRD + 위 4기둥 통합 → 최종 결과물
```

참조 PRD: [`reference-prd.md`](./reference-prd.md)

---

## 강사용 타임라인 (1일 8시간 × 5일)

| 시간 | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
|---|---|---|---|---|---|
| 오전 1 | 기획서 | Harness 개념 | MCP 개념 | 역할·상태 | 프로젝트 조립 |
| 오전 2 | PRD Canvas | LLMWiki 실습 | 로컬 MCP | HITL 데모 | 아키텍처 작성 |
| 오후 1 | 자가 점검 | eval + GraphRAG* | smoke E2E | 4종 경로 | 통합 검증 |
| 오후 2 | Day 2 예고 | PRD 8번 회고 | 외부 연동 계획 | PRD 9·10 | **발표** |

---

## 저장소 구조

```text
202608_sec_gumi/
├── docs/
│   ├── curriculum-5day.md      ← 이 문서
│   ├── tech-pillars.md         ← 4대 기술 기둥
│   └── reference-prd.md
├── mx-agentic-ai-day1-prd/
├── mx-agentic-ai-day2-knowledge-harness/
├── mx-agentic-ai-day3-mcp-tools/
├── mx-agentic-ai-day4-multi-agent-hitl/
└── mx-agentic-ai-day5-final-project/   ← Day 5
```

---

## 참고

- [3_AI PRD 가이드 (Notion)](https://adorable-hail-415.notion.site/3_AI-PRD-3c4137efedf680f7a491f3bd50c832c9)
- [GitHub 배포·코드복사 가이드](./github-deployment-and-quickstart.md)
- [4일 커리큘럼 (이전)](./curriculum-4day.md) — Day 5 미포함 버전
