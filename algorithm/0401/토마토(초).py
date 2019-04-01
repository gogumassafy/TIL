import queue

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global R, C, H, count, result
    while not q.empty():
        h, r, c = q.get()
        # 위, 아래 층 전염
        for i in range(-1, 2, 2):
            nh = h + i
            if not H > nh >= 0:
                continue
            if visited[nh][r][c]:
                continue
            if raw[nh][r][c]:
                continue
            visited[nh][r][c] = visited[h][r][c] + 1
            raw[nh][r][c] = 1
            q.put((nh, r, c))
            count -= 1
        # 같은 층의 애들 전염
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (R > nr >= 0 and C > nc >= 0):
                continue
            if visited[h][nr][nc]:
                continue
            if raw[h][nr][nc]:
                continue
            visited[h][nr][nc] = visited[h][r][c] + 1
            raw[h][nr][nc] = 1
            q.put((h, nr, nc))
            count -= 1
    if count != 0:
        result = -1
        return
    result = visited[h][r][c] - 1


C, R, H = map(int, input().split())
raw = [[list(map(int, input().split())) for _ in range(R)] for _ in range(H)]
visited = [[[0] * C for _ in range(R)] for _ in range(H)]
q = queue.Queue()
count = 0
result = 0
for height in range(H):
    for row in range(R):
        for col in range(C):
            if raw[height][row][col] == 1:
                visited[height][row][col] = 1
                q.put((height, row, col))
            elif raw[height][row][col] == 0:
                count += 1
bfs()
print(result)