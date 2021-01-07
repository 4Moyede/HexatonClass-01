
all_sentence = []
count = 0

while True:
    
    sentence = input(str("아무 문장이나 입력 : ")).split()  # 최초 배열

    if (sentence == ["END"]): # END 입력되면
        break

    else: # 정상 진행
            all_sentence.extend(sentence) # while절이 끝나고 사용될 배열 미리 선언
            length = len(sentence) # 배열의 길이
            num = 0
            list_result = []

            while( length > 0 ):
                result = [ (sentence[num]), int(sentence.count(sentence[num])) ] # 배열
                list_result.append(result) # 배열 안의 배열 (2차)
                length -= 1
                num += 1

            new_list_result = []
            for v in list_result:
                if v not in new_list_result:
                    new_list_result.append(v)  # 2차 배열 중 중복되는 배열 제거
                    
            new_list_result.sort(key = lambda x:(x[1], x[0]))   # 2차 배열을 오름차순으로 정렬

            print("Sentence %d" % count)
            count += 1

            for i in new_list_result:   # 출력...
                for j in i:  
                    print(j, end=' ')
                print()

# 위에서 했던 과정 똑같이 반복

print(all_sentence)
all_length = len(all_sentence)
all_num = 0
all_list_result = []

while( all_length > 0 ):
    all_result = [ (all_sentence[all_num]), int(all_sentence.count(all_sentence[all_num])) ]
    all_list_result.append(all_result)
    all_length -= 1
    all_num += 1

new_all_list_result = []
for w in all_list_result:
    if w not in new_all_list_result:
        new_all_list_result.append(w)

new_all_list_result.sort(key = lambda x:(x[1], x[0]))

print("All Sentence")

for i in new_all_list_result:
    for j in i:
        print(j, end=' ')
    print()

print("프로그램 종료")