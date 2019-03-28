import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col):
    global N
    stack = []
    result = 1
    visited[row][col] = 1
    stack.append((row, col))
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            if not raw[nr][nc]:
                continue
            visited[nr][nc] = 1
            result += 1
            stack.append((nr, nc))
    sol.append(result)


N = int(input())
raw = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count = 0
sol = []

for i in range(N):
    for j in range(N):
        if raw[i][j] and not visited[i][j]:
            count += 1
            dfs(i, j)
print(count)
sol.sort()
for i in sol:
    print(i)
