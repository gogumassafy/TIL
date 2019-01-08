## Day_2_2

## 파일 읽고 쓰기

> linux에서 touch a.txt로 파일 만들고 지우고, 삭제하고 했던 내용 remind
>
> 이걸 이제 파이썬으로만으로도 가능하다!

### 1. 파일 생성하기

> `f` 는 파일 객체이다. 
>
> 객체는 무엇일까? 영어로는 object. 그냥 간단히  

* 윈도우 혹시모르니 open시 `encoding='utf8'` 주의하자.

```python
# 첫번째 방법
f = open("new.txt", "w") # C:/python/new.txt 윈도우 절대경로
f.write("글써져랏!")
f.close()
# 열기 모드에는 r: 읽기  w: 쓰기(write - 오버라이트됨) a: 추가(append)

# 두번째 방법 - 추천**
"""
파이썬에서 with 구문은 '컨텍스트 매니저' 이다.
with 블록을 통해 명시적으로 파일을 불러서 작업하는 코드 블록을 만들 수 있다. 
with 블록이 종료되면 자동으로 파일을 닫으며, close() 메소드를 호출하지 않고 파일을 닫는다. 
덧) 파일 객체내에 내부적으로 구현되어 있는 __exit__() 메소드를 호출함. 
"""
with open("new.txt", "w") as f:
    f.write("글 다시 써져랏!")

```

### 2. 파일 열고 내용 가져오기

```python
f = open("new.txt", "r")
data = f.read()
print(data)
f.close()

# 두번째 방법
with open("new.txt", "r") as f:
    data = f.read()
    print(data)
```

### 3. 여러 줄 쓰기

```python
f = open("new.txt", 'w')
for i in range(1, 3):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

# 두번째 방법
with open("new.txt", 'w') as f:
    for i in range(1, 3):
    	data = f"{i}번째 줄입니다.\n"
    	f.write(data)
''' 참고
파이썬 escape sequence
\n : 개행문자(다음 줄 이동)
\t : 탭문자 (키보드 Tab키 여러칸 띄움)
\\ : 백슬래쉬를 쓰기 위해서
\', \"
advanced? \r : 캐리지리턴 
윈도우는 \r\n CRLF(carriage return + line feed)
유닉스는 \n LF(Line Feed)
LF는 커서의 위치는 그대로 두고 종이를 한 라인 위로 올리는 동작을,
CR는 현재 라인에서 커서의 위치를 맨 앞으로 옮기는 동작을 의미했다고 한다.
CR + LF 는 두 동작을 합해서, 커서를 다음 라인의 맨 앞으로 옮겨주는 것이었다.
'''
```

### 4. 여러 줄 쓰기 - 2

```python
menu = ["중국집", "일식집", "한식집", "분식집"]
f = open("menu.txt", "w")
f.writelines(menu)
f.close()
# writelines 엔터치려면 "중국집\n" 이렇게 되어있어야함! 개행문자포함
# 두번째 방법

with open('menu.txt', 'w') as f:  
    f.writelines(menu)
```

### 5. 여러 줄 읽기 : `readline()` 반복, `readlines()` 

```python
# 비추 1-1 : 무식
with open("new.txt", "r") as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
# 엔터 두번이지! \n이 있어서 그래. 
# .strip() 알려주기

# 비추 1-2 : 반복 
with open("new.txt", "r") as f:
    while True:
        line = f.readline()
        if not line: 
            break
        print(line.strip())

# 이것만 알려줄래
with open("new.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

# 근데 이렇게도 됨!
with open("new.txt", "r") as f:
    for line in f:
        print(line)
```

* 정리 :
  `readline()` : 한 줄을 읽어 return 
  `readlines()` : 파일 전체를 읽어 list 형태로 return 
  `read()` : 파일 전체를 읽어 문자열로 return 

