# Day 2 · 지식 자산화와 하네스 엔지니어링

합성 금형 ECO 문서를 근거 추적 가능한 지식 자산으로 변환하고, 검색 품질과 저장소 안전 규칙을 검증하는 실습입니다.

## 학습 목표

1. 원본을 수정하지 않고 정규화된 지식 파일을 생성한다.
2. 질문별 관련 문서를 검색하고 근거 문서 ID를 남긴다.
3. `AGENTS.md`와 repo skill로 반복 작업 규칙을 고정한다.
4. 상태 파일만으로 중단된 작업을 복구한다.

## 빠른 시작

```bash
python3 scripts/normalize_docs.py
python3 scripts/search_knowledge.py "P-100 하우징 변경과 관련된 ECO는?"
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

Codex에서는 다음처럼 repo skill을 호출할 수 있습니다.

```text
$eco-knowledge-builder로 data/raw/eco_documents.jsonl을 지식 자산으로 변환해줘.
$repo-harness-auditor로 저장소 안전 규칙과 산출물을 점검해줘.
```

## 참고 자료

Harness Engineering, Graph Engineering, skill 설계, `AGENTS.md`, 근거 추적, SHA-256과 Eval Check의 기술 배경 및 공식 URL은 [skill·기술 참고 자료](./docs/skill-and-tech-reference.md)를 참고합니다.

## Standard / Advanced

- Standard: 정규화, 키워드 검색, Top-3 평가, 하네스 검증
- Advanced: `knowledge/relations.json`을 확장해 부품→ECO→도면 2-hop 질의 추가

## 완료 기준

- 12개 ECO 레코드가 `knowledge/eco/`에 생성됨
- 모든 문서에 `source_id`와 `source_path`가 존재함
- 원본 SHA-256이 작업 전후 동일함
- 평가 질문의 정답 문서가 Top-3에 포함됨
- `plan.md`, `progress.md`, `decisions.md`가 비어 있지 않음
