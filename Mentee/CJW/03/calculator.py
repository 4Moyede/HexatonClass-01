global_number = 0


class calculator:

    def add(self, input_number):
        global global_number
        global_number = global_number + input_number
        return global_number

    def sub(self, input_number):
        global global_number
        global_number = global_number - input_number
        return global_number

    def mul(self, input_number):
        global global_number
        global_number = global_number * input_number
        return global_number

    def div(self, input_number):
        global global_number
        global_number = global_number / input_number
        return global_number

    def to_zero(self):
        global global_number
        global_number = 0
        return global_number


print('초기의 값은 0입니다')

object = calculator()

while True:
    sign = input('기호를 입력해주세요(+, -, /, *, CE ) : ')

    input_number = int(input('숫자를 입력해주세요 : '))
    end = input('계산 결과를 얻고 싶다면 등호를 입력해주세요 :')

    if end == '=':
        if sign == '+':
            object.add(input_number)
            print(global_number)

        elif sign == '-':
            object.sub(input_number)
            print(global_number)

        elif sign == '*':
            object.mul(input_number)
            print(global_number)

        elif sign == '/':
            object.div(input_number)
            print(global_number)

    reset = input('계산기를 종료하고 싶으면 END, 계속하시려면 아무키, 처음부터 다시 계산하고 싶으면 CE를 입력해주세요 : ')
    if reset == 'END':
        break

    elif reset == 'CE':
        object.to_zero()
        print(global_number)
