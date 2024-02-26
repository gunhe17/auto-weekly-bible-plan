# AUTO-WEEKLY-BIBLE-PLAN

## Description
`AUTO-WEEKLY-BIBLE-PLAN`은 성경 읽기 대행진 대회를 위해 매주 성경 읽기표를 자동으로 생성하는 프로젝트입니다. 


## To run

1. **about venv**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```


2. **requirements.txt**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## 스크립트 실행
 After edit 'run.sh'

```bash
scripts/run.sh
```

## 주의 사항

- 위 예제에서 `python3.11`는 Python 3.11 버전을 사용한다고 가정합니다. 실제 환경에 맞는 Python 실행 파일명을 사용해주세요.
- 환경 변수 설정은 현재 터미널 세션에만 적용됩니다. 새 터미널에서 스크립트를 실행하려면 환경 변수를 다시 설정해야 합니다.
- 가상 환경은 프로젝트 의존성을 격리하고 관리하기 위한 것입니다. 다른 프로젝트와 의존성 충돌을 방지하려면 가상 환경을 사용하는 것이 좋습니다.
