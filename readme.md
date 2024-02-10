# AUTO-WEEKLY-BIBLE-PLAN

## Description
`AUTO-WEEKLY-BIBLE-PLAN`은 성경 읽기 대행진 대회를 위해 매주 성경 읽기표를 자동으로 생성하는 프로젝트입니다. 


## To run

1. **about venv**

   프로젝트의 의존성을 격리하기 위해 가상 환경을 사용합니다. 가상 환경을 생성하고 활성화하는 방법은 다음과 같습니다:

   ```bash
   # 가상 환경 생성 (이미 생성된 경우 생략 가능)
   python3 -m venv .venv

   # 가상 환경 활성화
   source .venv/bin/activate
   ```


2. **requirements.txt**

   프로젝트의 의존성을 설치하기 위해 다음 명령어를 실행합니다:

   ```bash
   # pip 업그레이드
   pip install --upgrade pip

   # requirements.txt에 명시된 의존성 설치
   pip install -r requirements.txt
   ```

## 스크립트 실행

스크립트를 실행하기 전에 필요한 환경 변수를 설정합니다. 이 예제에서는 `START_BOOK`, `START_CHAPTER`, `DATE`, `SELECTED_CUSTOM` 환경 변수를 사용합니다:

```bash
export START_BOOK="창세기"
export START_CHAPTER="1"
export DATE="( mm월 dd일 - mm월 dd일 )"
export SELECTED_CUSTOM="animation_fall"
```

환경 변수를 설정한 후, 다음 명령어로 스크립트를 실행합니다:

```bash
python3.11 function.py
```

## 주의 사항

- 위 예제에서 `python3.11`는 Python 3.11 버전을 사용한다고 가정합니다. 실제 환경에 맞는 Python 실행 파일명을 사용해주세요.
- 환경 변수 설정은 현재 터미널 세션에만 적용됩니다. 새 터미널에서 스크립트를 실행하려면 환경 변수를 다시 설정해야 합니다.
- 가상 환경은 프로젝트 의존성을 격리하고 관리하기 위한 것입니다. 다른 프로젝트와 의존성 충돌을 방지하려면 가상 환경을 사용하는 것이 좋습니다.
