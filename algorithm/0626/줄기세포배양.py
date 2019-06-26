# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def spread():
    global N, M, K
    time = 0
    while q and time < K:
        count = len(q)
        for _ in range(count):
            r, c = q.pop(0)
            if raw[r][c][1] == 0:
                continue
            if raw[r][c][0] == raw[r][c][1]:
                size = raw[r][c][0]
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if not (K + N > nr >= 0 and K + M > nc >= 0):
                        continue
                    if raw[nr][nc][0] == 0:
                        raw[nr][nc] = [size, 2 * size, time]
                        q.append((nr, nc))
                    elif time == raw[nr][nc][2]:
                        if size > raw[nr][nc][0]:
                            raw[nr][nc] = [size, 2 * size, time]
            raw[r][c][1] -= 1
            q.append((r, c))
        time += 1


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    raw = [[[0, 0, 0] for _ in range(M + K)] for _ in range(N + K)]
    start = K // 2
    rowEnd = (K // 2) + N
    colEnd = (K // 2) + M
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(M):
            raw[start + i][start + j] = [temp[j], 2 * temp[j], 0]
    q = []
    for i in range(start, rowEnd):
        for j in range(start, colEnd):
            if raw[i][j][0]:
                q.append((i, j))
    spread()
    result = sum(1 for r, c in q if raw[r][c][1])
    print("#{} {}".format(tc, result))
