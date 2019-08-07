import copy
import sys
sys.stdin = open("벽돌깨기.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def dfs(depth, count):
    global total
    if total == result:
        return
    if depth == N or count == result:
        total = max(total, count)
        return
    for i in range(W):
        for j in range(H):
            if raw_data[depth][j][i]:
                dfs(depth + 1, count + boom(depth, j, i))
                break


def boom(depth, sr, sc):
    global W, H
    boom_count = 0
    raw_data[depth + 1] = copy.deepcopy(raw_data[depth])
    stack = [(sr, sc)]
    while stack:
        r, c = stack.pop()
        power = raw_data[depth + 1][r][c]
        if power == 0:
            continue
        raw_data[depth + 1][r][c] = 0
        boom_count += 1

        for i in range(4):
            for j in range(1, power):
                nr = r + dr[i] * j
                nc = c + dc[i] * j
                if not (W > nc >= 0 and H > nr >= 0):
                    break
                if raw_data[depth + 1][nr][nc] == 0:
                    continue
                stack.append((nr, nc))
    down(depth + 1)
    return boom_count


def down(depth):
    global W, H
    remain = []
    for c in range(W):
        for r in range(H):
            if raw_data[depth][r][c]:
                remain.append(raw_data[depth][r][c])
        remain = [0] * (H - len(remain)) + remain
        for r in reversed(range(H)):
            raw_data[depth][r][c] = remain.pop()


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    raw_data = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(N + 1)]
    result = 0
    total = 0
    for i in range(H):
        raw_data[0][i] = list(map(int, input().split()))
        result += sum(1 for j in raw_data[0][i] if j)
    dfs(0, 0)
    print("#{} {}".format(tc, result - total))
