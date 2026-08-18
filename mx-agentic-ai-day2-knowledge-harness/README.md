# Day 2 · 지식 자산화와 하네스 엔지니어링

합성 금형 ECO 문서를 근거 추적 가능한 지식 자산으로 변환하고, 검색 품질과 저장소 안전 규칙을 검증하는 실습입니다.

## 학습 목표

1. 원본을 수정하지 않고 정규화된 지식 파일을 생성한다.
2. 질문별 관련 문서를 검색하고 근거 문서 ID를 남긴다.
3. `AGENTS.md`/`CLAUDE.md`와 repo skill로 반복 작업 규칙을 고정한다.
4. 상태 파일만으로 중단된 작업을 복구한다.

## 빠른 시작

```bash
cd mx-agentic-ai-day2-knowledge-harness
python3 scripts/normalize_docs.py
python3 scripts/search_knowledge.py "P-100 하우징 변경과 관련된 ECO는?"
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

완료 기준은 ECO 12건, `source_id`·`source_path`, 원본 SHA-256 불변, 평가 정답 Top-3 포함입니다.

## Claude Code로 적용

```bash
claude
```

Claude Code 대화창에 다음 프롬프트를 복사합니다.

```text
/eco-knowledge-builder를 사용해 Day 2 실습을 수행해줘.
data/raw/eco_documents.jsonl은 절대 수정하지 말고, 합성 ECO 12건을
knowledge/eco/*.md와 knowledge/catalog.json으로 정규화해.
각 결과에 source_id, source_path, 원본 SHA-256 근거를 유지하고,
"P-100 하우징 변경과 관련된 ECO는?" 질문의 Top-3와 근거 ID를 확인해.
문서에 없는 값은 UNKNOWN으로 남겨. 완료 전 validate_repo.py와 전체
unittest를 실행하고 변경 파일, 테스트 결과, 남은 위험을 요약해줘.
```

```text
/repo-harness-auditor로 AGENTS.md의 원본·출력 경계, plan.md, progress.md,
decisions.md, catalog 근거 필드, raw.sha256와 전체 테스트를 감사해줘.
실패는 파일명과 수정 방법을 보고하고 raw 데이터는 고치지 마.
```

## Codex로 적용

```bash
codex
```

Codex 대화창에 다음 프롬프트를 복사합니다.

```text
$eco-knowledge-builder를 사용해 data/raw/eco_documents.jsonl을 추적 가능한
지식 자산으로 변환해줘. raw 입력은 수정하지 말고, 각 산출물에 source_id와
source_path를 유지해. "P-100 하우징 변경과 관련된 ECO는?"의 Top-3와
근거 ID를 확인한 뒤 validate_repo.py와 전체 unittest를 실행해줘.
```

```text
$repo-harness-auditor로 AGENTS.md의 출력 경계, 상태 파일 3종, catalog의
근거 필드, 원본 SHA-256, 전체 테스트를 확인해. 검증 실패를 숨기거나
raw 파일을 수정하지 마.
```

## 핵심 실습

1. 원본 입력 경계와 SHA-256을 확인한다.
2. 정규화 스크립트로 12개 Markdown과 catalog를 생성한다.
3. 검색 Top-3의 `source_id`와 `source_path`를 확인한다.
4. 상태 파일 3종으로 계획·진행·판단 근거를 남긴다.
5. 하네스 검증과 회귀 테스트를 모두 통과한다.

Advanced 팀 과제 프롬프트:

```text
기존 knowledge/catalog.json 계약과 raw 입력을 변경하지 않고,
knowledge/relations.json에 part_id -> eco_id -> drawing_id 관계를 추가해줘.
"P-100과 연결된 ECO 및 도면은?"에 관계 경로와 source_id를 반환하고,
정상 경로·관계 없음·잘못된 ID 테스트를 추가해. 완료 전 하네스 감사와
전체 회귀 테스트를 실행해줘.
```

## 검증과 팀 브랜치 제출

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
git status --short
git diff --check
git add knowledge/ plan.md progress.md decisions.md tests/
git commit -m "feat(day2): complete knowledge harness lab"
git push -u origin HEAD
```

## 참고 자료

- 전체 배포와 코드복사 절차: [GitHub 배포와 Day 2~4 실습 가이드](../docs/github-deployment-and-quickstart.md)
- 기술 배경과 공식 URL: [skill·기술 참고 자료](./docs/skill-and-tech-reference.md)

## Standard / Advanced

- Standard: 정규화, 키워드 검색, Top-3 평가, 하네스 검증
- Advanced: `knowledge/relations.json`을 확장해 부품→ECO→도면 2-hop 질의 추가

## 완료 기준

- 12개 ECO 레코드가 `knowledge/eco/`에 생성됨
- 모든 문서에 `source_id`와 `source_path`가 존재함
- 원본 SHA-256이 작업 전후 동일함
- 평가 질문의 정답 문서가 Top-3에 포함됨
- `plan.md`, `progress.md`, `decisions.md`가 비어 있지 않음
