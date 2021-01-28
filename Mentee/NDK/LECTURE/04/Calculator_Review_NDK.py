from Error import WrongOperatorError, NumberTurnError


# private, 사용자 모듈 import, property, setter, magic method(__str__)
# __name__ == __main__ -> Error.py 파일에 print(__name__) 추가를 하고

class Calculator:
    def __init__(self):
        self.__result = 0
        #계산 결과를 임시로 저장하는 역할을 할 변수
        self.__operator = None
        #연산기호를 저장하는 곳... 초기에는 None값
        self.__turn = 'NUMBER'
        #입력받는 값의 성격을 나타내는 곳.. 입력받을 값의 차례? 숫자를 받을 차례인지 연산자를 받을 차례인지
        self.__is_finished = True
        #변수 명이 상당히 인상깊다... 뭔가 계산이 끝나는 걸 의미하는 듯?
        self.__running = True
    # public 변수를 private 변수로 전환하기 위해, 언더 바 두개를 변수 이름 앞에 붙였음.
        self.main()

    def __add(self, number):
        self.__result += number
    # 함수를 정의할 때 역시 private 함수를 만들고 싶을 때, 정의된 함수 이름 앞에 언더 바 두개를 붙임.
    def __sub(self, number):
        self.__result -= number

    def __mul(self, number):
        self.__result *= number

    def __div(self, number):
        self.__result /= number

    def __operate(self, number):
        if self.__operator == '+':
            self.__add(number)
        elif self.__operator == '-':
            self.__sub(number)
        elif self.__operator == '*':
            self.__mul(number)
        elif self.__operator == '/':
            self.__div(number)
    # 여기까진 함수를 Private 함수로 한 것 이외에 저랑 비슷하게 짜신 것같아서 Pass-★ ㅎㅅㅎ
    def __distinguish_input(self, input_val):
        try:
            if input_val == 'END':
                print('Program Terminated..')
                self.__running = False
             # input_val 에 END가 입력되면, 출력문이 출력되면서, Self.__running이 False가 됨.
             # 그러면 뒤에서 나올 main에서 self.__running이 False가 되면서, while문이 종료.
                return

            if self.__turn == 'NUMBER':
                # 입력 받는 값이 number가 될 차례라면
                if input_val.isdigit():
                #.isdigit() -> 이 문자열이 숫자면 True, 아니면 False로 리턴 해주는 함수
                # if문과 함께 사용하여 이 문자열이 숫자인지를 판별하는데 사용...!!
                    self.result = int(input_val)
                    #입력 받은 값이 숫자이므로 이 값을 result에 저장.
                    self.__turn = 'OP'
                    # 전 차례에 숫자를 입력받았으니, 이번엔 연산기호를 받을 차례라는 뜻...
                else:
                    if self.__is_finished:
                        # is_finish값이 True가 되면
                        self.operator = input_val
                        # 입력 받은 값이 연산기호이므로 그것을 operator에 저장
                        self.__turn = 'NUMBER'
                        # 그리고 숫자를 받을 차례로 넘김
                    else:
                        raise NumberTurnError(input_val)
                    # 조건과 같이 입력을 받지 못했다면, error 모듈에서 가져온 numberturnerror를 실행..!
            elif self.__turn == 'OP':
                # 만약 turn 이  op(아마 operator를 의미하는듯..)라면
                self.operator = input_val
                #즉 입력받을 것이 연산기호 차례이므로 그것을 operator에 저장
                self.__turn = 'NUMBER'
                # 다음차례로 number를 받을 차례임을 알려줌
        except NumberTurnError as e:
            print(e)
        except WrongOperatorError as e:
            print(e)
        # try에 적힌 조건문 이외의 입력이 발생하면 except문에 있는 예외로 간주하여 정의한 오류가 발생
        # 코드를 실행시키지 못할 오류는 아니지만 의도적으로 발생시킨 오류로, 올바른 입력이 이루어져 원하는 결과를 얻을 수 있게끔 해줌.
    # 괴랄한 조건문이네요... 물론 이 계산기 코드를 팔면 제 계산기 코드보단 다기능, 친절한 계산기로 팔리겠지만
    # if문 너무 많아서 해석하는데 시간 많이 썼습니다....!ㅠㅠㅠㅠㅠㅠ
    @property
    def operator(self):
        return self.__operator
    # property를 이용해서 Class의 operator 값을 가져온다.
    @property
    def result(self):
        return self.__result
    # Property를 이용해서 Class의 result 값을 가져온다.
    @result.setter
    def result(self, number):
        if self.__is_finished:
            self.__result = number
        # self.__is_finished가 True가 되면, self.__result는 number값이 저장된다.
        else:
            self.__operate(number)
        # self.__is_finished가 True가 아니면, self.__operate 메소드로 number값을 계산
        self.__is_finished = False
    # setter를 이용해서 class 내부의 result값에 접근하여 저장하기 위함이다.
    @operator.setter
    def operator(self, op):
        if op == '=':
            print('[result]', self.result, '\n')
            self.__is_finished = True
        # 만약 op값이 '='라면, '[result]', self.result, '\n'를 출력하고, self.__is_finished는 True가 된다.
        elif op in ['+', '-', '*', '/']:
            self.__operator = op
            self.__is_finished = False
        # 만약 op라는 객체가 ['+', '-', '*', '/'] 이 리스트의 요소중에 있다면,
        # self.__operator에 op의 값이 저장되고, self.__is_finished는 False가 된다.
        else:
            raise WrongOperatorError(op)
        # 이외의 op의 경우는 예외로 간주하여 WrongOperatorError가 발생한다.
    # setter를 이용해서 class 내부의 operator값에 접근하여 저장하기 위함이다.
    def main(self):
        print("\nThe Calculator Program has been started.")
        print("Input number or operator")
        print("If you want to end the program, input 'END'\n")
        while self.__running:
            input_val = input("input: ")
            self.__distinguish_input(input_val)
    # 너무 뒤에 있어서 main이라는 메소드가 class에 포함되는지 잊어버릴뻔...!
    # class가 불러들여지면 가장 먼저 실행되는 부분인거 같다...!


if __name__ == "__main__":
    cal_obj = Calculator()

#__name__은 파이썬에서 내장변수로써의 역할을 한다. __name__은 각각 두가지의 값을 갖게되는데,
# 만약 직접 실행되는 파일의 경우 __name__에는 __main__이라는 값이 저장된다.
# import된 파일의 경우 __name__은 해당 모듈의 파일명이 저장된다.
# 즉 위 조건문은 '직접 이 calculator 파일을 실행'했을 경우에만 class가 실행된다는 의미인 것 같다.