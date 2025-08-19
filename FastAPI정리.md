# FastAPI란

생성일시: 2025/08/18 17:00 (GMT+9)
생성자: 강한손
최종 업데이트 시간: 2025년 8월 19일

## Meetifyr

---

여러 사용자가 같은 화면을 공유하며 일정을 맞출 수 있도록 도와주는 애플리케이션

일정 참여 불가한 날과 가능한 날 선호하는 날등을 종합하여 가장 적당한 날을 추천해준다

## Poetry

poetry공식홈페이지: ([https://python-poetry.org/](https://python-poetry.org/))

---

python 프로젝트의 의존성 관리를 위한 툴이다

- 프로젝트마다 별도의 가상 환경을 자동으로 생성해 주어, 환경 충돌 위험을 줄여줌
- pyproject.toml 로 프로젝트를 관리하는 것을 도와줌
- black, isort, mypy, ruff, coverage, pytest 설정을 pyproject.toml에 두어 관리할 수 있게 함

```bash
curl -sSL https://install.python-poetry.org | python3 - --version 1.8.5 
```

위의 방법으로 안 된다면

아래 방법으로 경로 지정후 진행 하는 방법도 있다

```bash
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
```

```bash
source ~/.zshrc
```

```bash
pip3 install poetry
```

poetry 설치 확인 (2025.08.18기준 **2.1.4버전을 확인 할 수 있다.)**

```bash
poetry --version
```

## Code Formatter

---

- BLACK
    - 코드 포맷터로, 여러 명이 한 프로젝트에서 작업할 때 일관된 코드 스타일을 유지할 수 있게 해줍니다.
    - 프로젝트 코드 에디터 내 터미널에서 다음 명령어로 설치합니다.
    
    ```bash
    poetry add --group=dev black==24.10.0
    ```
    
    ---
    
    - 실행 명령어
    
    ```bash
    poetry run black .
    ```
    
    - 다음 코드를 실행해 보면
    
    ```python
    print("Life is Toooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo Short")
    ```
    
    - 아래와 같이 줄 바꿈되어 정리되는 것을 확인할 수 있습니다.
    
    ```python
    print(
    "Life is Toooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo Short"
    )
    ```
    
    참고 공식 문서:
    
    ([https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file))
    
    `pyproject.toml` 파일에서 허용할 문자 길이를 다음과 같이 설정할 수 있습니다.
    
    ```toml
    [tool.black]
    line-length = 120
    ```
    
- RUFF
    
    `ruff`는 `formatter`와 `linter`의 기능을 모두 갖고 있습니다.
    
    `linter`는 소스 코드를 분석하여 잘못 작성된 부분을 자동으로 수정하거나 경고해 줍니다.
    
    'l', 'i', 'o'를 함수명으로 사용하는 것을 E741 규칙으로 제한합니다(가독성이 떨어지기 때문).
    
    #noqa 주석을 사용해 특정 코드 라인에 대한 검사를 건너뛸 수 있습니다.
    
    ```bash
    poetry add --group=dev ruff==0.8.2
    ```
    
    ---
    
    다음 명령어로 `ruff`의 기능 중 'I'(`isort`) 명령어를 실행할 수 있습니다.
    
    ```bash
    ruff check --select I --fix
    ```
    
    이 명령어는 import 문을 알파벳 순으로 정렬해 줍니다.
    
    관련 공식문서: ([https://docs.astral.sh/ruff/rules/#isort-i](https://docs.astral.sh/ruff/rules/#isort-i))
    
    ---
    
    사용 전
    
    ```python
    import sys
    import os
    ```
    
    사용 후
    
    ```python
    import os
    import sys
    ```
    
    `pyproject.toml` 파일에서 다음과 같이 코드 검사 설정을 추가할 수 있습니다.
    
    ```toml
    [tool.ruff]
    target-version = "py313"
    ```
    

## MYPY

---

코드 내의 함수의 return 타입을 확인해줄 수 있다.

다음을 통해 설치 할 수 있음

```bash
poetry add --group=dev mypy==1.13.0
```

---

어떠한 코드의 타입을 비교하여 사용자에게 알려줌

```python
my_int: int = 1
my_str: str = "abc"

my_list: list[str] = ["abc", "def"]

my_tuple: tuple[str, str] = ("abc", "def")

my_dict: dict[str, int] = {"a": 1, "b": 2}
```

mypy의 엄격함 수준을 조절할 수 있다

```toml
[tool.mypy]
plugins = ["pydantic.mypy"]
python_version = 3.13
strict = true
```

---