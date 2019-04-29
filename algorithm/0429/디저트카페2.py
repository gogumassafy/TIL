import sys
sys.stdin = open('디저트카페.txt')

dr = (1, 1, -1, -1)
dc = (1, -1, -1, 1)


def DFS(d, r, c):
    global N, sc, sr, result
    for i in range(2):
        if (d + i) == 4:
            return
        nr = r + dr[d + i]
        nc = c + dc[d + i]
        if not (N > nr >= 0 and N > nc >= 0):
            continue
        if nr == sr and nc == sc:
            result = max(result, sum(visited))
            return
        if nr <= sr and nc <= sc:
            continue
        if visited[raw[nr][nc]]:
            continue
        visited[raw[nr][nc]] = 1
        DFS(d + i, nr, nc)
        visited[raw[nr][nc]] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 101
    result = -1
    for i in range(N - 2):
        for j in range(1, N - 1):
            visited[raw[i][j]] = 1
            sr = i
            sc = j
            DFS(0, sr, sc)
            visited[raw[i][j]] = 0
    print('#{} {}'.format(tc, result))


#1 6
#2 -1
#3 4
#4 -1
#5 8
#6 6
#7 14
#8 12
#9 18
#10 30