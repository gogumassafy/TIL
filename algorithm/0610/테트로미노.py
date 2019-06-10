dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def dfs(total, depth, r, c):
    global result
    if depth == 4:
        result = max(result, total)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (N > nr >= 0 and M > nc >= 0):
            continue
        if visited[nr][nc]:
            continue
        visited[nr][nc] = 1
        stack.append((nr, nc))
        dfs(total + raw[nr][nc], depth + 1, nr, nc)
        visited[nr][nc] = 0
        stack.pop()
        

N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        visited = [[0] * M for _ in range(N)]
        stack = [(i, j)]
        visited[i][j] = 1
        dfs(raw[i][j], 1, i, j)
print(result)
