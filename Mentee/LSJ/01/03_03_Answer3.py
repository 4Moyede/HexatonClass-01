#!/usr/bin/env python
# coding: utf-8

# In[ ]:


FreqDict = {} #FrequencyDictionary, 한줄이 끝날때마다 딕셔너리를 초기화함
FreqTotalDict = {} #총 빈도수를 지정하는 딕셔너리

def CheckFrequency():
    Sentence = input().split() #문자열로 되어있는 것을 split함수를 이용하여 리스트로 변경
    for Frequency in Sentence:
        if "END" in Sentence: 
            break
        else:
            if Frequency in FreqDict: #Frequency라는 키가 빈도수를 일시적으로 저장하는 딕셔너리에 있다면 1을 더하고, 없다면 1로 지정
                FreqDict[Frequency] += 1
            else:
                FreqDict[Frequency] =1
    return FreqDict.items()

def CheckGlobalFrequency(Dictionary): #FreqDict이라는 딕셔너리는 매 줄마다 일시적으로 사용하는 딕셔너리이므로 총합을 구하기위해서 별도로 저장
    for FreqKey, FreqValue in Dictionary:
        if FreqKey in FreqTotalDict:
            FreqTotalDict[FreqKey] += FreqValue
        else:
            FreqTotalDict[FreqKey] = FreqValue
    


Trial = 1

while Trial<=20 :
    SenResult = CheckFrequency()
    if FreqDict == {}:
        break
    else:
        print("[Sentence %d]"%Trial)
        for word, frequnecy in sorted(SenResult, key=lambda x : (x[1], x[0])): #정렬을 위하여 람다함수를 이용, 구글링했습니다... 어려워
            print(word,":",frequnecy)
        Trial += 1
        CheckGlobalFrequency(FreqDict.items())
        FreqDict = {}
        print('\n')

print("[All Sentence]") #while문을 빠져나왔을때(END로 끝나거나 20문장이 채워지는 경우) 마지막으로 이 부분을 실행
for word, frequency in sorted(FreqTotalDict.items(), key=lambda x : (x[1], x[0])):
    print(word,":",frequency)

