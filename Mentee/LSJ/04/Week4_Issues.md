## 지난주 Issue 알아보기

### 1. 리스트 슬라이싱

알다시피 문자열이나 리스트의 경우 필요한 항목만 따로 빼올 수 있는 방법이 있다.

대표적인 방법이 인덱싱과 슬라이싱인데,

인덱싱은

```python
a[4]
```

다음과 같이 대괄호로 특정 인덱스를 입력하여 빼내는 방법이고

슬라이싱은

```python
a[1:4]
```

와 같이 : 라는 기호를 사용하여 1부터 3까지를 불러오는 방법도 있다.

그런데, 내가 airbnb과제를 하면서 필요한 칼럼이 2번째와 4번째부터 11번째까지에 있었기에 이를 iloc함수를 이용하여 한꺼번에 더해서 구하려했으나, 이것이 생각대로 되지 않고 오류가 떴다.

그래서 직접 인덱싱과 슬라이싱의 출력결과를 확인해보니

```python
a = [1,2,3,4,5]
a[3:4],a[1]
```

다음과 같이 슬라이싱과 인덱싱을 직접 수행해보니 결과가 슬라이싱은 리스트로, 인덱싱은 문자열로 출력되는 것을 확인할 수 있었다.

→ 즉, 슬라이싱의 반환되는 자료형은 리스트, 인덱싱은 문자열이 반환되므로 덧셈이 되지 않았던 것이다

→ 따라서 아예 인덱싱을 리스트로 넣어버려서 전체를 리스트로 만든다음, 이를 iloc함수에 넣는 식으로 해결하였다.

- 개인적으로 지금까지 물어본 이슈중에서 가장 뿌듯하고, 얻어갈것이 많고, 이상적으로 해결되었던 문제였다. 앞으로의 디버깅도 이와 같았으면...

### 2. pull request 버튼이 보이지 않음

1. pull request를 closed하고 다시 push
2. Everything up-to-date
    - 이 코드의 경우 커밋이 정상적으로 됐을때 나오는 코드다 → 그래서 오류는 아님
3. 그런데 pull request는 다시 뜨지 않았다.

→개인적인 생각으로는 지우 멘티님이 request를 닫았는데, 닫은 이후에 commit한것은 반영되지 않은 것으로 보인다

지지난주에 만든 공부용 github로 테스트를 해보았더니, 예상한대로 closed된 commit의 경우 pull request가 반영되지 않았다. **그렇지만 reopen하게 되면, 그때 commit이 반영된다.**

### 3. Matplotlib 모듈을 설치했음에도 인식하지 못하는 오류&8. 쥬피터파일에서 이미지가 안보이는 이유

모듈을 설치해도 실행하지 못하는 경우는 파이썬이 설치되어있는 디렉토리와 모듈이 설치되어있는 디렉토리가 달라서 생기는 이유다.

→ 그런데 우리는 가상환경을 사용하고 있음.

가상환경의 경로는 : anaconda3/envs/(가상환경 명)

여기에 설치되어있는 파이썬 경로는

 anaconda3/envs/(가상환경 명)/python.exe

라고 되어있고,

패키지의경우 같은 디렉토리에 lib, DLLs파일등에 저장되어있음.

즉, 가상환경에서 모듈과 파이썬이 설치되어있는 경로는 같은 디렉토리에 있다.

→ 다른 경로에 있다면 모듈을 import못한다고 추측가능

같은 이유로, 어떤 파일에 이미지 파일을 첨부한 상태라면, 반드시 이 이미지 파일도 같은 디렉토리에 넣어놔야한다.

→ 즉, 디렉토리에 있는 파일을 불러오는 것이, 파일 자체에 이 이미지를 내장하는 것보다 용량을 아낄 수 있는 방법이기 떄문에, 이렇게 불러온다고 (개인적으로) 추측한다.

### 4. import구문을 하단에 쓰면 안되는 이유 & 5. for 구문에 i를 쓰면 안되는 이유 & 9. for i in range문 & 19. for i in list의 i에 대하여

→ 두 이슈 모두 C언어와 파이썬의 차이점에서 나오는 이유임.

우선, import라는 구문의 경우 하단에 쓰면 안되고, 상단에 모아써야함. 물론 파이썬에서는 이렇게 써도 오류가 안뜨긴하지만, 그래도 C언어와 같은 언어의 경우 import를 위에다가 하지 않으면 오류가 뜬다.

→ 다만 파이썬은 interpreter방식을 사용하여 컴파일과정없이 코드를 순차적으로 실행시키는 언어라서 컴파일이 필요한 C언어와는 다르게 바로 실행할 수 있다.

또한 파이썬에서도 for문의 경우 i와 같은 문자를 사용하지 않아도 for문을 돌릴 수 있지만, C언어와 java같은 경우 for문에서 문자열을 사용할 수 있는 것이 아니라, iterator, 다시 말해 반복문을 사용하기에, 이때 변수이름을 최대한 간결하게 만들 필요가 있었기 때문에 어쩔 수 없이 i라는 간단한 문자로 대치했다고 볼 수 있다.

결국 파이썬과 C/java의 구동방식과 문법에 대한 차이점때문에 문법상으로 큰 오류는 없지만 다른 언어를 쓰듯이 규격을 맞춰야하는것이다.

### 6. 최적의 변수명 짓기&11. 가독성 좋은 코드 짜기&16.함수 이름 지을 때의 문제점

→ 우선 변수나 함수의 이름의 경우 확실하게 뜻을 구별할 수 있어야하고, 다른 내장함수와 확실하게 구별할 수 있어야한다.

그렇기에 변수와 함수의 경우 다음과 같이 몇가지 수칙을 만들어보았다

1. 변수의 첫글자는 소문자, 함수의 첫글자는 대문자로 정한다
2. 함수 이름은 되도록 겹치지 않게, 구별할 수 있게 만들자
3. 함수의 정보를 정확하게 밝히기 위해 동사를 맨앞에 넣자. 
4. 변수의 경우, 띄어쓰기를 활용하고, 너무 길어지면 약자를 쓰자

다만, 이렇게 특색있는 변수명을 짓게된다면, 코드한줄에 변수를 많이 넣으면 가독성이 떨어진다는 단점이 있다.

그렇기에 재범 멘티님이 제안한 방법대로 코드를 줄바꿈을 해도 아무런 문제없이 코드가 돌아가기 때문에,

```python
airbnb_filter = airbnb_db[(airbnb_db["price"]>PFilter) & (airbnb_db["neighborhood"] == NFilter) & (airbnb_db["reviews"] > RFilter)]
```

다음과 같은 코드를 줄바꿈을 사용하면

```python
airbnb_filter = airbnb_db[ (airbnb_db["price"] > PFilter)
                         & (airbnb_db["neighborhood"] == NFilter)
                         & (airbnb_db["reviews"] > RFilter) ]
```

다음과 같이 훨씬 보기 좋은 코드가 만들어진다.

그 외에도 멘토님이 알려주신 코드 중 하나인 enumerate와 같은 다양한 함수를 활용하면 반복되는 부분을 최대한 줄일 수 있어 이러한 함수로 가독성을 높이는 방법도 고려하면 좋다.

### 그 외의 이슈들

1. BeautifulSoup에서 하위 태그를 검색 못하는 오류가 있었다.

    →원래 의도는 table > tbody로 table의 body부분을 따로 추출하려했지만 이렇게 되지 않았다

    → 그렇지만 td_03이라는 machine의 정보만을 담당하는 class 명을 찾아서, 이를 td.td_03으로 추출 → 해결

    가장 정석적인 방법은 하위태그를 타고 들어가는 것이지만, 이것이 안통할수도 있으니 꼭 꼼꼼하게 크롤링해보자

2. 문자열 입력시 '', ""사용

    → 작은따옴표나 큰따옴표는 입력할때 한꺼번에 두개가 입력이 됨

    → 이때 뒤에 있는 따옴표를 지워야 하나만 지워지고, 앞에 있는 따옴표를 지우는 경우 따옴표 2개가 한꺼번에 사라짐

    → ',"을 하나만 쓰고 싶을때는 뒤에서 지우자

3. global 변수를 쓰면 안되는 이유

→ 글로벌 변수의 경우 저장이 파일 내부가 아닌, 컴퓨터의 메모리에 저장이 된다

→ 그렇기에 메모리 낭비가 될 뿐만 아니라, 다른 프로그램에서 같은 이름의 변수를 불러올경우 이 값이 나오게 된다.

→ global변수를 사용할일이 거의 없으므로, 웬만하면 사용을 지양하자

4. 변수 선언

→코드에 보면 변수가 위에 filtered_data.index라는 변수의 인덱스를 활용했는데, 밑에 filtered_data라는 변수가 다시 정의되었음.

→ 쥬피터 파일에서는 돌아가고, VSCode와같은 다른 프로그램에서는 실행되지 않으므로 이에 유의하자

5. 확장자 이슈(.ipynb, .py)

→ ipynb는 쥬피터 노트북에서만 사용하는 별도의 확장자이다. 그렇기에 이를 py로 바꾸고싶다면 그냥 확장자만 바꿔도 될 것 같지만, 확장자만 바꾸면 .py파일이 실행되지 않는다

→별도의 바꾸는 과정으로 py확장자로 바꿔야함

6. 리스트 전체를 for문을 돌릴때

→ 나는 여기에서 range를 칼럼이 8개니까 단순히 8이라 적었지만, 칼럼의 개수는 고정된것이 아니라 가변적이다. 그렇기에 칼럼의 개수를 바꿀때 굳이 range(8)까지 수정할 고생을 할 필요 없이 range(len(list))와 같이 적으면 리스트의 개수가 바뀌어도 이 코드까지 바꿀 필요가 없어진다

7. set자료형과 unique함수

→ unique함수의 경우 데이터의 중복을 없애는 함수임. 예를들어 1,2,2,2,3,3,4,5와 같은 데이터가 있다면, 이를 1,2,3,4,5로 출력한다.

다만, 이때 정렬이 되지 않아 별도로 정렬해야한다.

→ set 자료형은 말그대로 집합 자료형이다.

그렇기에 딕셔너리처럼 중괄호로 표현되지만, 이때 함수니까 key : value형식이 아니다.

set 자료형을 사용하면 중복을 자동으로 제거해줄 뿐만 아니라, 자동으로 정렬까지 해준다.