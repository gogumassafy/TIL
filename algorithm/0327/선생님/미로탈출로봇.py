import sys
sys.stdin = open("input.txt")

def BFS():
    que=[]
    dr =(-1, 1, 0, 0) #상하좌우 행증감치
    dc =(0, 0, -1, 1)
    # 1] 시작점을 큐에저장(방문표시)
    que.append((sr, sc, 0)) # 행, 열, 시간 큐에 저장
    arr[sr][sc] = 1 # 맵에 방문표시
    while que: #큐가 있을동안 반복
        r, c, time = que.pop(0)#2] 큐에서 데이타 읽기(현재좌표)
        if r==er and c == ec : return time # 도착하면 리턴
        for i in range(4): #3] 사방탐색하면서 연결점(길)을 찾아 큐에저장
            nr = r + dr[i]
            nc = c+ dc[i]
            if nr<0 or nr>=R or nc<0 or nc>=C : continue #맵의 범위를 벗어나면 스킵
            if arr[nr][nc] !=0 : continue # 길이 아니면 스킵
            que.append((nr, nc, time+1))
            arr[nr][nc]=1 # 맵에 방문표시
    return -1 #4] 큐가 빈상태(예외상황)

#main -----------------------------------
C, R = map(int, input().split())
sc, sr, ec, er = map(int, input().split())
sc-=1; sr-=1; ec-=1; er-=1
arr = []
for i in range(R):
    arr.append(list(map(int, input())))

print( BFS())
