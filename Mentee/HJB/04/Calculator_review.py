from Error import WrongOperatorError, NumberTurnError

# private, 사용자 모듈 import, property, setter, magic method(__str__)
# __name__ == __main__ -> Error.py 파일에 print(__name__) 추가를 하고

class Calculator: # 클래스 생성!
	def __init__(self): # 생성자 이용해서 인스턴스 생성! , 내부에서만 접근 가능 (private)
		self.__result = 0 # 초기값은 0으로 설정
		self.__operator = None # 연산기호 초기값은 None
		self.__turn = 'NUMBER' # 이 변수도 초기값을 'NUMBER'로 설정
		self.__is_finished = True # 
		self.__running = True

		self.main()

	def __add(self, number): # 덧셈 하는 함수, 객체에 해당하는 self와 실제 매개변수인 number로 이루어져 있음
		self.__result += number # 덧셈 실시

	def __sub(self, number): # 위와 같음
		self.__result -= number

	def __mul(self, number): # 위와 같음
		self.__result *= number

	def __div(self, number): # 위와 같음
		self.__result /= number

	def __operate(self, number): # 연산기호(operator)가 뭐냐에 따라 어떤 함수를 발동할지 선택함
		if self.__operator == '+':
			self.__add(number)
		elif self.__operator == '-':
			self.__sub(number)
		elif self.__operator == '*':
			self.__mul(number)
		elif self.__operator == '/':
			self.__div(number)
		
	def __distinguish_input(self, input_val):
		try:
			if input_val == 'END': # END 입력받으면 아래 메시지 출력하고 11번째 줄의 변수가 False로 변함
				print('Program Terminated..')
				self.__running = False
				return
			
			if self.__turn == 'NUMBER': # __turn 값이 'NUMBER'면 
				if input_val.isdigit(): # input_val 이 숫자인지 판단하고 숫자면 self.result에 값 저장하고 
					self.result = int(input_val)
					self.__turn = 'OP' # __turn의 값을 'OP'로 바꿈
				else: # input_val이 숫자가 아니면 
					if self.__is_finished: # __is_finished가 ture이면
						self.operator = input_val # 입력받은 연산기호를 input_val에 대입하고
						self.__turn = 'NUMBER' # __turn은 'NUMBER가 된다. 
					else: # __is_finished가 false 이면
						raise NumberTurnError(input_val) # error.py에 정의되어 있는 error 띄워줌
			elif self.__turn == # 'OP': __turn이 'OP' 이면
				self.operator = input_val # 연산기호를 operator 에 저장하고
				self.__turn = 'NUMBER' # __turnㅇ[] NUMBER을 대입
		except NumberTurnError as e: # 아래 두 가지의 오류는 숫자나 연산기호를 잘못 입력했을 때 발동
			print(e)
		except WrongOperatorError as e:	
			print(e)

	@property # 프로퍼티를 이용해 __operator 값을 가져온다. 원래 private라 못가져옴
	def operator(self):
		return self.__operator

	@property # 프로퍼티를 이용해 __result 값을 가져온다. 원래 private라 못가져옴
	def result(self):
		return self.__result

	@result.setter
	def result(self, number):
		if self.__is_finished: # __is_finished가 ture이면 __result에 number 대입
			self.__result = number
		else: # __is_finished가 flase 이면 __operate(number)를 실행함
			self.__operate(number)
		self.__is_finished = False # self.__is_finithed를 false로 지정
			
	@operator.setter
	def operator(self, op):
		if op == '=': # op가 '='면
			print('[result]', self.result, '\n') # 해당 형식대로 print
			self.__is_finished = True # __is_finished를 true로 바꿈
		elif op in ['+', '-', '*', '/']: # op가 등호가 아닌 다른 연산자이면
			self.__operator = op # __operator에 op를 대입하고
			self.__is_finished = False # __is_finished를 false로 바꿈
		else: # 아무것도 아니면 에러 출력
			raise WrongOperatorError(op)

	def main(self):
		print("\nThe Calculator Program has been started.")
		print("Input number or operator")
		print("If you want to end the program, input 'END'\n")
		while self.__running: # __running 이 ture인 동안 계속 반복, running의 초기값은 true 였음
			input_val = input("input: ") # input 받는다.
			self.__distinguish_input(input_val) # self.__distinguish_input(input_val)를 실행한다.


if __name__ == "__main__":
	cal_obj = Calculator()

# 인터프리터에서 직접 실행하면, __name__에 __main__이 들어감
# import 해서 실행하면, __name__변수에 “임포트한 파일명”이 담겨서 프린트됨
# __name__ == __main__이 true가 될 조건은 인터프리터에서 직접 실행했을 경우이다.