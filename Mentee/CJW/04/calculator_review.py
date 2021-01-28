from Error import WrongOperatorError, NumberTurnError


# private, 사용자 모듈 import, property, setter, magic method(__str__)
# __name__ == __main__ -> Error.py 파일에 print(__name__) 추가를 하고

class Calculator:
    def __init__(self):           # 생산자 method (한 객체에 대한 인스턴스를 생성할 때 호출되는 것)
        # 더블 언더스코어를 사용하므로써 내부에서만 접근 가능(외부에서는 접근안됨) , public -> private
        self.__result = 0         # 계산 결과의 초기값을 0으로 지정해줌
        self.__operator = None    # 연산 기호의 초기값을 none으로 지정
        self.__turn = 'NUMBER'    # __turn의 초기값을 'NUMBER'로 지정 (이 변수는 input받을 차례가 숫자인지 기호인지 판단)
        self.__is_finished = True # 이 변수가 False값이 되면 계산을 수행하거나 예외시에 오류 발생
        self.__running = True     # 이 변수가 False값이 되면 입력받는 것을 멈춤

        self.main()

    # 더블 언더스코어를 사용하므로써 내부에서만 접근 가능(외부에서는 접근안됨) , public -> private
    def __add(self, number):     # 덧셈을 해주는 함수
        self.__result += number  # result 값에 number를 더해줌

    def __sub(self, number):     # 뺄셈을 해주는 함수
        self.__result -= number  # result 값에 number를 빼줌

    def __mul(self, number):     # 곱셈을 해주는 함수
        self.__result *= number  # result 값에 number를 곱해줌

    def __div(self, number):     # 나눗셈을 해주는 함수
        self.__result /= number  # result 값에 number를 나눠줌

    def __operate(self, number):    # 연산 기호에 따라 실행할 함수가 무엇인지 정희해주는 함수
        if self.__operator == '+':  # 연산 기호가 '+'라면 __add함수를 실행 (아래는 비슷한 코드이므로 생략)
            self.__add(number)
        elif self.__operator == '-':
            self.__sub(number)
        elif self.__operator == '*':
            self.__mul(number)
        elif self.__operator == '/':
            self.__div(number)

    def __distinguish_input(self, input_val):      # 인풋받는 값이 무엇인지 구분해주는 함수
        try:
            if input_val == 'END':                 # 'END'를 입력받으면
                print('Program Terminated..')      # 'Program Terminated..'를 출력하고
                self.__running = False             # self.__running = False 가 됨
                return

            if self.__turn == 'NUMBER':            # __turn이 'NUMBER'과 같다면 (초기값이 'NUMBER'임)
                if input_val.isdigit():            # input_val의 값이 숫자라면 True임(IF문 사용 : 만약 input_val이 숫자라면 )
                    self.result = int(input_val)   # input_val의 값을 정수형으로 result에 저장
                    self.__turn = 'OP'             # __turn은 'OP'가 됨 (: 다음 입력받을 차례는 연산기호라는 의미인듯)
                else:                              # input_val의 값이 숫자가 아니라면
                    if self.__is_finished:         # __is_finished의 값이 'True'와 같다면
                        self.operator = input_val  # 입력받은 연산 기호를 operator라는 변수에 저장
                        self.__turn = 'NUMBER'     # __turn는 'NUMBER'가 됨 (: 다음 입력받을 차례는 숫자)
                    else:                          # __is_finished의 값이 'True'와 같지 않다면 (: False라면 )
                        raise NumberTurnError(input_val)  # error.py에서 가져온 numberturnerror를 실행
            elif self.__turn == 'OP':              # __turn이 'OP'와 같다면
                self.operator = input_val          # 입력받은 연산 기호를 operator라는 변수에 저장
                self.__turn = 'NUMBER'             # __turn는 'NUMBER'가 됨 (: 다음 입력받을 차례는 숫자)
        except NumberTurnError as e:
            print(e)
        except WrongOperatorError as e:
            print(e)

# try에 적힌 조건문 이외의 입력이 발생하면 except문에 있는 예외라고 생각하여 NumberTurnError, WrongOperatorError 출력



#자바와 같은 객체 지향 언어에서는 외부로부터 바로 접근할 수 없는 prviate 객체 속성을 지원, 이러한 언어에서는 private 속성의 값을 읽고(get) 변경(set)하기 위해 getter 메서드와 setter 메서드를 사용
# 하지만, 파이썬에는 getter 메서드나 setter메서드가 없고, 파이썬에서 선언되는 모든 속성(변수)와 메서드는 public이기 때문. 파이썬에서는 사용자가 속성에 직접 접근을 막기 위해 getter 또는 setter 메서드 대신에 프로퍼티(property) 를 사용

    @property                             # 값을 가져오는 메서드
    def operator(self):                   # Calculator의 __operator 값을 가져온다.
        return self.__operator

    @property                             # 값을 가져오는 메서드
    def result(self):                     # Calculator의 __result 값을 가져온다.
        return self.__result

    @result.setter                        # 값을 저장하는 메서드
    def result(self, number):
        if self.__is_finished:            # __is_finished가 True라면
            self.__result = number        # __result에 number값 저장
        else:                             # __is_finished가 False라면
            self.__operate(number)        # self.__operate(number) 실행
        self.__is_finished = False        # __is_finished는 False

    @operator.setter                                     # 값을 저장하는 메서드
    def operator(self, op):
        if op == '=':                                    # op가 '='라면
            print('[result]', self.result, '\n')         # print문 출력
            self.__is_finished = True                    # __is_finished는 True
        elif op in ['+', '-', '*', '/']:                 # op가 '+', '-', '*', '/' 중 하나라면
            self.__operator = op                         # __operator는 op와 같고
            self.__is_finished = False                   # __is_finished는 False
        else:                                            # op가 '=','+', '-', '*', '/'중 아무것도 아니라면
            raise WrongOperatorError(op)                 # error.py에서 가져온 WrongOperatorError를 실행

    def main(self):
        print("\nThe Calculator Program has been started.")
        print("Input number or operator")
        print("If you want to end the program, input 'END'\n")
        while self.__running:                            # __running이 True인 동안 반복
            input_val = input("input: ")                 # input 받고 self.__distinguish_input(input_val)실행 (반복)
            self.__distinguish_input(input_val)


if __name__ == "__main__":
    cal_obj = Calculator()

# 모듈을 실행할 수 있는 방법은 직접 실행하거나 임포트하거나 둘 중 하나
# 인터프리터에서 직접 실행하면, __name__ 변수에 __main__이 담겨서 프린트되고
# 모듈에서 임포트해서 실행하면, __name__변수에 “임포트한 파일명”이 담겨서 프린트됨
# 즉, __name__ == __main__은 인터프리터에서 직접 실행했을 경우에만 아래 코드를 돌리라는 명령