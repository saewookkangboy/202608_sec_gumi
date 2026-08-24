# Repository Instructions

## 목적

합성 금형 ECO 문서를 추적 가능한 지식 자산으로 변환하고 검색 품질을 검증한다.
팀 PRD 연속형 실습은 `relations.json` · `eval-top3.md` · (선택) `knowledge/001-*.md`를 사용한다.

## 안전 규칙

- `data/raw/`의 원본 파일을 수정·삭제·이동하지 않는다.
- 생성 결과는 `knowledge/`, `relations.json`, `eval-top3.md`, `outputs/`, `reports/`, `_sandbox/`에만 기록한다.
- 문서에 없는 값은 추정하지 말고 `UNKNOWN`으로 기록한다.
- 가상 테스트는 `_sandbox/`에서만 한다.
- 변경 전 대상 파일 목록을 먼저 제시한다.
- 완료 전 `eval-top3.md` 확인과 (선택) `python3 scripts/validate_repo.py`를 실행한다.

## 작업 상태

- 계획은 `plan.md`, 진행 상태는 `progress.md`, 선택 근거는 `decisions.md`에 기록한다.
- 이미 완료된 단계는 재실행하지 말고 다음 미완료 단계부터 이어간다.

Claude Code는 같은 폴더의 `CLAUDE.md`가 이 파일을 가져온다.
