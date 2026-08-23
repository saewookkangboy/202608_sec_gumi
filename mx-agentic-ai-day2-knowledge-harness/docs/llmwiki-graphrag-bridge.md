# LLMWiki + GraphRAG 브리지

> Day 2에서 **Harness Engineering** 위에 **LLMWiki**(추적 가능 위키)와 **GraphRAG**(관계 탐색)를 쌓는 방법입니다.

---

## 개념 구분

| 개념 | 역할 | 이 실습 |
|---|---|---|
| **Harness Engineering** | 원본 보호, 상태, 검증, 재개 | `AGENTS.md`, `validate_repo.py`, 상태 파일 3종 |
| **LLMWiki** | 사람·AI용 근거 위키 | `knowledge/eco/*.md`, `knowledge/WIKI.md` |
| **GraphRAG** | 엔터티·관계 그래프 + 다중 홉 검색 | Advanced: `knowledge/relations.json` |

```text
Harness (규칙·검증)
    └── LLMWiki (문서 + source_id)
            └── GraphRAG* (관계 엣지 + 2-hop)
```

---

## Standard: LLMWiki

1. `normalize_docs.py` → Markdown 12건
2. `knowledge/WIKI.md` → 인덱스 페이지
3. `search_knowledge.py` → Top-3 + `source_id`
4. `eval/questions.jsonl` → 회귀 평가

**실무 이식:** 팀 SOP·매뉴얼·FAQ를 같은 패턴으로 `knowledge/`에 ingest.

---

## Advanced: GraphRAG

`knowledge/relations.json` 스키마 (템플릿: [`relations.template.json`](../knowledge/relations.template.json)):

```json
{
  "edges": [
    {
      "from_type": "part",
      "from_id": "P-100",
      "relation": "AFFECTS",
      "to_type": "eco",
      "to_id": "ECO-001",
      "source_id": "ECO-001",
      "source_path": "data/raw/eco_documents.jsonl"
    }
  ]
}
```

질의 예: "P-100과 연결된 ECO 및 도면은?" → 2-hop 경로 + 근거.

참고: [Microsoft GraphRAG](https://github.com/microsoft/graphrag) — 비정형 텍스트에서 엔터티·커뮤니티 추출. 이 실습은 **합성 ECO**로 동일 패턴을 축소 구현합니다.

---

## Day 3·4·5 연결

| Day 2 산출 | 다음 단계 |
|---|---|
| `equipment` 필드 (ECO) | Day 3 MCP 설비 ID 조인 |
| `source_id` 규칙 | Day 4 evidence ID 계약 |
| `WIKI.md` + eval PASS | Day 5 `project/knowledge/` |

---

## Day 5 체크리스트 (지식 층)

- [ ] 팀 도메인 위키 인덱스 1페이지 (`wiki-index.md`)
- [ ] ingest 규칙 (원본 경로, UNKNOWN 정책)
- [ ] eval 질문 ≥ 3개 + PASS 기준
- [ ] GraphRAG*: 관계 엣지 ≥ 5개 + 2-hop 질의 1개
