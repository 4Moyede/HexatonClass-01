## 멘티 Calculator Code Review


### 지우

Class를 아주 잘 사용하셨네요! 그러나 초기값을 0이라고 하지 않고 input으로 받았으면 더 좋았을 것 같다는 생각이 들었습니다.
sign에는 연산기호가 들어가고, input number에는 숫자가 들어가야 하는데 숫자와 연산자 이외에 다른 것들이 입력되더라도,
그냥 계산기가 진행되는 점이 아쉬웠습니다..! Class에 to_zero라는 메소드도 정의해서 초기화되는 건 생각 못해봤는데 정말
꼼꼼하게 잘하신 것 같네요...! 


### 재범

print("<결과> {} {} {} = {}".format(cal.first, cal.symbol, cal.second, cal.add())) format이 뭔지는 알고 있었는데 이렇게 원할 때 바로바로
쓸줄 아는 것...배우고 갑니다! 
다만 두개의 연산자만 연산이 가능한게 아쉽네요. 저는 Class 정의에서 연산들을 정의 할 때, self랑 연산자로 받을 숫자를 지정해줘서
이 문제를 해결했습니다...! 뭔가 설명이 이상하지만 한번..해보시길 추천드려요!

### 경훈

ㅋㅋㅋ가독성이 좋은 코드인 것 같고, 역시  print("{}{}{} = {}".format(cal.x, cal.operator, cal.y, cal.add())) 이 부분을 잘 쓸줄 아는 것 같아서 좋
습니다. 그렇지만 재범이와 마찬가지로 연산자가 두개만 되서 좀 아쉽습니다...! 
try except문은 혼자 python 공부하면서 이해가 잘 안됬던 부분인데 계산기 코드에 적어둔 걸 보니까 언제 쓰는 건지 좀 알게된 것 같습니다..!


### 성준

역시 reset을 추가할 생각은 전 못했는데.... 어떤 문제가 주어지고 이에 대한 코드를 기획할 때 문제를 꼼꼼히 볼 줄 알아야
이런 기능들도 보이는 것 같네요! 전반적으로 깔끔한 코드인 것 같아서 고칠 건..없어보입니다..ㅎㅎ

## ISSUE 정리하기!

### 1. import 구문의 위치에 대하여.

import matplotlib.pyplot as plt

다음과 같이 import 구문을 통해 모듈을 불러올 때, 구문을 맨 위에 적는게 Python에서 권장하는 스타일이라고 했다. 물론 import 구문을 중간에 작성해도 오류는 발생하지 않았다. 그러나,i mport 구문을 코드의 맨 위에 작성하게 되면, 어떤 모듈을 불러올 것인지 한번에 알 수 있게 되고, 그렇게 되면 이 파일이 어떤 내용을 포함하게 되는지 초반에 알 수 있게 되어서 코드를 읽는 협업자들에게 굉장히 도움이 되기 때문이다.

### 2. for i in range의 i는 옳은 것일까?
Pandas 과제를 할 때 많이 지적당했던 부분인데, 사실 오류가 없었기 때문에 왜 지적당했었는지 알지 못했었다. 그런데 관련 issue가 올라왔었고, 다음과 같은 이유로 '권장'하지 않음을 알 수 있었다. 

1. range는 len함수와 같이 사용해야한다.
2. 리스트와 같은 자료구조의 **인덱스**에 접근해야 한다.

그리고 i라는 변수도 너무 무의미한 변수이기 때문에 for i in range() 구문을 쓰더라도, i라는 변수를 지정하는 것을 **지양해야겠다.**

### 3. 가독성이 좋은 CODE는 어떤 걸까?

3. 가독성이 좋은 CODE에 대하여...

    가령 단순하게 다음과 같은 코드를 짰다고 해보자

    ```
    print("We select only Good information about airbnb dataset : ")
    print("1  :  room_type")
    print("2  :  neighborhood")
    print("3  :  reviews")
    print("4  :  overall_satisfaction")
    print("5  :  accommodates")
    print("6  :  bedrooms")
    print("7  :  price")
    print("8  :  minstay")
    ```

딱봐도 조잡해보인다.  **python은 이런 조잡함을 해결할 함수들과 자료형들이 있는데 이를 적재적소로 활용하여 코드를 간결하게 만드는건 내 능력**이다...

위에 작성했던 코드를 enumerate함수를 활용하면 다음처럼 간결하게 정리할 수 있다.

```
for i, v in enumerate(t):
   print("index : {}, value: {}".format(i,v))
```

tuple이라는 자료형과 enumerate라는 함수를 적재적소로 활용했기 때문에 이렇게 깔끔한 코드를 만들 수 있었다.

### 4. Enumerate 함수는 무엇일까? 

### **enumerate 함수**

- 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
- enumerate는 “열거하다”라는 뜻이다. 이 함수는 **순서가 있는 자료형(리스트, 튜플, 문자열**)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
- 보통 enumerate 함수는 아래 예제처럼 for문과 함께 자주 사용된다.

**`>>>** **for** i, name **in** enumerate(['body', 'foo', 'bar']):
**...**     **print**(i, name)
**...**0 body
1 foo
2 bar`

for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할때 enumerate 함수를 사용하면 매우 유용하다.

`names **=** ['철수', '영희', '영수']
**for** i, name **in** enumerate(names):
  **print**('{}번: {}'**.**format(i **+** 1, name))`
  
 ### 5. list slicing(리스트 슬라이싱 하기)
 
 ```
airbnb_remake = airbnb_db.loc[:, ['room_type','neighborhood':'minstay']]
airbnb_remake
```

우리가 이런식으로 loc함수를 이용해서 airbnb_db라는 DataFrame의 column을 선별적으로 불러오려 할 때, 굳이 column명을 다 적지 않고 위처럼 콜론을 사용하여 범위처럼 나타내고자 할 것이다.(나도 그랬음)

이 때, 오류가 발생하는데 그 오류를 파악해보면

```
a = [1,2,3,4,5]
a[3:4],a[1]
```

이렇게 입력했을 때, a[3:4]는 list의 type으로 출력되었고, a[1]은 문자열의 type으로 출력되었다. 즉 

'room_type','neighborhood':'minstay' 에서 'room_type'과 'neighborhood':'minstay'는 서로 다른 형태였던 것이다. 그래서 오류가 발생하였다. 

```
column_extract = [2] + list(range(4,11))
airbnb_remake = airbnb_db.iloc[:, column_extract]
```

그래서 이런식으로 아예 모두 리스트로 통일하여 대입하면, 원하는 결과를 얻을 수 있었다.

### 6. 길어지는 코드 대처하기.

```
airbnb_filter = airbnb_db[ (airbnb_db["price"] > PFilter)
                         & (airbnb_db["neighborhood"] == NFilter)
                         & (airbnb_db["reviews"] > RFilter) ]
```

줄바꿈하는 방법은 처음 알았다..! 간결해보이고 한눈에 다 들어와서 아주 좋은듯!

### 7. list 전체를 for문에 돌리기.

```
test_list = [ 1, 2, 3 ]

# python에서 제공해주는 in 을 활용
for element in test_list:
    print(element)

# index를 활용하는 방법
for idx in range(len(test_list)):
    print(test_list[idx])
```

test_list라는 리스트를 for 문에 적용하고 싶을 때,

요소 자체를 불러들이는 for ~ in을 사용하는 방법이 첫번째이고

요소의 index를 이용하는 방법이 두번째 코드이다. 근데 만약 len(test_list)가 아닌 자체적으로 list의 길이를 직접 입력하여

                                  for idx in range(5):
                                         print(test_list[idx])

이런 식으로 코드를 작성할 경우, list는 가변적인 자료형이라 리스트를 수정할 경우 range안 괄호도 수정해야 한다. 그렇지만 len(list)를 이용할 경우 list가 변할 때 len(list)도 변하기 때문에 코드를 두번 수정할 일이 없게 되는 것이다!

### 8. 중복을 제거하자 set vs unique

Set함수

- 순서가 없음
- 집합 내에서 unique한 값을 갖는다.
- 가변적 개체
- 집합 자료형 자체가 정렬된 상태로 출력이 됨.

unique함수

- 'python db분석 라이브러리'를 사용할 때 사용가능
- 입력되는 value들은 직선형의 array로 입력되야 함
- 따로 정렬해주는 기능이 없음

### 9. 함수이름을 정의하는 좋은 방법이란?


```
def information():
    good_info = df.loc[:,['room_type','neighborhood','reviews','overall_satisfaction','accommodates','bedrooms','price','minstay']]
    print("We select only Good information about airbnb dataset : ")
    print("1  :  room_type")
    print("2  :  neighborhood")
```

```
def filtered ():
    filtering = (df.price > 250)&(df.neighborhood == 'Downtown')&(df.reviews > 5)
    df_filtering = df.loc[filtering, :]
    return df_filtering
filtered()
```

```
def column_value(column):
    my_column_value = {}
    my_column_value[column] = set(df[column].unique())
    return my_column_value

```

위 코드 문제점 : information은 무슨 information을 의미하는거지? c

 a. 함수를 지을 때 동사는 무조건 앞으로 하자.

가령  set_{},make_{}, del_{}, insert_, change_{}, select_{}, init_{} 이런 식으로 동사가 앞에 오게끔 쓰면 무엇을 할 지 알 수있는 함수 명명법이다.

b.  함수이름을 단조롭게 쓰지말자 충돌난다.

위처럼 filter, information 이렇게 1차원적으로 쓰면 무조건 충돌 난다.

### 10.  'if __name__ = '__main__'의 의미...?!

이를 그대로 해석해보면, '__name__이라는 변수의 값이 __main__이라면 아래의 코드를 실행하라.' 라는 뜻이 된다.  하나하나 파악해보면,,,

__name__은 먼저 파이썬의 내장변수이다. 이는 현재 모듈의 이름을 담고 있다. 직접 실행된 모듈의 경우 __main__의 값을 갖고, 직접 실행되지 않고 import된 모듈의 경우 모듈의 이름(파일명)을 갖게 된다.

다음과 같은 코드가 있다

**<코드 - 모듈>**

```
#module.py
def hello():
    print("Hello!")

print(__name__)
```

**<코드 - 메인>**

```
#main.py
import module

print(__name__)
module.hello()

```

**<결과 - 메인>**

```
module
__main__
Hello!
```

먼저 module.py는 hello()라는 함수가 정의되어 있고, __name__이라는 내장변수를 출력하게끔 되어있다.

main.py에서 module을 import하고, __name__을 출력하게끔 되어있다. 그리고 module에서 import된 hello()라는 함수를 실행한다.

결과를 보면, 먼저 import된 module에서 print(__name__)이 실행되면서 module.py의 내장변수에 module이라는 값이 들어가게 된다.(직접 실행된게 아니라서) 그 후, main함수 자체의 내장변수를 출력하는 명령이 실행되는데 이는 직접 실행된 파일이기 때문에 __main__을 갖게 된다. 그리고 hello()함수가 실행된다.

만약, module.py에 if __name__ = '__main__'을 추가하면 어떻게 될까?

**<코드 - 모듈>**

```
#module.py
def hello():
    print("Hello!")

if __name__=="__main__":
    print(__name__)

```

**<결과 - 메인>**

```
__main__
Hello!
```

즉 module 내부의 __name__에는 __main__이 아닌 module이 저장되어 있기 때문에 출력되지 않은 것이다.

결론을 짓자면 모듈에 if **name**=="**main**"이라는 조건문을 넣어주고 그 아래는 직접 실행시켰을 때만 실행되길 원하는 코드들을 넣어주는 것으로 생각하면 쉬울 것이다.


