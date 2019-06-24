import itertools

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def select(depth, k):
    global M
    if depth == M and len(selected) == 3:
        return
    for i in range(k, len(store)):
        selected.append(store[i])
        select(depth + 1, i)
        selected.pop()


def check(sr, sc):
    global N, total
    q = [(sr, sc)]
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    while q:
        r, c = q.pop(0)
        if (r, c) in comb:
            total += visited[r][c] - 1
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))


N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
store = []
house = []
selected = []
result = float('inf')
for i in range(N):
    for j in range(N):
        if raw[i][j] == 2:
            store.append((i, j))
        if raw[i][j] == 1:
            house.append((i, j))
combs = list(itertools.combinations(store, M))
for comb in combs:
    total = 0
    for r, c in house:
        if total >= result:
            break
        check(r, c)
    result = min(result, total)
print(result)
