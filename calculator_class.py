# 두 수를 입력받아 사칙 연산하는 계산기 프로그램 객체를 이용하여 작성
# 클래스 선언
class Calculator(): # 클래스 선언
    # 속성, 변수
    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y

    def add(self):
        print('\n === add ===')
        print('num1 + num2 = ', self.num1 + self.num2)

    def substract(self):
        print('\n === substract ===')
        print('num1 - num2 = ', self.num1 - self.num2)

# 클래스 실행(사용)
# 객체 생성 : 클래스 이름(속성값...)
calc1 = Calculator(10, 20)
print('clac.num1:', calc1.num1)
print('clac.num1:', calc1.num2)

#객체의 기능 실행
calc1.add()
calc1.substract()


calc2 = Calculator(2000, 45)
print('clac.num1:', calc2.num1)
print('clac.num1:', calc2.num2)
calc2.add()
calc2.substract()