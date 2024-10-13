# Calculator 프로젝트

이 프로젝트는 기본적인 산술 연산을 수행할 수 있는 **일반 계산기**와 고급 수학 연산을 지원하는 **공학 계산기**를 구현한 Python 코드입니다.

## 주요 기능

### 1. 일반 계산기 (Calculator)
- **덧셈 (`add`)**: 여러 숫자를 더합니다.
- **뺄셈 (`subtract`)**: 첫 번째 숫자에서 나머지 숫자들을 차례대로 뺍니다.
- **곱셈 (`multiply`)**: 입력받은 모든 숫자를 곱합니다.
- **나눗셈 (`divide`)**: 첫 번째 숫자를 나머지 숫자들로 차례대로 나눕니다.

### 2. 공학 계산기 (EngineeringCalculator)
일반 계산기의 기능 외에 추가로 고급 수학 연산을 지원합니다.
- **제곱근 (`square_root`)**: 입력값의 제곱근을 계산합니다.
- **거듭제곱 (`power`)**: 첫 번째 숫자를 두 번째 숫자의 거듭제곱으로 계산합니다.
- **로그 (`log`)**: 입력값의 로그(log)를 계산합니다 (기본값은 상용 로그).
- **자연로그 (`ln`)**: 입력값의 자연 로그(ln)를 계산합니다.
- **삼각함수 (사인, 코사인, 탄젠트)**: 각도(라디안 또는 도)로 사인, 코사인, 탄젠트를 계산합니다.

## 설치 및 사용 방법

1. 저장소를 클론합니다.
   ```bash
   git clone https://your-repository-url.git
   ```

2. 프로젝트 디렉토리로 이동합니다.

   ``` bash
   cd your-repository
   ```

3. Python 파일을 실행하거나 프로젝트에서 클래스를 임포트하여 사용합니다.


## 예시 코드
``` python
from calculator import Calculator, EngineeringCalculator

# 기본 계산기 사용 예시
calc = Calculator(precision=2, return_float=True)
result = calc.add(10, 5.1264, 3)
print(result)  # 출력: 18.13

# 공학 계산기 사용 예시
eng_calc = EngineeringCalculator()
sqrt_result = eng_calc.square_root(16)
print(sqrt_result)  # 출력: 4.0
```

## 메서드 설명
- Calculator 클래스
  - add(*args, **kwargs): 입력된 모든 숫자를 더합니다.
  - subtract(*args, **kwargs): 첫 번째 숫자에서 나머지 숫자들을 뺍니다.
  - multiply(*args, **kwargs): 입력된 모든 숫자를 곱합니다.
  - divide(*args, **kwargs): 첫 번째 숫자를 나머지 숫자들로 나눕니다.
- EngineeringCalculator 클래스
  - square_root(x): 입력값의 제곱근을 계산합니다.
  - power(x, y): 첫 번째 숫자의 두 번째 숫자 거듭제곱을 계산합니다.
  - log(x, base=10): 주어진 밑(base)으로 입력값의 로그를 계산합니다.
  - ln(x): 입력값의 자연 로그를 계산합니다.
  - sin(x), cos(x), tan(x): 입력값의 각도에 대해 삼각함수 값을 계산합니다.


## 라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참고하세요.
