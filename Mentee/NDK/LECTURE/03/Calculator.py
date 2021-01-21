class calculate:
    def __init__(self,num):
        self.result = num

    def plus(self, num):
        self.result += num
        return self.result

    def minus(self, num):
        self.result -= num
        return self.result

    def multi(self, num):
        self.result = self.result * num
        return self.result

    def divide(self, num):
        if num == 0:
            print('0으로 나눌 수 없습니다.')
        else:
            self.result = self.result / num
            return self.result

num_two = int(input('숫자를 입력하시오'))


c = calculate(num_two)
while True:
    operation = input('원하는 사칙연산을 입력하시오(예 : + ) : ')
    num_one = int(input('숫자를 입력하시오'))
    ending = input('등호를 입력하시면 결과가 산출됩니다.')
    if ending == '=':
        if operation == '+':
            c.plus(num_one)
            print(c.result)
        elif operation == '-':
            c.minus(num_one)
            print(c.result)

        elif operation == '*':
            c.multi(num_one)
            print(c.result)

        elif operation == '/':
            c.divide(num_one)
            print(c.result)

        else:
            operation = input('사칙연산만 입력해주십시오 : ')

