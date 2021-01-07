#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#함수는 2개로 구현, 각 자리수의 합을 구하는 함수 & 역을 만드는 함수
#각 자리수를 구현하는 함수는 TotalSum으로하고, 역은 TotalReverse로 하자(통일)

def TotalSum(InputNumber):
    sum = 0
    for Digits in InputNumber:
        if InputNumber == '0':
            break
        else:
            sum += int(Digits)
    return sum

def TotalReverse(InputNumber):
    reverse = 0
    digit = 0
    for Digits in InputNumber:
        if InputNumber == '0':
            break
        else:
            reverse += int(Digits) * 10**(digit)
            digit += 1
    return reverse

Trial = 0

while Trial<10 :
    InputNumber = input()
    if InputNumber == '0':
        break
    else:
        print(TotalReverse(InputNumber),TotalSum(InputNumber))
        Trial += 1

