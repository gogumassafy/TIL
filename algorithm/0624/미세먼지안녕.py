import copy
# 상우하좌
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


def clean():
    global R, C
    cleaned = 0
    for i in range(len(cleaner)):
        if i == 0:
            d = 0
        else:
            d = 2
        r, c = cleaner[i]
        while 1:
            nr = r + dr[d]
            nc = c + dc[d]
            if not (R > nr >= 0 and C > nc >= 0):
                if i:
                    d = (d - 1) % 4
                else:
                    d += 1
                continue
            if raw[nr][nc] == -1:
                raw[r][c] = 0
                break
            if nc == (C - 1) and nr == cleaner[i][0]:
                if i:
                    d = (d - 1) % 4
                else:
                    d += 1
            if raw[r][c] != -1:
                raw[r][c] = raw[nr][nc]
            else:
                cleaned += raw[nr][nc]
            r = nr
            c = nc


def spread(q):
    global R, C, raw
    temp = copy.deepcopy(raw)
    while q:
        r, c = q.pop(0)
        count = 0
        target = []
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (R > nr >= 0 and C > nc >= 0):
                continue
            if temp[nr][nc] == -1:
                continue
            count += 1
            target.append((nr, nc))
        if count == 0:
            continue
        numberOfDust = raw[r][c] // 5
        temp[r][c] -= numberOfDust * count
        for tr, tc in target:
            temp[tr][tc] += numberOfDust
    raw = copy.deepcopy(temp)


def init():
    global R, C, T
    for t in range(T):
        q = []
        for i in range(R):
            for j in range(C):
                if raw[i][j] >= 5:
                    q.append((i, j))
        spread(q)
        clean()
    return


R, C, T = map(int, input().split())
raw = [list(map(int,input().split())) for _ in range(R)]
for i in range(2, R - 2):
    if raw[i][0] == -1:
        cleaner = [(i, 0), (i + 1, 0)]
        break
init()
result = 0
for i in range(R):
    for j in range(C):
        if raw[i][j] > 0:
            result += raw[i][j]
print(result)
