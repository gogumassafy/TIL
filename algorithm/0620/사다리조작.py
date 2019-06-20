import sys
sys.stdin = open('사다리조작.txt')

dr = (0, 0, 1)
dc = (-1, 1, 0)


def dfs(n, depth, k):
    global empty, result
    if result <= n:
        return
    if depth == n:
        run(n)
        return
    numberOfempty = len(empty)
    for i in range(k, numberOfempty):
        r, c = empty[i]
        if raw[r][c] or raw[r][c + 1]:
            continue
        raw[r][c] = c + 1
        raw[r][c + 1] = c
        dfs(n, depth + 1, i + 1)
        raw[r][c], raw[r][c + 1] = 0, 0


def run(n):
    global N, H, result
    for i in range(N):
        r, c = 0, i
        while 1:
            if raw[r][c]:
                c = raw[r][c]
            r += 1
            if r == H:
                break
        if c != i:
            return
    result = min(result, n)


N, M, H = map(int, input().split())
raw = [[0] * (N + 1) for _ in range(H)]

for i in range(M):
    a, b = map(int, input().split())
    raw[a - 1][b] = b + 1
    raw[a - 1][b + 1] = b

result = float('inf')
empty = []

for i in range(H):
    for j in range(1, N):
        if raw[i][j] or raw[i][j + 1]:
            continue
        empty.append((i, j))

for i in range(4):
    dfs(i, 0, 0)
    if result != float('inf'):
        break

if result == float('inf'):
    print(-1)
else:
    print(result)
