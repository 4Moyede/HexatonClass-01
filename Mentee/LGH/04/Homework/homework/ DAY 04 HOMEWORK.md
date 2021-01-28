지난주 ISSUE
===========

1.set 함수와 unique 함수에 대하여
---------------------------
지우 멘티님이 set 함수와 unique 함수를 비교해 주셨다. 에어비앤비 과제에서 나 또한 set 함수와 unique 함수를 동시에 썼는데 이 이슈를 보고 쉽게 정리가 되었다. 

set 함수
1. 순서가 없음
2. 집합 안에서 unique한 값을 가짐
3. mutable 객체

unique 함수
Python 데이터 분석 라이브러리를 사용하는 경우 사용가능하고
pandas.unique(value)의 함수 형태를 가지며, value는 1d-array 형태로 들어가야한다.( np.array, list , Series 가능)

이 두 함수의 큰 차이점은 set 함수는 순서가 없지만 unique는 순서가 있게 중복을 제거한다는 것이었다. 

2.list 전체를 for문에 돌리는 방법
-----------------
성준 멘티님이 리스트를 인덱스를 이용해 불러왔고, 그 당시에는 칼럼이 8개로 정해져 있어 range(8)을 썼지만, 멘토님의 의견에 따라 리스트가 변할 때까지 함께 쓸 수 있게 range(len(remake_index))를 이용하면 훨씬 더 좋을 것이라고 느꼈다. 

3.함수 이름 지을 때의 문제점
--------
멘토님이 나의 코드를 보시고 많은 함수 이름에 대해 문제점을 지적해주셨다. 사실 함수를 만들 때 코드를 짜는 것보다 함수 이름을 어떻게 하면 더 쉬우면서도 간결하고 간단하게 지을지에 대해 고민을 많이 했던 것 같다. 노력을 많이 한 함수 이름임에도 많이 부족했었던 것 같다. 
결론적으로 멘토님이 말씀해주신 것은
1. 함수는 무조건 동사를 앞에다 쓰기
    - 함수 이름이 info_weather 처럼 명사로만 이루어져 있다면 날씨 정보를 set 하는 함수인지, get 혹은 del 하는 함수인지 전혀 알 수가 없다고 하셨다.
2. 함수 이름을 단조롭게 쓰지 않기
    - 함수 이름을 단조롭게 쓰면 나중에 협업을 할 때 무조건 충돌이 생긴다고 하셨다..... 나도 사실 내가 짠 코드를 다시 볼 때 함수 옆에 주석을 달아놓지 않으면 그게 무슨 함수였는지 잘 기억이 나지 않은 경험이 있다. 나조차도 이런데 협업하는 다른 사람들은 더욱 알아보기 힘들것이라는 걸 느꼈다... 어렵겠지만,,,, 노력해야지..!
    
4.가독성 좋은 코드 짜기
---------------
<pre><code>
print("We select only Good information about airbnb dataset : ")
print("1  :  room_type")
print("2  :  neighborhood")
print("3  :  reviews")
print("4  :  overall_satisfaction")
print("5  :  accommodates")
print("6  :  bedrooms")
print("7  :  price")
print("8  :  minstay")
</code></pre>
이 코드는 내가 쓴 코드인데 역시 더 좋은 방법이 있을 것 같다는 생각을 했다. 가독성이 좋지 않기 때문이다. 이 문제에 대해 지우 멘티님이 enumerate 함수에 대한 이슈를 올렸다. 사실 이전 지우 멘티님의 코드를 보면서 for i in range(len())이라는 코드가 좋지 않다는 의견을 남긴 적이 있었는데 그것과 더불에 같이 이슈에 올려 주셨다.
결과적으로 위에 내가 짠 코드는 
<pre><code>
for idx, column in enumerate(columns_list):
    print(idx+1, " : ", column)
    </code></pre>
로 짧게 구현할 수 있었다. 

이 enumerate 함수에 대해 좀 더 알아보면, '열거한다' 라는 의미로 순서가 있는 자료형을 입력을 받아 인덱스 값을 포함하는 객체로 리턴하게 된다. 여기서 순서 있는 자료형으로는 리스트, 튜플, 문자열이 될 것이다.

**********************************

멘티님들 review
=======
성준
----
가장 깔끔한 코드를 본 것 같습니다! 성준님의 코드를 처음 보고 저의 계산기 코드에서 아쉬운 점을 바로 찾을 수 있었어요.. 저의 계산기 코드로는 단순히 두 숫자만 계산하는것이 가능하다는 것을 느꼈습니다.. 추가로 reset 기능을 더 넣어준 것이 아주 인상 깊었습니다. 

지우
----
class에 to_zero라는 함수를 통해 쉽게 초기화를 시킨걸 보고 되게 똑똑하다는 생각이 들었습니다! 역시 마찬가지로 저의 계산기 코드의 문제점을 알 수 있는 코드였습니다.. 다만 초기값이 항상 0인것이 계산기가 돌아갈 때 문제가 있는것 같습니다!

재범
----
저와 같은 방법으로 가장 단순한 코드를 짠 것 같네요:) 연산기호에 연산기호가 아닌 다른 문자나 숫자가 들어가도 코드가 계속 진행되는 부분은 아쉽습니다.

덕규
----
기본적인 코드로 깔끔하게 잘 짠것 같아요! 근데 무한루프에서 빠져나오는 장치를 안 한것이 아쉽습니다!

*******************

멘토님 review
=======


```python
from Error import WrongOperatorError, NumberTurnError
class Calculator:
  def __init__(self): #생산자 메소드
		self.__result = 0 # 계산 결과값으로 초기값을 0으로 지정
		self.__operator = None # 연산기호로 초기값은 none로 지정
		self.__turn = 'NUMBER' # 숫자를 입력 받을지 기호를 입력받을지를 알려주는 변수, 초기값은 숫자
		self.__is_finished = True #계산기를 끝내는지에 대한 값으로 초기값 True로 지정
		self.__running = True	
    # 모두 언더바를 이용해서 private하게 설정 (외부에서는 접근을 할 수 없다.)
  	self.main()
    
    #여기부터는 연산 기호에 대한 함수
    #마찬가지로 모두 언더바를 이용해서 외부에서는 접근 불가능
	def __add(self, number): #더하기 함수, 결과에 number를 더해줌
		self.__result += number

	def __sub(self, number): #빼기 함수, 결과에 number를 빼줌
		self.__result -= number

	def __mul(self, number): #곱하기 함수, 결과에 number를 곱해줌
		self.__result *= number

	def __div(self, number): #나누기 함수, 결과에 number를 나누어줌
		self.__result /= number
	
	def __operate(self, number): 			#연산기호에 따라 어떤 연산함수(?)를 이용할지 정하는 함수
		if self.__operator == '+': 			# +일 때 더하기 함수 
			self.__add(number)
		elif self.__operator == '-': 		# -일 때 더하기 함수 
			self.__sub(number)
		elif self.__operator == '*': 		# *일 때 더하기 함수 
			self.__mul(number)
		elif self.__operator == '/': 		# /일 때 더하기 함수 
			self.__div(number)
	
	def __distinguish_input(self, input_val): #어렵다...
		try:
			if input_val == 'END': 									#input_val 이 END이면 
				print('Program Terminated..')				 	# 'porgram terminated..'를 출련하고
				self.__running = False 								#__runnging 값은 Fales가 됨
				return
		
			if self.__turn == 'NUMBER': 						#__turn 값이 NUMBER(초기값)이면
				if input_val.isdigit(): 							#input_val 이 숫자라면 (isdigit는 숫자인지를 판단해주는 함수)
					self.result = int(input_val) 				#result에 input_val 저장
					self.__turn = 'OP' 									#__turn 에는 OP 저장 
				else:																	#__turn 값이 초기값이 아니라면
					if self.__is_finished:							#__is_finished이 true 이면
						self.operator = input_val					#input_val은 operator에 저장 (입력받은 값이 연산기호)
						self.__turn = 'NUMBER'						#다음 입력은 숫자를 입력받아야함 
					else:																#아니면
						raise NumberTurnError(input_val)	#NumberTurnError을 실행(에러 모듈)
				elif self.__turn == 'OP':							#연산기호를 넣을 차례라면	
					self.operator = input_val						#input_val을 operator에 저장
					self.__turn = 'NUMBER'							#다음 턴을 숫자로 넘겨줌
          
		except NumberTurnError as e:							#try문에서의 조건 이외의 입력을 넣어주면 except문이 실행됨 
			print(e)																#여기서 에러의 종류는 NumberTurnError, WrongOperatorError
		except WrongOperatorError as e:						#에러 코드를 잘 모르지만 에러명만 보고도 무슨 에러일지 대충 감이 잡히네요..
			print(e)																#작명의 중요성을 다시 한번 느꼈습니다..!

	@property																		#property는 값을 가저오는 메소드이므로 proterty를 이용해서
	def operator(self):													#클래스의 operator 값과 result 값을 가져온다.
		return self.__operator

	@property
	def result(self):
		return self.__result

	@result.setter															#result 값을 저장한다. 위에서 클래스 내부에 private 한 속성을 만들었기 때문에
	def result(self, number):										#setter 메소드를 사용한다. (보편적인 개체지향프로그래밍 방법!!)
		if self.__is_finished:										#__is_finished의 값이 true라면 
			self.__result = number									#__result에는 number 가 저장되고
		else:																			#고것이 아니라면
			self.__operate(number)									#__operate(number)가 실행되면서 
		self.__is_finished = False								#__is_finished의 값이 False가 된다. 
		
	@operator.setter														#설명 생략..해도 될까요..?
	def operator(self, op):											
		if op == '=':															#만약 op가 =이라면
			print('[result]', self.result, '\n')		#print('[result]', self.result, '\n')이 프린트문 출력
			self.__is_finished = True								#self.__is_finished에 True 저장
		elif op in ['+', '-', '*', '/']:					#만약 op가 ['+', '-', '*', '/']라면
			self.__operator = op										#self.__operator는 op가 되고
			self.__is_finished = False							#self.__is_finished에는 False 저장
		else:																			#다 아니면
			raise WrongOperatorError(op)						#에러 뜨게 함

	def main(self):
		print("\nThe Calculator Program has been started.")
		print("Input number or operator")
		print("If you want to end the program, input 'END'\n")
		while self.__running:
			input_val = input("input: ")
			self.__distinguish_input(input_val)
    

if __name__ == "__main__":
	cal_obj = Calculator() 
  #해당 모듈이 임포트된 경우가 아니라 인터프리터에서 직접 실행된 경우에만, if문 이하의 코드를 돌리라는 명령.
  #즉 직접 이 파일을 실행해야 한다는 의미..?!?!!!!!!!!!!

```

