import math

# 일반계산기
class Calculator:
    def __init__(self, precision: int = None, return_float: bool = False):
        """
        Calculator 클래스의 생성자.

        :param precision: 결과값의 소수점 자릿수 (기본값: None)
        :param return_float: True일 경우 결과값을 float 타입으로 반환 (기본값: False)
        """
        self.default_precision = precision  # 기본 precision 설정
        self.default_return_float = return_float  # 기본 return_float 설정

    def add(self, *args, **kwargs):
        # 모든 숫자 더하기
        result = sum(args)

        # kwargs 처리
        precision = kwargs.get('precision', None)  # 기본값: None (소수점 처리 안함)
        return_float = kwargs.get('return_float', False)  # 기본값: False (정수로 반환)

        # 결과를 소수로 반환할지 여부에 따른 처리
        if return_float:
            result = float(result)

        # 소수점 자릿수 조정
        if precision is not None and isinstance(precision, int):
            result = round(result, precision)

        return result

    def subtract(self, *args, **kwargs):
        if len(args) < 2:
            return "Error: 두 개 이상의 값이 있어야 합니다."

        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)

        # 첫 번째 값을 기준으로 차를 계산
        result = args[0]
        for num in args[1:]:
            result -= num

        # precision이 설정된 경우 소수점 자릿수 반올림
        if precision is not None:
            result = round(result, precision)

        # return_float가 True일 경우 float으로 변환
        if return_float:
            result = float(result)

        return result

    def multiply(self, *args, **kwargs):
        if len(args) < 1:
            return "Error: 두개 이상의 값이 있어야 합니다."

        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)

        # 첫 번째 값을 기준으로 곱셈 결과 초기화
        result = 1
        for num in args:
            result *= num

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result

    def divide(self, *args, **kwargs):
        if len(args) < 2:
            return "Error: 두 개 이상의 값이 있어야 합니다."

        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)

        # 첫 번째 값을 기준으로 나누기 결과 초기화
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Error: 0으로 나눌수 없습니다."
            result /= num

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result


## 공학계산기
class EngineeringCalculator(Calculator):
    def __init__(self, precision: int = None, return_float: bool = False):
        """
        EngineeringCalculator 클래스의 생성자.

        :param precision: 결과값의 소수점 자릿수 (기본값: None)
        :param return_float: True일 경우 결과값을 float 타입으로 반환 (기본값: False)
        """
        super().__init__(precision, return_float)


    # 오버라이드
    def divide(self, *args, **kwargs):
        if len(args) < 2:
            return "Error: 2개 이상의 값을 입력해야 합니다."

        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)

        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise DivisionByZeroError("Error: 0으로 나눌수 없습니다.")
            result /= num

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result
    
    # 제곱근
    def square_root(self, x, **kwargs):
        if x < 0:
            return "Error: 입력값은 0보다 커야합니다."

        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)

        result = math.sqrt(x)

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result

    # 제곱
    def power(self, x, y, **kwargs):
        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)

        result = math.pow(x, y)

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result

    # 로그
    def log(self, x, base=10, **kwargs):
        if x <= 0:
            return "Error: 입력값은 0보다 커야합니다."

        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)

        result = math.log(x, base)

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result

    # 자연로그
    def ln(self, x, **kwargs):
        if x <= 0:
            return "Error: 입력값은 0보다 커야합니다."

        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)

        result = math.log(x)

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result

    # 사인
    def sin(self, x, **kwargs):
        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)
        angle_unit = kwargs.get('angle_unit', 'radian')

        if angle_unit == 'degree':
            x = math.radians(x)

        result = math.sin(x)

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result

    # 코사인
    def cos(self, x, **kwargs):
        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)
        angle_unit = kwargs.get('angle_unit', 'radian')

        if angle_unit == 'degree':
            x = math.radians(x)

        result = math.cos(x)

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result

    # 탄젠트
    def tan(self, x, **kwargs):
        precision = kwargs.get('precision', None)
        return_float = kwargs.get('return_float', False)
        angle_unit = kwargs.get('angle_unit', 'radian')

        if angle_unit == 'degree':
            x = math.radians(x)

        result = math.tan(x)

        if precision is not None:
            result = round(result, precision)

        if return_float:
            result = float(result)

        return result


# 파일 직접 실행시 데모
if __name__ == "__main__":
    # 데모 코드
    calc = Calculator()
    print("Basic Calculator Demo:")
    print("calc = Calculator()")
    print("calc.add(10, 5.1264, 3, precision=2, return_float=True) #결과 : {0}".format(calc.add(10, 5.1264, 3, precision=2, return_float=True)))
    print("calc.subtract(10, 5.1264, 3, precision=2, return_float=True) #결과 : {0}".format(calc.subtract(10, 5.1264, 3, precision=2, return_float=True)))
    print("calc.multiply(10.1234, 5.5678, precision=2, return_float=True) #결과 : {0}".format(calc.multiply(10.1234, 5.5678, precision=2, return_float=True)))
    print("calc.divide(100.1234, 5.5678, precision=2, return_float=True) #결과 : {0}".format(calc.divide(100.1234, 5.5678, precision=2, return_float=True)))

    eng_calc = EngineeringCalculator()
    print("\nEngineering Calculator Demo:")
    print("eng_calc = EngineeringCalculator()")
    print("eng_calc.square_root(16) #결과 : {0}".format(eng_calc.square_root(16)))
    print("eng_calc.power(2, 3) #결과 : {0}".format(eng_calc.power(2, 3)))
    print("eng_calc.log(8, base=2) #결과 : {0}".format(eng_calc.log(8, base=2)))
    print("eng_calc.ln(1) #결과 : {0}".format(eng_calc.ln(1)))
    print("eng_calc.sin(30) #결과 : {0}".format(eng_calc.sin(30)))
    print("eng_calc.cos(60) #결과 : {0}".format(eng_calc.cos(60)))
    print("eng_calc.tan(45) #결과 : {0}".format(eng_calc.tan(45)))

    print("\nDivisionByZeroError 예외 처리 예제")
    print_str = """
try:
    print(eng_calc.divide(100, 5, 0))
except DivisionByZeroError as e:
    print(e)  # "Error: 0으로 나눌 수 없습니다.."
"""
    print(f"{print_str}")