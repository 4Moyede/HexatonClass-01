```python
###Error.py
class WrongOperatorError(Exception):
    def __init__(self, err):
        self.input_val = err
    def __str__(self):
        error_msg = "\n"
        error_msg += 'Input VALUE ERROR.. wrong operator\n'
        error_msg += 'Your input : ' + str(self.input_val)
        error_msg += '\n'
        return error_msg


class NumberTurnError(Exception):
    def __init__(self, err):
        self.input_val = err
    def __str__(self):
        error_msg = "\n"
        error_msg += 'input VALUE ERROR.. input number\n'
        error_msg += 'Your input : ' + str(self.input_val)
        error_msg += '\n'
        return error_msg


# 1번의 경우
# if __main__ is __name__: #이 함수 자체가 오류가 있다면서 실행되지 않음
#     print("hello")

# 2번의 경우 #이 함수는 반면에 정상적으로 실행이 된다.
# print("hi")



###Calculator.py
from Error import WrongOperatorError, NumberTurnError #Error.py의 두 오류 클래스를 불러옴

# private, 사용자 모듈 import, property, setter, magic method(__str__)
# __name__ == __main__ -> Error.py 파일에 print(__name__) 추가를 하고

class Calculator:
	def __init__(self):
		self.__result = 0 #결과를 저장하는 변수
		self.__operator = None #연산자를 처리하는 변수
		self.__turn = 'NUMBER' 
		self.__is_finished = True
		self.__running = True 

		self.main()

	#네 함수는 계산하는 함수
	def __add(self, number):
		self.__result += number

	def __sub(self, number):
		self.__result -= number

	def __mul(self, number):
		self.__result *= number

	def __div(self, number):
		self.__result /= number 

	#연산자의 종류가 어떤지에 따라 위의 계산함수를 소환
	def __operate(self, number):
		if self.__operator == '+':
			self.__add(number)
		elif self.__operator == '-':
			self.__sub(number)
		elif self.__operator == '*':
			self.__mul(number)
		elif self.__operator == '/':
			self.__div(number)

	#프로그램 종료, 숫자, 연산자를 구별하는 함수	
	def __distinguish_input(self, input_val):
		try:
			if input_val == 'END': #END로 끝날시 프로그램 종료
				print('Program Terminated..')
				self.__running = False # running를 False라는 Boolean으로 바꾸면 프로그램이 종료됨을 추측가능
				return
			
			if self.__turn == 'NUMBER': #숫자로 바꿨을때
				if input_val.isdigit(): #isdigit = 받은문자열이 숫자인지 파악하는 내장함수
					self.result = int(input_val) #받은 숫자는 문자열이므로, int로 숫자로 바꿈
					self.__turn = 'OP' #OP를 받게끔 바꿈
				else: #isdigit가 false일때
					if self.__is_finished: #init에 선언되어있던 Boolean
						self.operator = input_val #이건 문자열이기에 그대로 받음
						self.__turn = 'NUMBER' #이제 다시 숫자를 받게끔 바꿈
					else:
						raise NumberTurnError(input_val) 
			elif self.__turn == 'OP': #문자로 바꿨을때
				self.operator = input_val #
				self.__turn = 'NUMBER'
		except NumberTurnError as e:
			print(e)
		except WrongOperatorError as e:	
			print(e)

	@property
	def operator(self):
		return self.__operator

	@property
	def result(self):
		return self.__result

	@result.setter
	def result(self, number):
		if self.__is_finished:
			self.__result = number
		else:
			self.__operate(number) 
		self.__is_finished = False #False로 바꾸게 되면 87번째 줄의 else가 실행되면서 NumberTurnError로 이동
			
	@operator.setter
	def operator(self, op):
		if op == '=':
			print('[result]', self.result, '\n')
			self.__is_finished = True
		elif op in ['+', '-', '*', '/']:
			self.__operator = op
			self.__is_finished = False
		else:
			raise WrongOperatorError(op)

	def main(self):
		print("\nThe Calculator Program has been started.")
		print("Input number or operator")
		print("If you want to end the program, input 'END'\n")
		while self.__running: #__running이 True일때만 이 계산기를 실행, 즉 END로 끝났을때 False로 바꿨으므로 더이상 실행되지 않음
			input_val = input("input: ")
			self.__distinguish_input(input_val) #75번째 줄 이하 구문 실행


if __name__ == "__main__": #아주 중요한 함수. 이 부분은 따로 main함수에 대한 markdown파일을 사용하여 정리하겠습니다!
	cal_obj = Calculator()
```
