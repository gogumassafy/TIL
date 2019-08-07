import sys
sys.stdin = open('핀볼게임.txt')

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

# 상좌하우
blocks = (
    (0, 0, 0, 0), (2, 0, 3, 1), (3, 2, 0, 1), (1, 3, 0, 2), (2, 3, 1, 0), (2, 3, 0, 1)
)


def dfs(sr, sc, direction):
    global result
    count = 0
    nr = sr
    nc = sc
    d = direction
    while 1:
        nr += dr[d]
        nc += dc[d]
        if not (N > nr >= 0 and N > nc >= 0):
            d = (d + 2) % 4
            count += 1
            continue
        if (nr == sr and nc == sc) or raw[nr][nc] == -1:
            result = max(result, count)
            return
        if (6 > raw[nr][nc] > 0):
            d = blocks[raw[nr][nc]][d]
            count += 1
            continue
        if raw[nr][nc] >= 6:
            wormhole = raw[nr][nc]
            for i in range(N):
                for j in range(N):
                    if (raw[i][j] == wormhole and (i != nr or j != nc)):
                        nr = i
                        nc = j
                        break
                else:
                    continue
                break


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if raw[i][j]:
                continue
            for d in range(4):
                dfs(i, j, d)
    print("#{} {}".format(tc, result))
