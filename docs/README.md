<p align="center">
  <img src="../assets/readme/docs-index.svg" width="100%" alt="Skill and Tech 참고 자료 — Claude Code가 CLAUDE.md와 /skill로 같은 계약을 읽고, Day 2는 Harness·Eval, Day 3는 Loop·E2E·MCP, Day 4는 HITL·HOTL·A2A로 나눈다">
</p>

<p align="center">
  <a href="#개요">개요</a> ·
  <a href="#권장-읽기-순서">읽기 순서</a> ·
  <a href="#문서">문서</a> ·
  <a href="./github-deployment-and-quickstart.md">배포·코드복사</a> ·
  <a href="#개념-맵">개념 맵</a> ·
  <a href="#claude-code-기준">Claude Code</a> ·
  <a href="#일차-간-핸드오프">핸드오프</a>
</p>

## 개요

**삼성 MX 구미 에이전틱 AI 5일 실습** 기술·개념 참고 인덱스입니다. 일자별 실습 README를 대체하지 않습니다.

| 역할 | 이 문서에서 찾는 것 |
|---|---|
| **교육생** | 개념 정의, Claude Code skill 호출, 일차별 skill 참고 링크 |
| **강사** | 커리큘럼·기술 기둥·배포 가이드·핸드오프 체크리스트 진입점 |
| **에이전트** | Harness·Eval·MCP·HITL 계약, 공통 규칙, 외부 스펙 링크 |

루트 [README](../README.md)는 저장소 전체 소개·빠른 시작·일차별 요약을 담습니다. **5일 커리큘럼**과 4대 기술 기둥은 먼저 [`curriculum-5day.md`](./curriculum-5day.md) · [`tech-pillars.md`](./tech-pillars.md)를 읽습니다.

## 권장 읽기 순서

```text
1. curriculum-5day.md     — 5일 흐름·일차별 목표·강사 타임라인
2. tech-pillars.md        — 4대 기술 기둥 × Day 매핑
3. reference-prd.md       — Day 2~4 공통 시나리오 (ECO·설비·품질)
4. dummy-data.md          — Day 2~4 합성 데이터 경로·사용법 (clone 후 확인)
5. github-deployment-and-quickstart.md — 환경·배포·복사용 프롬프트
6. handoffs/README.md     — 일차 간 사람 승인 게이트
7. 일차별 README.md       — 비개발자용 실습 가이드 (이론·구조도·실행·문제해결)
8. 일차별 skill-and-tech-reference.md — 해당 Day 실습 계약
```

### 일차별 실습 가이드 (비개발자용)

각 Day 폴더 `README.md`는 아래 **동일 섹션**으로 구성됩니다.

| 섹션 | 내용 |
|---|---|
| **이론** | 개념·구조도·안전 원칙 |
| **사용법** | 순서·팁·비개발자 안내 |
| **저장소 구조** | 실제 폴더·산출물 경로 |
| **예제** | 붙여넣기 프롬프트·시나리오 |
| **실행** | 단계별 진행·승인 조건 |
| **테스트 조건** | 가상 테스트(`_sandbox/` 등) 범위·되돌리기 |
| **문제 해결** | 증상·대응 표 |

| Day | 가이드 |
|:---:|---|
| 1 | [mx-agentic-ai-day1-prd/README.md](../mx-agentic-ai-day1-prd/README.md) |
| 2 | [mx-agentic-ai-day2-knowledge-harness/README.md](../mx-agentic-ai-day2-knowledge-harness/README.md) |
| 3 | [mx-agentic-ai-day3-mcp-tools/README.md](../mx-agentic-ai-day3-mcp-tools/README.md) |
| 4 | [mx-agentic-ai-day4-multi-agent-hitl/README.md](../mx-agentic-ai-day4-multi-agent-hitl/README.md) |
| 5 | [mx-agentic-ai-day5-final-project/README.md](../mx-agentic-ai-day5-final-project/README.md) |

## 문서

### 커리큘럼·기둥

| 문서 | skill | 내용 |
|---|---|---|
| [**5일 커리큘럼**](./curriculum-5day.md) | — | Day 1~5 + 4대 기술 기둥, 강사 8시간 타임라인 |
| [**기술 기둥**](./tech-pillars.md) | — | Harness · LLMWiki/GraphRAG · MCP · HITL/Multi, Standard vs Advanced |
| [**참조 PRD**](./reference-prd.md) | — | Day 2~4 공통 시나리오: ECO·설비 로그·품질 연계 분석 에이전트 |
| [**Dummy Data 가이드**](./dummy-data.md) | — | Day 2~4 합성 데이터 필요 판단·경로·스키마·clone 확인 |
| [4일 커리큘럼 (이전)](./curriculum-4day.md) | — | Day 5 미포함 버전 (레거시) |

### 운영·배포

| 문서 | skill | 내용 |
|---|---|---|
| [공통 배포·빠른 시작](./github-deployment-and-quickstart.md) | Claude `/skill` | main 배포, 팀 브랜치 제출, Day 1~5 프롬프트와 검증 명령 |
| [일차 간 핸드오프](./handoffs/README.md) | — | `request_handoff` · `approve_handoff` · `check_day_gate` |
| [day1-to-day2](./handoffs/day1-to-day2.md) | — | PRD → Harness/Eval 연결 |
| [day2-to-day3](./handoffs/day2-to-day3.md) | — | 지식 → MCP 도구화 |
| [day3-to-day4](./handoffs/day3-to-day4.md) | — | MCP → HITL/Multi-agent |
| [day4-to-day5](./handoffs/day4-to-day5.md) | — | 운영 → 최종 프로젝트 |

### 일차별 skill·기술 참고

| 실습 | skill | 내용 |
|---|---|---|
| [Day 1](../mx-agentic-ai-day1-prd/docs/skill-and-tech-reference.md) | `/prd-canvas-builder` | PRD Canvas 1~7, sample-data, expected-output, validate_day1 |
| [Day 2](../mx-agentic-ai-day2-knowledge-harness/docs/skill-and-tech-reference.md) | `/eco-knowledge-builder` · `/repo-harness-auditor` | 원본 잠금, `source_id`, SHA-256, Top-3 검색, Claude Code 하네스 |
| [Day 3](../mx-agentic-ai-day3-mcp-tools/docs/skill-and-tech-reference.md) | `/mcp-tool-designer` · `/mcp-smoke-test` | MCP stdio, E2E smoke, Claude Code MCP 호스트 |
| [Day 4](../mx-agentic-ai-day4-multi-agent-hitl/docs/skill-and-tech-reference.md) | `/plan-maintenance-analysis` · … · `/request-human-approval` | HITL · HOTL · Multi-agent · A2A* |
| [Day 5](../mx-agentic-ai-day5-final-project/docs/skill-and-tech-reference.md) | `/final-project-assembler` | project/ 조립·데모·발표 (자연어 프롬프트) |

### 기계 판독용 인덱스

[`research-ingest.jsonl`](./research-ingest.jsonl) — 외부 리서치·스펙 URL과 실습 매핑. 각 줄은 `day`, `concept`, `url`, 한국어 요약, 실습 매핑, 도입 수준, 검증일을 포함합니다. 에이전트가 공식 문서 출처를 찾을 때 사용합니다.

## 개념 맵

실습 전체에서 반복되는 개념 정의입니다. PRD Canvas 칸·적용 일차·저장소 증거를 한 표에 둡니다.

| 개념 | 교육용 정의 | PRD Canvas | 주 적용일 | 구현 증거 |
|---|---|---|---|---|
| AI PRD Canvas | AI가 실행 가능한 요구사항 10칸 | 1~10 | Day 1~5 | `prd.md`, 참조 PRD, `final-prd.md` |
| Harness Engineering | 에이전트를 둘러싼 규칙·상태·도구·검증·재개 장치 설계 | 6·8 | Day 2 | `AGENTS.md`, `CLAUDE.md`, 상태 파일, 원본 해시, 검증 스크립트 |
| LLMWiki | Markdown 지식 + 인덱스 + `source_id`로 추적 가능한 위키형 지식 | 6 | Day 2 | `knowledge/eco/*.md`, `WIKI.md`, `catalog.json` |
| Graph Engineering | 엔터티·관계·상태 전이를 그래프로 표현하고 탐색하는 설계 | — | Day 2 → 4 | `relations.json` 2-hop, Day 4 상태 전이 |
| GraphRAG | 지식 그래프 + 검색으로 관계 질의 확장 | 8 | Day 2 Advanced | `knowledge/relations.json` |
| Loop Engineering | 실행→관찰→판정→재시도/중단을 명시한 제어 루프 | 5 | Day 3 → 4 | MCP smoke loop, 최대 3회 복구 루프 |
| E2E | 사용자/클라이언트 요청부터 실제 결과와 부작용까지 전체 경로 검증 | 8 | Day 3 | `initialize → tools/list → tools/call`, 승인 없는 쓰기 차단 |
| MCP | 모델이 도구·리소스·프롬프트에 표준 방식으로 접근하는 프로토콜 | 5·6 | Day 3 | `src/server.mjs`, `.mcp.json` stdio |
| A2A | 서로 독립적인 에이전트 시스템 사이의 발견·메시지·작업·산출물 교환 표준 | — | Day 4 Advanced | Agent Card와 Task/Artifact 계약 설계 |
| Agent Orchestration | 전문 역할의 소유권·handoff·순서를 코드 또는 모델 판단으로 조정 | 5·9 | Day 4 | Planner→Executor→Verifier→Human |
| Eval Check | 고정 데이터·판정 기준·회귀 테스트로 품질을 반복 측정 | **8** | Day 2 → 4 | Top-k eval, 프로토콜 smoke, 결함 주입 테스트 |
| HITL | 위험 행동 전에 실행을 멈추고 명시적 사람 결정을 기다림 | **9** | Day 4 | `AWAITING_APPROVAL`, `--approve` |
| HOTL | 자동 실행을 계속 관찰하다 임계치·이상 시 사람이 개입 | **10** | Day 4 Advanced | `events.jsonl`, 동일 결함 3회 `ESCALATED` |

> 요청에 적힌 `HILT`는 일반적으로 쓰이는 `HITL`(Human-in-the-Loop)의 오기로 보고 문서 전체에서 `HITL`로 통일했습니다. `HOTL`은 Human-on-the-Loop를 뜻하는 교육용 운영 구분이며, 특정 SDK의 단일 표준 API 이름은 아닙니다.

### 개념 × 일차 요약

```text
Day 1  Canvas 1~7 정의, 8·9·10 예약
Day 2  Harness + LLMWiki + eval (Canvas 8)  [+ GraphRAG Advanced]
Day 3  MCP 도구화 + E2E smoke (Canvas 5·6)
Day 4  Multi-agent + HITL/HOTL (Canvas 9·10)  [+ A2A Advanced]
Day 5  project/ 통합 — final-prd, architecture, evidence, demo
```

<p align="center">
  <img src="../assets/readme/docs-hosts.svg" width="100%" alt="Claude Code는 CLAUDE.md와 /skill을 쓰고, Day 3는 프로젝트 .mcp.json으로 로컬 MCP 서버를 붙인다">
</p>

## Claude Code 기준

실습은 **Claude Code**에서 진행합니다. skill 본문은 `.agents/skills/`에 두고 `.claude/skills/` 브리지로 `/skill-name`을 호출합니다. 일자 `CLAUDE.md`가 하네스 지침입니다.

| 층 | Claude Code | 실습 매핑 |
|---|---|---|
| Harness | [`CLAUDE.md`](https://code.claude.com/docs/en/memory), [Skills](https://code.claude.com/docs/en/skills) | Day 2 원본 잠금·상태 파일·검증 |
| Loop | [Agent SDK loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) | Day 3 smoke, Day 4 3회 복구 |
| Graph | subagent 관계를 명시적 workflow로 구성 | Day 2 지식 관계, Day 4 역할·상태 전이 |
| Tools | [MCP](https://code.claude.com/docs/en/mcp) | Day 3 로컬 stdio 서버 (`.mcp.json`) |
| A2A | MCP로 도구, A2A로 독립 에이전트 | Day 4 Advanced Agent Card |
| Eval | 테스트·max_turns·측정 후 복잡도 | Day 2 Top-3, Day 3 smoke, Day 4 결함 주입 |
| HITL | `default` 권한, `canUseTool` | `APPROVE_WRITE`, `--approve` |
| HOTL | hooks·외부 모니터링으로 이상 감시 | `events.jsonl`, 3회 후 `ESCALATED` |

### 기본 skill·repo

- [anthropics/skills](https://github.com/anthropics/skills) — Claude Agent Skills 카탈로그
- [a2aproject/A2A](https://github.com/a2aproject/A2A) — Agent-to-Agent 스펙·SDK
- [modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol) — MCP 스펙

<p align="center">
  <img src="../assets/readme/learning-path.svg" width="100%" alt="Day 2 Harness·eval, Day 3 MCP·E2E, Day 4 HITL·HOTL 학습 경로">
</p>

## 일차 간 핸드오프

자동 검증 **PASS ≠ 다음 일차 진입**. 각 Day 종료 시 사람 승인이 필요합니다.

```bash
python3 scripts/check_day_gate.py --status
python3 scripts/request_handoff.py --day N
python3 scripts/approve_handoff.py --day N --reviewer "이름" --role instructor
python3 scripts/check_day_gate.py --enter-day N+1
```

| 구분 | 내용 |
|---|---|
| **팀 PRD** | `mx-agentic-ai-day1-prd/docs/prd.md` — 본인 업무 에이전트 정의 |
| **참조 PRD** | [`reference-prd.md`](./reference-prd.md) — Day 2~4 합성 데이터 실습 시나리오 |
| **승인 패킷** | `mx-agentic-ai-day{N}-*/.lab/handoff-approval.json` |
| **체크리스트** | [`handoffs/templates/`](./handoffs/templates/) |

[handoffs/README.md](./handoffs/README.md)

## 세 실습이 공유하는 계약

1. **원본은 건드리지 않는다.** Day 2 `data/raw/`, Day 3 `data/`, Day 4 `fixtures/`.
2. **없는 값은 추정하지 않는다.** `UNKNOWN`, 빈 집계, 조인 실패를 모델이 메우지 않는다.
3. **근거 ID가 없으면 결과가 아니다.** `ECO-*`, `LOG-*`, `QUALITY-*`.
4. **스킬은 점진적으로 로드된다.** `name`·`description`만 상시 적재되고, 본문은 해당 작업에서만 읽힌다. Claude Code는 `.claude/skills/` 브리지를 통해 `/skill-name`으로 호출한다.
5. **검증 PASS는 사람 승인이 아니다.** Day 3 dry-run과 Day 4 `AWAITING_APPROVAL`을 사람이 직접 확인한다.

## 공통 외부 자료

Claude Code 문서를 먼저 읽습니다. Agents API와 운영 가이드는 보조 참고입니다.

| 분류 | 링크 |
|---|---|
| Agent Skills | [Specification](https://agentskills.io/specification) · [Anthropic Engineering](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) |
| 에이전트 설계 | [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) |
| Claude Code | [Skills](https://code.claude.com/docs/en/skills) · [CLAUDE.md](https://code.claude.com/docs/en/memory) · [MCP](https://code.claude.com/docs/en/mcp) · [Agent loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) |
| MCP | [Specification 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18) · [Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) |
| A2A | [Protocol](https://a2a-protocol.org/latest/) |
| PRD Canvas | [3_AI PRD 가이드 (Notion)](https://adorable-hail-415.notion.site/3_AI-PRD-3c4137efedf680f7a491f3bd50c832c9) |
| 리서치 인덱스 | [research-ingest.jsonl](./research-ingest.jsonl) |
