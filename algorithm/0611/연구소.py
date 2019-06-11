import copy
import itertools

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def bfs():
    global N, M, safe, result
    while q:
        if safe <= result:
            return
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and M > nc >= 0):
                continue
            if lab[nr][nc]:
                continue
            lab[nr][nc] = 2
            safe -= 1
            q.append((nr, nc))
    if safe == 30:
        print('no!')
    result = max(result, safe)


N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
total = 0
germ = []
empty = []
result = 0
for i in range(N):
    for j in range(M):
        if raw[i][j] == 0:
            total += 1
            empty.append((i, j))
        if raw[i][j] == 2:
            germ.append((i, j))


combs = list(itertools.combinations(empty, 3))
# 반복
for comb in combs:
    safe = total - 3
    q = copy.deepcopy(germ)
    lab = copy.deepcopy(raw)
    for r, c in comb:
        lab[r][c] = 1
    bfs()
print(result)