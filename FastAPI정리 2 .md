# FastAPI란 2

생성일시: 2025/08/19 10:23 (GMT+9)
생성자: 강한손
최종 업데이트 시간: 2025년 8월 19일

## pytest

---

파이썬으로 작성된 코드를 테스트 하기 위한 테스트 프레임 워크

- Install
    - 다음 명령어를 통해 설치
    
    ```bash
    poetry add --group=dev pytest==8.3.4
    ```
    
- Test 방법
    
    ```python
    # test_example.py 파일
    import pytest
    
    def add(x:int, y:int) -> int: # 타입힌트
        return x + y
    #테스트 구문
    def test_add():
    	# Given / 재료의 준비
    	a, b = 1, 2
    	# When / 테스트 대상이 되는 함수 호출
    	result = add(a, b):
    	# Then / 
        assert add(1, 1) == 2
        
        #테스트 구문
    def test_add():
    	# Given / 
    	a, b = 2, 3
    	# When
    	result = add(a, b):
    	# Then
        assert add(2, 3) == 5
    
    ```
    
    - `assert` 문으로 간단하게 테스트 할 수 있음
    
    테스트 방법은 `pytest .` 또는 입력창에 def ~ 왼쪽에 초록색으로 화살표 아이콘 클릭하고 → ‘run’을 선택하여 실행
    
- Test의 성공과 실패 & 검증
    
    test를 실행하는 동안 정의 되어 있는가가 성공과 실패의 기준
    

## Coverage

---

- 커버리지의 정의
    
    $$
    \frac{(테스트 도중 한 번이라도 실행된 제품코드)}{(전체 제품 코드)}
    $$
    

- Install
    - 다음 명령어를 통해 설치
    
    ```bash
    poetry add --group=dev coverage==7.6.9
    ```
    
- Test
    
    다음과 같은 코드를 실행하여 테스트 했을 때 
    
    ```python
    def add(a: int, b: int) -> int:
        return a + b
    
    def mul(a: int, b: int) -> int:
        return a * b
    
    def test_add() -> None:
        # Given
        a, b = 1, 1
    
        # When
        result = add(a, b)
    
        # Then
        assert result == 2
    ```
    
    - 테스트
    - `poetry run coverage run -m pytest temp.py`
    - 보고서 출력
    - `poetry run coverage report -m`
    - `-m`  옵션을 통해 실행 되지 않은 라인을 알려준다
    
    ```bash
    poetry run coverage report -m
    
    Name      Stmts   Miss  Cover   Missing
    ---------------------------------------
    temp.py       8      1    88%   6
    ---------------------------------------
    TOTAL         8      1    88%
    
    ```
    
    다음의 결과를 출력한다
    
    다음의 내용은 총 8줄의 작성된 코드중 6번줄 한 줄만 실행 되지 않았다고 해석할 수 있다
    
- Test +
    
    위와 같이 실행하면 테스트 하는 줄까지 포함되어 실행되는 것으로 간주하여 계산의 정확도가 떨어지게 됨.
    
    테스트 코드와 제품코드를 분리하여 확인 할 필요가 있다
    
    - `pyproject.toml` 에 다음과 같이 추가
        
        ```toml
        
        [tool.coverage.run]
        omit = ["*/test_*.py"]  # 루트 혹은 루트 아래의 파일들 중 test_ 로 시작하는 파일을 제외.
        
        ```
        
    - `test_temp.py` 라는 파일에 테스트 코드를 분리
        
        ```python
        from temp import add
        
        def test_add() -> None:
            # Given
            a, b = 1, 1
        
            # When
            result = add(a, b)
        
            # Then
            assert result == 2
        
        ```
        
    - [`temp.py`](http://temp.py)  기존의 제품코드와 테스트코드가 있던 파일
        
        ```python
        def add(a: int, b: int) -> int:
            return a + b
        
        def mul(a: int, b: int) -> int:
            return a * b
        ```
        
- 커버리지 실행에 대한 코드
    - `poetry run coverage run -m pytest .`
    - `poetry run coverage report -m`
    - `poetry run coverage html`

## 테스트 스크립트 작성

- pytest_asyncio 설치
    
    `poetry add --group=dev pytest-asyncio==0.25.0`
    
    `pyproject.toml` 파일 내 작성
    
    ```powershell
    
    [tool.pytest.ini_options]
    asyncio_mode = "auto"
    asyncio_default_fixture_loop_scope = "session"
    ```
    
- `test.sh`
    
    ```powershell
    set -eo pipefail
    
    COLOR_GREEN=`tput setaf 2;`
    COLOR_NC=`tput sgr0;` # No Color
    
    echo "Starting black"
    poetry run black .
    echo "OK"
    
    echo "Starting ruff"
    poetry run ruff check --select I --fix
    poetry run ruff check --fix
    echo "OK"
    
    echo "Starting mypy"
    poetry run mypy .
    echo "OK"
    
    echo "Starting pytest with coverage"
    poetry run coverage run -m pytest
    poetry run coverage report -m
    poetry run coverage html
    
    echo "${COLOR_GREEN}All tests passed successfully!${COLOR_NC}"
    ```
    
    각각의 포멧터와 테스터들을 실행 전후로 `echo` 를 통해 시작과 완료를 알려 어디까지 실행 되었는지 알 수 있게 되어 있다
    
    마지막으로는 초록색의 문구로 완료 되었음을 알려준다.
    

## Github Actions

github에 push 할 때 마다 black 부터 pytest 까지 검사를 자동으로 실행 되도록 할 수 있다

- `.github/workflows/ci.yaml`
    
    ```yaml
    name: CI
    
    on:
      push:
    
    jobs:
      static-analysis:
        runs-on: ubuntu-22.04
        steps:
          - name: Check out the codes
            uses: actions/checkout@v2
    
          - name: Setup python environment
            id: setup-python
            uses: actions/setup-python@v2
            with:
              python-version: "3.13"
    
          - name: Install Poetry
            run: |
              curl -sSL https://install.python-poetry.org | python3 - --version 1.8.5
    
          - name: Register Poetry bin
            run: echo "${HOME}/.poetry/bin" >> $GITHUB_PATH
    
          - name: Install dependencies
            run: poetry install --no-root
    
          - name: Run Black
            run: poetry run black . --check
    
          - name: Run Ruff
            run: |
              poetry run ruff check --select I
              poetry run ruff check
    
          - name: Run Mypy
            run: poetry run mypy .
    
      test:
        runs-on: ubuntu-22.04
        steps:
          - name: Check out the codes
            uses: actions/checkout@v2
    
          - name: Setup python environment
            id: setup-python
            uses: actions/setup-python@v2
            with:
              python-version: "3.13"
    
          - name: Install Poetry
            run: |
              curl -sSL https://install.python-poetry.org | python3 - --version 1.8.5
    
          - name: Register Poetry bin
            run: echo "${HOME}/.poetry/bin" >> $GITHUB_PATH
    
          - name: Install dependencies
            run: poetry install --no-root
    
          - name: Run tests
            run: |
              poetry run coverage run -m pytest .
              poetry run coverage report -m
    
    ```
    
- `on: push` → 위의 코드가 `push` 할 때 마다 실행 [https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions#on](https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions#on)
- `jobs`→ 하나의 workflow 는 여러개의 job 으로 구성됩니다. [https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions#jobs](https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions#jobs)
    - 2개의 job 을 생성했습니다. `static-analysis` 와 `test` job 을 2개로 쪼갠 이유는 실행 속도를 개선하기 위해서 입니다. 프로젝트가 점점 커지게 되면 가장 오래 걸리는 작업이 mypy 실행과 전체 단위 테스트 실행인데, 이 둘을 서로 쪼개 병렬로 실행하면 전체 CI 가 더 빨리 끝납니다.
- `runs-on` → job 이 실행되는 machine 을 의미합니다. [https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions#jobsjob_idruns-on](https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions#jobsjob_idruns-on)
- `steps` → 하나의 job 은 여러개의 step 으로 구성됩니다. step 은 명령을 실행하거나 다른 action 을 실행합니다.
- `uses` → 실행할 action 을 가리킵니다.
- `with` → action 에 전달할 parameter 변수입니다.
- `run` → 실행할 명령어입니다.
- `run: |` → yaml 문법입니다. `|` (파이프라인)을 사용해 value 가 여러 줄(multiline) 이라는 것을 의미합니다.