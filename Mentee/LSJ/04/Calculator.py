from Error import WrongOperatorError, NumberTurnError

# private, 사용자 모듈 import, property, setter, magic method(__str__)
# __name__ == __main__ -> Error.py 파일에 print(__name__) 추가를 하고

class Calculator:
	def __init__(self):
		self.__result = 0
		self.__operator = None
		self.__turn = 'NUMBER'
		self.__is_finished = True
		self.__running = True

		self.main()

	def __add(self, number):
		self.__result += number

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
		
	def __distinguish_input(self, input_val):
		try:
			if input_val == 'END':
				print('Program Terminated..')
				self.__running = False
				return
			
			if self.__turn == 'NUMBER':
				if input_val.isdigit():
					self.result = int(input_val)
					self.__turn = 'OP'
				else:
					if self.__is_finished:
						self.operator = input_val
						self.__turn = 'NUMBER'
					else:
						raise NumberTurnError(input_val)
			elif self.__turn == 'OP':
				self.operator = input_val
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
		self.__is_finished = False
			
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
		while self.__running:
			input_val = input("input: ")
			self.__distinguish_input(input_val)


if __name__ == "__main__":
	cal_obj = Calculator()
