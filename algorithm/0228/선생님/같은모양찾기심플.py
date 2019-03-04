
M = int(input())
mArr = [] #모눈종이 맵
for i in range(M):
    mArr.append(list(map(int, input())))
P = int(input())
pArr = [] #패턴맵
for i in range(P):
    pArr.append(list(map(int, input())))

def check(i, j):
    flag = 0
    for k in range(P):  # 패턴행
        for l in range(P):  # 패턴열
            if mArr[i + k][j + l] != pArr[k][l]:
                return 0 # 실패
    return 1  # 패턴찾음

sol=0
for i in range(  M-P ): #모눈종이의 시작행 제어
    for j in range( M-P ):#모눈종이의 시작열 제어
        if check(i, j)==1:
            sol+=1

print(sol)










