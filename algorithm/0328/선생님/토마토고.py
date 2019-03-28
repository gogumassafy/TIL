import sys
sys.stdin = open("input.txt")

def BFS():
    que=[]
    dr =(-1, 1, 0, 0) #상하좌우 행증감치
    dc =(0, 0, -1, 1)
    zero =0 # 0의 개수
    r, c, day = 0, 0, 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] ==1: # 익은 토마토자리를 모두 시작점으로 큐에저장
                que.append((i, j, 0))
            elif arr[i][j]==0: zero+=1 # 0의 개수 카운트
    if zero==0: return 0 # 모두 익힌상태라면 리턴
    while que:
        r, c, day = que.pop(0)#2] 큐에서 데이타 읽기(현재좌표)
        for i in range(4):
            nr = r + dr[i]
            nc = c+ dc[i]
            if nr<0 or nr>=R or nc<0 or nc>=C : continue #맵의 범위를 벗어나면 스킵
            if arr[nr][nc] == 0: # 안익은 토마토라면
                que.append((nr, nc, day+1))
                arr[nr][nc]=1 # 맵에 방문표시
                zero-=1 # 익혀가면서 차감
    if zero : return -1 # 모두 못익힌 상태라면 -1리턴
    else: return  day #모두 익힌 상태라면 최소일자를 리턴

#main -----------------------------------
C, R = map(int, input().split())
arr = []
for i in range(R):
    arr.append(list(map(int, input().split())))
print( BFS())
