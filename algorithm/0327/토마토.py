import queue

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def bfs():
    global R, C
    while not q.empty():
        r, c = q.get()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (R > nr >= 0 and C > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            if raw[nr][nc] != 0:
                continue
            visited[nr][nc] = visited[r][c] + 1
            raw[nr][nc] = 1
            q.put((nr, nc))
    return visited[r][c] - 1


C, R = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
q = queue.Queue()
for i in range(R):
    for j in range(C):
        if raw[i][j] == 1:
            visited[i][j] = 1
            q.put((i, j))
ret = bfs()
for i in range(R):
    for j in range(C):
        if raw[i][j] == 0:
            ret = -1
print(ret)

