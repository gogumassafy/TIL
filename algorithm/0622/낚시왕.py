# 0 상 하 우 좌
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, 1, -1)


def shark_move(c):
    global R, C
    stack = []
    time = c % 2
    for i in range(R):
        for j in range(C):
            if raw[time][i][j] == [0, 0, 0]:
                continue
            stack.append((i, j))

    while stack:
        r, c = stack.pop()
        s, d, z = raw[time][r][c]
        raw[time][r][c] = [0, 0, 0]
        for i in range(s):
            if d == 1 and r == 0:
                d += 1
            elif d == 2 and r == R - 1:
                d -= 1
            elif d == 3 and c == C - 1:
                d += 1
            elif d == 4 and c == 0:
                d -= 1
            r += dr[d]
            c += dc[d]
        next = (time + 1) % 2
        if raw[next][r][c][2] < z:
            raw[next][r][c] = [s, d, z]


def fishing(c):
    global R, total
    now = c % 2
    for r in range(R):
        if raw[now][r][c] == [0, 0, 0]:
            continue
        total += raw[now][r][c][2]
        raw[now][r][c] = [0, 0, 0]
        break
    return


def dfs():
    global R, C

    for i in range(C):
        fishing(i)
        shark_move(i)


R, C, M = map(int, input().split())
raw = [[[[0, 0, 0] for _ in range(C)] for _ in range(R)] for _ in range(2)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    raw[0][r - 1][c - 1] = [s, d, z]
total = 0
dfs()
print(total)
