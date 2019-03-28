import sys
sys.stdin = open("input.txt")

# def BFS():
#     #1] 시작점을 큐에저장(방문표시)
#     while que: #큐가 있을동안 반복
#         #2] 큐에서 데이타 꺼내기(현재위치)
#         #3] 사방탐색하면서 연결점(길)을 찾아 큐에저장
#             #3-1] 맵 범위 체크
#             #3-2] 연결점찾아 큐에저장(방문표시)
#     #4] 큐가 빈상태

def BFS():
    que=[]
    dr =(-1, 1, 0, 0) #상하좌우 행증감치
    dc =(0, 0, -1, 1)
    que.append((sr, sc, 3))
    arr[sr][sc] = 0 # 맵에 방문표시
    while que:
        r, c, time = que.pop(0)#2] 큐에서 데이타 읽기(현재좌표)
        for i in range(4):
            nr = r + dr[i]
            nc = c+ dc[i]
            if nr<0 or nr>=R or nc<0 or nc>=C : continue #맵의 범위를 벗어나면 스킵
            if arr[nr][nc] ==1: # 저글링이면
                que.append((nr, nc, time+1))
                arr[nr][nc]=0 # 맵에 방문표시
    return  time #4] 큐가 빈상태(더이상 없앨 저글링이 없는 경우)

#main -----------------------------------
C, R = map(int, input().split())
arr = []
for i in range(R):
    arr.append(list(map(int, input())))
sc, sr = map(int, input().split())
sc-=1; sr-=1;
print( BFS())
