
while(True):
    num = int(input("양의 정수를 입력"))
    if (num>2100000000):
        print("21억 넘으면 안됨")
        break
    if (num==0):
        break

    num_length = (len(str(num))-1)
    rev = []

    while num_length >= 0 :
        res = num // 10**(num_length)
        rev.append(res)
        num = num - res * 10**(num_length)
        num_length -= 1

    rev.reverse()

    if(rev[0]==2 and rev[1]==1 and num>1000000000):
        print("결과값이 21억 이상임")
    else:
        for k in rev:
            print(k,end='')
        print()
        print(sum(rev))