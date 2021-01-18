
class calculate:
    def __init__(self):
        self.result = 0

    def plus(self, num1, num2):
        self.result = num1 + num2
        return self.result

    def minus(self, num1, num2):
        self.result = num1 - num2
        return self.result

    def multi(self, num1, num2):
        self.result = num1 * num2
        return self.result

    def divide(self, num1, num2):
        if num2 == 0:
            print('0으로 나눌 수 없습니다.')
        else:
            self.result = num1 / num2
            return self.result

num_one = int(input('숫자를 입력하시오'))
operation = input('원하는 사칙연산을 입력하시오(예 : + ) : ')
num_two = int(input('숫자를 입력하시오'))
ending = input('등호를 입력하시면 결과가 산출됩니다.')


c = calculate()
while True:
    if ending == '=':
        if operation == '+':
            c.plus(num_one,num_two)
            print(c.result)
        elif operation == '-':
            c.minus(num_one,num_two)
            print(c.result)

        elif operation == '*':
            c.multi(num_one,num_two)
            print(c.result)

        elif operation == '/':
            c.divide(num_one,num_two)
            print(c.result)

        else:
            operation = input('사칙연산만 입력해주십시오 : ')
    break