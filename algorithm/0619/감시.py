# 상, 좌, 하, 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

cctv = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]


def dfs(N, depth, total):
    global result
    if result == 0:
        return
    if depth == N:
        result = min(result, total)
        return
    cctvNum = raw[stack[depth][0]][stack[depth][1]]
    for i in range(4):
        newDirection = cctv[cctvNum][i + 1:4] + cctv[cctvNum][0:i + 1]
        num = check(depth, newDirection)
        dfs(N, depth + 1, total - num)
        clear(depth, newDirection)
        if cctvNum == 5:
            break


def check(depth, direction):
    global N, M
    count = 0
    for i in range(4):
        if not direction[i]:
            continue
        r, c = stack[depth]
        while 1:
            r = r + dr[i]
            c = c + dc[i]
            if not (N > r >= 0 and M > c >= 0):
                break
            if raw[r][c] == 6:
                break
            if raw[r][c] == 0:
                raw[r][c] = 10
            elif raw[r][c] < 6:
                continue
            else:
                raw[r][c] += 1
                continue
            count += 1
    return count


def clear(depth, direction):
    for i in range(4):
        if not direction[i]:
            continue
        r, c = stack[depth]
        while 1:
            r = r + dr[i]
            c = c + dc[i]
            if not (N > r >= 0 and M > c >= 0):
                break
            if raw[r][c] == 6:
                break
            if raw[r][c] == 10:
                raw[r][c] = 0
            elif raw[r][c] > 10:
                raw[r][c] -= 1


N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
count = 0
stack = []
for i in range(N):
    for j in range(M):
        if raw[i][j] == 0:
            count += 1
        if 6 > raw[i][j] > 0:
            stack.append((i, j))
result = count
dfs(len(stack), 0, count)
print(result)