# 정적 GraphRAG 데모 데이터

이 폴더는 `data/raw/eco_documents.jsonl`의 합성 ECO 12건을 브라우저와 간단한 FE 데모에서 바로 읽을 수 있게 변환한 학습용 스냅샷입니다. 기존 `knowledge/eco/*.md`와 루트 `relations.json` 실습을 대체하지 않으며, GraphRAG 결과 모양을 먼저 살펴보는 참조 예제입니다.

## 파일 구성

| 파일 | 역할 |
|---|---|
| `documents.jsonl` | 원본 ECO 한 건을 하나의 추적 가능한 문서로 표현합니다. |
| `chunks.jsonl` | 검색이 반환하는 텍스트 조각입니다. 이 작은 데모에서는 문서당 1개입니다. |
| `entities.jsonl` | ECO, 부품, 변경 사유·영향, 도면, 설비 같은 그래프 노드입니다. |
| `relationships.jsonl` | 노드 사이의 방향 관계와 그 근거입니다. |
| `entity_index.csv` | 엔터티를 스프레드시트나 표 UI에서 빠르게 살펴보는 인덱스입니다. |
| `metadata.json` | 스키마 버전, 건수, 타입별 집계, `UNKNOWN` 목록입니다. |

## 다섯 가지 개념

1. **문서(document)**: 출처를 추적하는 가장 큰 단위입니다. `document_id`와 원본의 `source_id`를 함께 가집니다.
2. **청크(chunk)**: 검색 결과로 FE에 보여 줄 텍스트 조각입니다. `document_id`로 문서에, `entity_ids`로 그래프 노드에 연결됩니다.
3. **엔터티(entity)**: 사람이나 사물처럼 관계의 출발점·도착점이 되는 노드입니다. 이 예제에는 `PART`, `DRAWING`, `EQUIPMENT` 등이 있습니다.
4. **관계(relationship)**: `source_entity_id → target_entity_id` 방향의 엣지입니다. 예: `reason:ECO-001 → eco:ECO-001 → part:P-100`은 “균열 예방 사유가 ECO 변경을 촉발했고 그 변경은 후면 하우징에 영향을 준다”는 2-hop입니다.
5. **메타데이터(metadata)**: 날짜, 출처 경로, 타입, 누락값처럼 검색·필터·검증에 쓰는 보조 정보입니다. 원본의 `UNKNOWN`은 채워 넣지 않고 `metadata.json`에 그대로 남깁니다.

모든 관계에는 `source_id`, `source_path`, `chunk_id`, `evidence`가 있어 화면에서 “왜 이 관계가 보이나요?”를 원문까지 역추적할 수 있습니다.

## FE/demo에서 읽기

JSONL은 한 줄에 JSON 객체 하나가 있습니다. 별도 라이브러리 없이 다음처럼 정적 파일을 불러올 수 있습니다.

```js
async function loadJsonl(url) {
  const text = await fetch(url).then((response) => {
    if (!response.ok) throw new Error(`${url}: ${response.status}`);
    return response.text();
  });
  return text.trim().split("\n").filter(Boolean).map(JSON.parse);
}

const base = "/knowledge/graphrag";
const [chunks, entities, relationships] = await Promise.all([
  loadJsonl(`${base}/chunks.jsonl`),
  loadJsonl(`${base}/entities.jsonl`),
  loadJsonl(`${base}/relationships.jsonl`),
]);
```

간단한 데모 흐름은 다음과 같습니다.

1. 사용자의 검색어가 들어 있는 `chunks[].text`를 찾습니다.
2. 선택한 청크의 `entity_ids`를 노드로 표시합니다.
3. 해당 ID가 `source_entity_id` 또는 `target_entity_id`인 관계를 이어 그립니다.
4. 엣지를 클릭하면 `evidence`와 `source_id`를 보여 줍니다.
5. 필요하면 같은 부품을 공유하는 다른 ECO까지 한 번 더 따라가되 수업 범위인 2-hop에서 멈춥니다.

정적 호스팅 경로가 다르면 `base`만 바꾸면 됩니다. `file://`로 직접 열 때는 브라우저 보안 정책 때문에 `fetch`가 막힐 수 있으므로 저장소의 기존 FE 개발 서버나 단순 정적 서버를 사용하세요.

## 재생성 및 확인

저장소의 Day 2 폴더에서 실행합니다.

```bash
python3 scripts/build_static_graphrag.py
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

생성기는 Python 표준 라이브러리만 사용합니다. 원본을 수정하지 않고 이 폴더의 파생 파일만 다시 씁니다.
