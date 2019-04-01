dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(stack):
    global H, W
    cnt = 0
    while stack:
        d, r, c = stack.pop()
        size = data[d][r][c]
        data[d][r][c] = 0
        cnt += 1
        for dis in range(1, size):
            for i in range(4):
                nr = r + dr[i]*dis
                nc = c + dc[i]*dis
                if not (H > nr >= 0 and W > nc >= 0):
                    continue
                if not data[d][nr][nc]:
                    continue
                stack.append((d, nr, nc))
    return cnt


def cpy(depth):
    for i in range(H):
        if depth == 1:
            data[0][i] = raw[i][:]
        else:
            data[depth][i] = data[depth - 1][i][:]


def start(depth, total):
    global N, W, H, result
    stack = []
    if depth == N:
        result = max(result, total)
        return
    for col in range(W):
        cpy(depth)
        cnt = 0
        for row in range(H):
            if data[depth][row][col]:
                stack.append((depth, row, col))
                cnt = dfs(stack)
                break
        else:
            continue
        gravity(depth)
        start(depth + 1, total + cnt)


def gravity(depth):
    global W, H
    for col in range(W):
        for row in range(H - 1, 0, -1):
            if data[depth][row][col] == 0:
                for row2 in range(row - 1, -1, -1):
                    if data[depth][row2][col]:
                        data[depth][row][col], data[depth][row2][col] = data[depth][row2][col], data[depth][row][col]
            else:
                continue


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(H)]
    data = [[[0] * W for _ in range(H)] for _ in range(N)]
    count = 0
    for i in range(H):
        for j in range(W):
            if raw[i][j]:
                count += 1
    result = 0
    start(0, 0)
    print('#{} {}'.format(tc, count - result))
