#!/usr/bin/env python
# coding: utf-8

# In[22]:


LineInput = int(input()) # 줄 개수를 받는 변수 LineInput
String = 0 #변수 String(문자) 정의
StringPlus = 0 #같은 줄에 n개만큼 더한다는 것을 표현하는 변수 정의
Blank = 0 #빈칸 개수 정하는 변수 정의
for Lines in range(LineInput+1):
    String = Lines #각 줄의 첫번째 글자를 설정함
    for Blank in range(LineInput - Lines):
        print(end="  ")
    for StringPlus in range(Lines):
        print(chr((int(String)-1)%26+65), end=" ")
        String += LineInput - StringPlus -1
    print('')

