## Day_2_1

> 181218

**Index**

1. String Interpolation
2. 파일명 바꾸기
3. 파일 읽고 쓰기
4. 웹스크래핑
5. 이메일
6. GitHub-static-website

------

### 1. String Interpolation(삽입)

```python
# 과거
'%s %s' % ('one', 'two')

# pyformat
'{} {}'.format('one', 'two')
```

1-1 [pyformat](https://pyformat.info/)

```python
name = "홍길동"
english_name = "hong"
print("안녕하세요, {}입니다. My name is {}".format(name, english_name))
#=> "안녕하세요, 홍길동입니다. My name is hong"

print("안녕하세요, {1}입니다. My name is {0}".format(name, english_name))
#=> "안녕하세요, hong입니다. My name is 홍길동"

print("안녕하세요, {1}입니다. My name is {1}".format(name, english_name))
#=> "안녕하세요, hong입니다. My name is hong"
```

#### 1-1 f-strings (PEP 498)

> New in python 3.6

```python
name = "홍길동"
print(f"안녕하세요, {name}입니다.")
#=> "안녕하세요, 홍길동입니다."
```

```python
import random

menu = ["김밥천국", "스타벅스", "부대찌개"]

lunch = random.choice(menu)
print("오늘의 점심은 {}입니다.".format(lunch))
print(f"오늘의 점심은 {lunch}입니다.")
```

```python
import random

numbers = list(range(1,46))
lotto = random.sample(numbers, 6)
print(f"오늘의 행운의 번호는 {sorted(lotto)} 입니다")
```

2. 모르면 이렇게 해보자

```python
name = "홍길동"
print("안녕하세요, " + name + "입니다.")
```

---

### 2. 파일명 바꾸기

> [zzu.li/dummy](http://zzu.li/dummy) 에서 가져온 코드 그대로 bash 에서 실행.
>
> 이제 500 개의 지원서를 조작해보자.

- import os

1. `os.chdir(r'폴더주소')` : 작업하고 있는 위치 변경
2. `os.listdir('폴더주소')` : 저장된 디렉토리 전체 파일 목록 얻기
3. `os.rename('현재파일명','바꿀 파일명')`

- os 함수

```python
#1 os 를 import 한다.
import os

#2 해당 폴더로 들어간다.
os.chdir(r“C:\Users\user\Downloads\files”)

#3 폴더 안에 모든 파일을 돌면서 이름을 바꾼다.
for filename in os.listdir(“.”):
    os.rename(filename, “SAMSUNG  ” + filename)
```

```python
#1 os 를 import 한다.
import os

#2 해당 폴더로 들어간다.
os.chdir(r“C:\Users\user\Downloads\files”)

#3 폴더 안에 모든 파일을 돌면서 이름을 바꾼다.
for filename in os.listdir(“.”):
    os.rename(filename, filename.replace(“SAMSUNG“, “SAFFY”))
```

---

### 3. 웹 스크래핑

> 하나하나씩 내용물 찍어보면서 진행!

- requests

```python
import requests
req = requests.get("https://www.google.com")
print(req)
print(req.text)
print(req.status_code)
```

#### 3-1. 정보 스크랩 1단계

1. 원하는 정보가 있는 주소로 요청을 보내, 응답을 저장한다.

```python
import requests
req = requests.get("https://www.google.com").text
```

2. 정보를 출력하여 확인한다. 


```python
print(req)
```

#### 3-2. 코스피 지수

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)

```python
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.google.com")

soup = BeautifulSoup(req, 'html.parser')
soup.select(경로)
soup.select_one(경로)
```

#### 3-3. 정보 스크랩 2단계

1. 정보를 조작하기 편하게 바꾸고,

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(req, 'html.parser')
```

2. 바꾼 정보 중 원하는 것만 뽑아서,

```python
kospi = soup.select_one(‘selector 경로’)
```

3. 출력한다

```python
print(kospi.text)
```

- kospi

```python
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one('#KOSPI_now')

print(kospi.text)
```

**실습-1 네이버 실시간 검색어 스크래핑**

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k'):
    print(tag.text)
```

- ### 도전과제 <데이터 최대한 많이 가져오기>

---

### 4. 이메일 (분량 상 마크다운 분리)

### 5. GitHub Static Website

- GitHub에서는 [GitHub Pages](https://pages.github.com/) 라는 호스팅 서비스를 제공하고 있는데, 이를 이용하면 개인 페이지(블로그)를 **무료**로 생성할 수 있다. [영상](<https://youtu.be/2MsN8gpT6jY>)

|               | 구축형 (Wordpress) | 가입형 (Tistory) | GitHub Pages |
| ------------- | ------------------ | ---------------- | ------------ |
| 비용          | 유료(서버+네트웍)  | 무료             | 무료         |
| 서버 구축     | 필요함             | 필요없음         | 필요없음     |
| 네트워크 설정 | 필요함             | 필요없음         | 필요없음     |
| Markdown      | 가능               | 불가능(제한적)   | 가능         |
| HTML 편집     | 가능               | 불가능(제한적)   | 가능         |

1. 레퍼지토리를 생성한다.
   - **단, 레퍼지토리의 이름은 반드시 `나의유저네임.github.io` 로 설정한다.**
2. 무료 템플릿 사이트에서 마음에 드는 템플릿을 다운로드 한다.
   - [startbootstrap](https://startbootstrap.com)
   - [Resume](https://startbootstrap.com/template-overviews/resume/)

3. 다운 받은 폴더를 위에 생성한 레퍼지토리에 연결하고 push 한다.

4. `https://나의유저네임.github.io/` 으로 접속해 템플릿을 확인한다.

> github 호스팅에 시간이 소요될 수 있으니 페이지가 바로 뜨지 않는다면 잠시후 다시 시도해 본다.
>
> GitHub Pages 는 `index.html` 을 자동으로 메인 페이지로 인식한다.
>
> 그래서 `https://나의유저네임.github.io/` 와 `https://나의유저네임.github.io/index.html/` 의 모습이 같다.