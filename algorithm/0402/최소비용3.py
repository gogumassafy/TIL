import sys
sys.stdin = open("최소비용_input.txt")

for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[999999]*N for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    D[0][0] = 0
    Q = [(0,0)]
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            tr, tc = r+dr[i], c+dc[i]
            if 0<=tr<N and 0<=tc<N:
                diff = 0
                if arr[tr][tc] > arr[r][c]: diff = arr[tr][tc]-arr[r][c]
                if D[tr][tc] > D[r][c]+diff+1:
                    D[tr][tc] = D[r][c]+diff+1
                    Q.append((tr, tc))
    print("#%d"%(T+1), D[N-1][N-1])