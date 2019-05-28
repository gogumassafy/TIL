dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def comb(n, r, c):
    global M, count
    if n == M:
        # print(queue)
        bfs(combination[:], count)
        return
    for i in range(r, N):
        for j in range(c + 1, N):
            if raw[i][j] == 2:
                combination.append((i, j))
                comb(n + 1, i, j)
                combination.pop()
        if c >= 0:
            c = -1


def bfs(queue, cnt):
    global result, visited
    visited = [[0] * N for _ in range(N)]
    for i in queue:
        sr, sc = i
        visited[sr][sc] = 1
    while queue:
        time = len(queue)
        for t in range(time):
            r, c = queue.pop(0)
            cnt -= 1
            if visited[r][c] > result:
                return
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (N > nr >= 0 and N > nc >= 0):
                    continue
                if visited[nr][nc]:
                    continue
                if raw[nr][nc] == 1:
                    continue
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))
    if cnt == 0:
        result = min(result, visited[r][c] - 1)


N, M = map(int, input().split())
result = float('inf')
raw = [list(map(int, input().split())) for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if raw[i][j] != 1:
            count += 1
for i in range(N):
    for j in range(N):
        if raw[i][j] == 2:
            combination = [(i, j)]
            comb(1, i, j)

print(result if result != float('inf') else -1)
