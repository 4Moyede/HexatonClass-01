<<<<<<< HEAD
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

    switch = str(input("계속하시려면 아무 키나, 끝내시려면 N를 입력하세요. ")) 
    print("-------------------{} {}--------------------\n".format(switch, "입력"))
    if(switch == 'N' or switch == 'n'):
        print("계산기를 종료합니다.")
        break 
=======
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "experienced-rubber",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "      원하는 계산을 입력하세요. (사칙연산만 가능)\n",
      "                                             \n",
      "피연산자1 : 5\n",
      "연산기호 : *\n",
      "피연산자2 : 2\n",
      "<결과> 5 * 2 = 10\n",
      "계속하시려면 아무 키나, 끝내시려면 N를 입력하세요. \n",
      "------------------- 입력--------------------\n",
      "\n",
      "\n",
      "      원하는 계산을 입력하세요. (사칙연산만 가능)\n",
      "                                             \n",
      "피연산자1 : 4\n",
      "연산기호 : +\n",
      "피연산자2 : 7\n",
      "<결과> 4 + 7 = 11\n",
      "계속하시려면 아무 키나, 끝내시려면 N를 입력하세요. \n",
      "------------------- 입력--------------------\n",
      "\n",
      "\n",
      "      원하는 계산을 입력하세요. (사칙연산만 가능)\n",
      "                                             \n",
      "피연산자1 : 8\n",
      "연산기호 : /\n",
      "피연산자2 : 3\n",
      "<결과> 8 / 3 = 2.6666666666666665\n",
      "계속하시려면 아무 키나, 끝내시려면 N를 입력하세요. \n",
      "------------------- 입력--------------------\n",
      "\n",
      "\n",
      "      원하는 계산을 입력하세요. (사칙연산만 가능)\n",
      "                                             \n",
      "피연산자1 : 4\n",
      "연산기호 : -\n",
      "피연산자2 : 1\n",
      "<결과> 4 - 1 = 3\n"
     ]
    }
   ],
   "source": [
    "class Calculator:\n",
    "\n",
    "    def __init__(self, first, symbol, second): # 호출자\n",
    "        self.first = first\n",
    "        self.symbol = symbol\n",
    "        self.second = second\n",
    "\n",
    "    def symbol(self): # 연산 기호\n",
    "        symbol = self.symbol\n",
    "        return symbol\n",
    "\n",
    "    def add(self): # 덧셈\n",
    "        result = self.first + self.second\n",
    "        return result\n",
    "\n",
    "    def sub(self): # 뺄셈\n",
    "        result = self.first - self.second\n",
    "        return result\n",
    "\n",
    "    def mul(self): # 곱셈\n",
    "        result = self.first * self.second\n",
    "        return result\n",
    "\n",
    "    def div(self): # 나눗셈5\n",
    "        result = self.first / self.second\n",
    "        return result\n",
    "\n",
    "\n",
    "while True:\n",
    "    print('''\n",
    "      원하는 계산을 입력하세요. (사칙연산만 가능)\n",
    "                                             ''')\n",
    "    a = Calculator( int(input(\"피연산자1 : \")), input(\"연산기호 : \") , int(input(\"피연산자2 : \")) )\n",
    "\n",
    "    if (a.symbol == \"+\"):\n",
    "        print(\"<결과> {} {} {} = {}\".format(a.first, a.symbol, a.second, a.add()))\n",
    "    if (a.symbol == \"-\"):\n",
    "        print(\"<결과> {} {} {} = {}\".format(a.first, a.symbol, a.second, a.sub()))\n",
    "    if (a.symbol == \"*\"):\n",
    "        print(\"<결과> {} {} {} = {}\".format(a.first, a.symbol, a.second, a.mul()))\n",
    "    if (a.symbol == \"/\"):\n",
    "        print(\"<결과> {} {} {} = {}\".format(a.first, a.symbol, a.second, a.div()))\n",
    "\n",
    "    switch = str(input(\"계속하시려면 아무 키나, 끝내시려면 N를 입력하세요. \")) \n",
    "    print(\"-------------------{} {}--------------------\\n\".format(switch, \"입력\"))\n",
    "    if(switch == 'N' or switch == 'n'):\n",
    "        print(\"계산기를 종료합니다.\")\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "typical-cooling",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.8 : galaxy",
   "language": "python",
   "name": "sample"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
>>>>>>> 41458244936243f4b124854fa193f9d4b769640c
