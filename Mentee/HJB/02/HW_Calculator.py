class Calculator:

    def __init__(self, first, symbol, second): # 호출자
        self.first = first
        self.symbol = symbol
        self.second = second

    def symbol(self): # 연산 기호
        symbol = self.symbol
        return symbol

    def add(self): # 덧셈
        result = self.first + self.second
        return result

    def sub(self): # 뺄셈
        result = self.first - self.second
        return result

    def mul(self): # 곱셈
        result = self.first * self.second
        return result

    def div(self): # 나눗셈5
        result = self.first / self.second
        return result


while True:
    print('''
      원하는 계산을 입력하세요. (사칙연산만 가능)
                                             ''')
    a = Calculator( int(input("피연산자1 : ")), input("연산기호 : ") , int(input("피연산자2 : ")) )


    if (a.symbol == "+"):
        print("<결과> {} {} {} = {}".format(a.first, a.symbol, a.second, a.add()))
    if (a.symbol == "-"):
        print("<결과> {} {} {} = {}".format(a.first, a.symbol, a.second, a.sub()))
    if (a.symbol == "*"):
        print("<결과> {} {} {} = {}".format(a.first, a.symbol, a.second, a.mul()))
    if (a.symbol == "/"):
        print("<결과> {} {} {} = {}".format(a.first, a.symbol, a.second, a.div()))

    switch = input("계속하시려면 아무 키나, 끝내시려면 N를 입력하세요. ") 
    print("-------------------{} {}--------------------\n".format(switch, "입력"))
    if(switch == 'N' or switch == 'n'):
        print("계산기를 종료합니다.")
        break 