import itertools

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def bfs():
    global N, count, result
    total = 0
    while q:
        r, c = q.pop(0)
        if raw[r][c] != 2:
            total += 1
            time = visited[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            if raw[nr][nc] == 1:
                continue
            q.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1
    if total == count:
        result = min(result, time - 1)


N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
result = float('inf')

virus = []
count = 0

for i in range(N):
    for j in range(N):
        if raw[i][j] == 0:
            count += 1
        elif raw[i][j] == 2:
            virus.append((i, j))
combs = itertools.combinations(virus, M)
if count:
    for comb in combs:
        q = []
        visited = [[0] * N for _ in range(N)]
        for r, c in comb:
            q.append((r, c))
            visited[r][c] = 1
        bfs()
    if result == float('inf'):
        print(-1)
    else:
        print(result)
else:
    print(0)
