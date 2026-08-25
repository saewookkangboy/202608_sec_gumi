# Decisions

- 외부 API 키 없이 재현할 수 있도록 Python 표준 라이브러리 기반 검색을 사용한다.
- 실제 업무 정보 대신 합성 ECO 데이터만 사용한다.
- 정적 GraphRAG 데모는 기존 `relations.json` 팀 실습을 덮어쓰지 않고 `knowledge/graphrag/`에 격리한다.
- 작은 합성 문서이므로 학습 편의를 위해 ECO 문서당 청크 1개를 사용하고, 모든 관계에 근거 필드를 둔다.
- `UNKNOWN`은 추정하거나 그래프 노드로 승격하지 않고 `metadata.json`의 `unknown_values`에 보존한다.
