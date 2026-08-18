# Repository Instructions

## 목적

합성 금형 ECO 문서를 추적 가능한 지식 자산으로 변환하고 검색 품질을 검증한다.

## 안전 규칙

- `data/raw/`의 원본 파일을 수정·삭제·이동하지 않는다.
- 생성 결과는 `knowledge/`, `outputs/`, `reports/`에만 기록한다.
- 문서에 없는 값은 추정하지 말고 `UNKNOWN`으로 기록한다.
- 변경 전 대상 파일 목록을 먼저 제시한다.
- 완료 전 `python3 scripts/validate_repo.py`와 전체 테스트를 실행한다.

## 작업 상태

- 계획은 `plan.md`, 진행 상태는 `progress.md`, 선택 근거는 `decisions.md`에 기록한다.
- 이미 완료된 단계는 재실행하지 말고 다음 미완료 단계부터 이어간다.

