import queue

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global R, C, H
    while not q.empty():
        h, r, c = q.get()
        # 우선 같은 층의 애들부터 전염
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (R > nr >= 0 and C > nc >= 0):
                continue
            if visited[h][nr][nc]:
                continue
            if raw[h][r][c]:
                continue

        print(h, r, c)
    return


C, R, H = map(int, input().split())
raw = [[list(map(int, input().split())) for _ in range(R)] for _ in range(H)]
visited = [[[0] * C for _ in range(R)] for _ in range(H)]
q = queue.Queue()
count = 0
for height in range(H):
    for row in range(R):
        for col in range(C):
            if raw[height][row][col] == 1:
                visited[height][row][col] = 1
                q.put((height, row, col))
            elif raw[height][row][col] == -1:
                count += 1
bfs()