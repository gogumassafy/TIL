## Day_1

> 181217

**Index**

1. 4차산업혁명과 프로그래밍
2. Hack your life
3. Python 기초
4. Python 심화
5. git

---

### 3. Python 기초

- 컴퓨터 프로그래밍 언어 개념

#### 1) string

- 기본 활용법

```python
# 기본 방법
print("안녕하세요")
print("저는 홍길동입니다.")
print("만나서 반갑습니다.")

print("""안녕하세요
저는 홍길동입니다.
만나서 반갑습니다.
""")
```

출력결과:

```bash
안녕하세요
저는 홍길동입니다.
만나서 반갑습니다.

안녕하세요
저는 홍길동입니다.
만나서 반갑습니다.
```

#### 2) range

- `range` 는 숫자의 범위를 가지고 있다.

```python
print(range(5))
#=> range(0,4)

# list 형변환
a = list(range(5))
print(a)
#=> [0,1,2,3,4]

# 반복문 활용
for i in range(3):
    print(i)
#=> 0
#=> 1
#=> 2
```

#### 3) List

- `list`는 배열 또는 array라고도 불린다. 인덱스를 통해 값에 접근할 수 있다.

```python
menu = ["중국집", "초밥", "고기", "분식"]
menu[0]
#=> 중국집
```

- `list`는 정렬을 할 수 있다.

```python
a = [3, 1, 2]

# 1. sorted
sorted(a)
#=> [1,2,3] 리턴
print(a)
#[3,1,2]
a = sorted(a)
print(a)
#[1,2,3]

# 2. .sort()
a.sort()
#=> None 리턴
print(a)
#[1,2,3]
```

#### 4) Dictionary

`Dictionary` 는 hash(해시)라고도 불린다. `key`와 `value`가 짝지어져있다.

```python
phonebook = {
    "중국집": "123-525",
    "초밥": "8464-5215",
    "고기": "213-987",
    "분식": "564-2123"
}
phonebook["중국집"]
#=> "123-525"
```

#### 5) **챗봇 실습**

3-1. 변수 활용하기 - 여러번 인사

```python
greeting = "안녕하세요!"
print(greeting)
print(greeting)
print(greeting)
print(greeting)
print(greeting)
```

3-2. 리스트 활용하기 - 점심메뉴 알려주기

```python
import random

menu = ["김밥천국", "스타벅스", "부대찌개"]

lunch = random.choice(menu)
print(lunch)
```

```python
import random

menu = ["김밥천국", "스타벅스", "부대찌개"]

lunch = random.choice(menu)
print("오늘의 점심은 {}입니다.".format(lunch))
print(f"오늘의 점심은 {lunch}입니다.")
```

3-3. 딕셔너리 활용하기 - 커피 + 사진

```python
import random

# 1. menu 리스트를 만들어주세요.
menu = ["이화수전통육개장 대전한밭대점", "롱다리 묵은지 김치찜", "응급실국물떡볶이", "신전떡볶이 노은역점", "2마리3맛투존치킨 노은점", "교촌치킨 노은1지구점", "7번가피자 노은점", "노은각"]
choice = random.choice(menu)
print(choice)

# 2. 번호 딕셔너리를 만들어주세요.
phonebook = {'이화수전통육개장 대전한밭대점': '050-6209-2300', 
 '롱다리 묵은지 김치찜': '050-6271-2288', 
 '응급실국물떡볶이': '050-7802-2013', 
 '신전떡볶이 노은역점': '050-6403-7450', 
 '2마리3맛투존치킨 노은점': '050-6448-3916', 
 '교촌치킨 노은1지구점': '0504-831-3920', 
 '7번가피자 노은점': '050-7996-4830', 
 '노은각': '050-6457-7071'}

print(phonebook[choice])
```

3-4. 조건문 활용하기 - 미세먼지

```python
import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EB%8C%80%EC%A0%84&ServiceKey=QaGapZXPV5DTM72fy6lrf3hJnrJxhila1UVkPlUCo0N0g0F0RZ9WEngT8RkNjNo4IF%2BikV%2BthQLze39nK4IQjA%3D%3D&ver=1.3&pageNo=2'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
daejeon = soup('item')[0]
location = daejeon.stationName.text
time = daejeon.dataTime.text
dust = int(daejeon.pm10Value.text)


print(f"{time} 기준 \n대전 {location}의 미세먼지 농도는 {dust} 입니다.")


# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.
if(150 < dust):
  print("매우나쁨")
elif(80 < dust <= 150):
  print("나쁨")
elif(30 < dust and dust <= 80):
  print("보통")
else:
  print("좋음")
```

3-5. 반복문 활용하기 - 여러번인사

```python
greeting = "안녕하세요??"

for i in range(5):
    print(greeting)
```

- 웹 API 란?
  - 미세먼지 데이터 살펴보기

3-6. 외장함수 - 로또

```python
import random

numbers = list(range(1,46))
lotto = random.sample(numbers, 6)
print(lotto)
```

```python
import random

numbers = list(range(1,46))
lotto = random.sample(numbers, 6)
print(sorted(lotto))
```

```python
import random

numbers = list(range(1,46))
lotto = random.sample(numbers, 6)
print(f"오늘의 행운의 번호는 {sorted(lotto)} 입니다")
```

---

### 4. 파이썬 심화

> git bash / python3.6.7 / vscode / typora 설치

- **CLI**
  - 명령어를 통해서 사용하는 인터페이스로, 기존의 GUI(Graphic User Interface)와는 다르게 터미널(bash/shell/cmd)을 통해서 명령을 할 수 있다.
  - [유용한 bash 명령어](https://nolboo.kim/blog/2015/12/01/bash-command/)
- **markdown**
  - [markdown guide](https://www.markdownguide.org/basic-syntax)

4-1 웹브라우저 조작 (python console 에서 간단히 진행)

```python
import webbrowser

webbrowser.open("https://www.google.com/")
webbrowser.open_new("https://www.google.com/")
webbrowser.open_new_tab("https://www.google.com/")
```

---

### 5. git

### [git](https://git-scm.com/book/ko/v1/Git%EB%A7%9E%EC%B6%A4-Git-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)

- `Git`은 분산형버전관리시스템(DVCS - Distributed Version Control System)이다.

  소스코드의 버전 관리를 할 수 있고, 이력이 관리된다.

- 사용자 정보 설정

> 메일주소는 반드시 GitHub 계정과 동일해야하고 유저네임도 맞춰주는 것이 좋다.
>
>  `--global` 옵션으로 설정하는 것은 딱 한 번만 하면 된다. 해당 시스템에서 해당 사용자가 사용할 때는 이 정보를 사용한다. (만약 프로젝트마다 다른 이름과 이메일 주소를 사용하고 싶으면 `--global` 옵션을 빼고 명령을 실행한다.)

```bash
$ git config --global user.name "###"
$ git config --global user.email "test@example.com"
```

- git 명령어 자동 색칠

```bash
$ git config --global color.ui true
```

> Mac 에서 한글파일명 깨짐 및 commit 오류 문제 해결
>
> ```bash
> $ git config --global core.precomposeunicode true
> $ git config --global core.quotepath false
> ```

- 설정 확인

```bash
$ git config --global --list
```

---

#### 기초 명령어 정리

```bash
$ git init
$ git add .
$ git commit -m "example"
$ git remote add origin https://github.com/example		# remote 는 한번만
$ git push -u origin master							# 첫 push 이후로는 git push 만 입력
```

##### 1. git 저장소 설정

```bash
$ git init
student@DESKTOP MINGW64 ~/Desktop/TIL (master)
$
```

**주의!! 반드시 현재 디렉토리에 git을 사용하고 있는지, (master) 있는지 확인 할 것**

#### 2. git add

`git add`는 현재 `working directory` 에서 `commit` 할 목록에 담아놓는 것이다.

그리고 그 목록은 `INDEX(staging area)` 라고 한다.

```bash
$ touch a.txt
$ git add .
```

- `git add a.txt`를 해도 되지만, 우선 `git add .` 을 하자!!
- `.` 은 리눅스 상에서 현재 디렉토리를 뜻한다.

#### 3. git commit

`git commit`은 현재 소스코드 상태를 스냅샷을 찍는 것과 동일하다.

`staging area`에 담겨 있는 내용을 이력으로 기록한다.

```bash
$ git status
$ git commit -m "커밋메시지"
```

#### 4. git status

git의 현재 상태를 확인한다. 자주자주 입력해보자!

```bash
$ git status
```

------

#### 원격 저장소로 보내기(git push)

사전에 github 에 저장소(repository)를 만들어 놓는다.

1. github 저장소(원격저장소) `url`를 `origin` 이라는 이름으로 설정한다.

```bash
$ git remote add origin https://github.com/example/TIL.git
```

2. 원격 저장소로 보낸다.(push)

```bash
$ git push -u origin master
```

- git 학습 사이트
  - [git 입문](https://backlog.com/git-tutorial/kr/intro/intro1_1.html)
  - [git 간편안내서](https://rogerdudler.github.io/git-guide/index.ko.html)

