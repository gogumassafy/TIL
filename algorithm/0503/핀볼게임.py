import sys
sys.stdin = open('핀볼게임.txt')

# 상 좌 하 우
dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)
# 벽면
block = ((0, 0, 0, 0), (2, -1, 1, -2), (3, 1, -2, -2), (1, 2, -2, -2), (2, 2, -1, -2), (2, 2, -2, -2))


def dfs(r, c, d):
    global N, result
    cnt = 0
    nr = r
    nc = c
    while 1:
        nr += dr[d]
        nc += dc[d]
        if not (N > nr >= 0 and N > nc >= 0):
            d = (d + 2) % 4
            cnt += 1
            continue
        if raw[nr][nc] == -1 or (nr == r and nc == c):
            result = max(result, cnt)
            return
        elif raw[nr][nc] == 0:
            continue
        elif raw[nr][nc] < 6:
            d += block[raw[nr][nc]][d]
            cnt += 1
        else:
            for wr, wc in wormhole[raw[nr][nc]]:
                if nr != wr and nc != wc:
                    nr = wr
                    nc = wc
                    break


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    wormhole = {6:[], 7:[], 8:[], 9:[], 10:[]}
    for i in range(N):
        for j in range(N):
            if raw[i][j] > 5:
                wormhole[raw[i][j]].append((i, j))

    for i in range(N):
        for j in range(N):
            if raw[i][j] == 0:
                for d in range(4):
                    dfs(i, j, d)
    print('#{} {}'.format(tc, result))
