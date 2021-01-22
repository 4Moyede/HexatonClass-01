class calculator :

    def __init__(self):
        self.result = 0

    def add(self, input_number):
        self.result = self.result + input_number
        return self.result

    def sub(self, input_number):
        self.result = self.result - input_number
        return self.result

    def mul(self, input_number):
        self.result = self.result * input_number
        return self.result

    def div(self, input_number):
        if input_number == 0 :
            print('Error')
        else :
            self.result = self.result/input_number

    def to_zero(self, input_number):
        self.result = 0
        return self.result

print('초기의 값은 0입니다')


cal = calculator()

while True:
    sign = input('기호를 입력해주세요( +, -, /, * ) : ')
    input_number = int(input('숫자를 입력해주세요 : '))
    end = input('계산 결과를 얻고 싶다면 등호를 입력해주세요 :')

    if end == '=':
        if sign == '+':
            print(cal.add(input_number))

        elif sign == '-':
            print(cal.sub(input_number))

        elif sign == '*':
            print(cal.mul(input_number))

        elif sign == '/':
            print(cal.div(input_number))

    else :
        print('Error')

    reset = input('계산기를 종료하고 싶으면 END, 계속하시려면 아무키, 처음부터 다시 계산하고 싶으면 CE를 입력해주세요 : ')
    if reset == 'END':
        break

    elif reset == 'CE':
        print(cal.to_zero(input_number))
