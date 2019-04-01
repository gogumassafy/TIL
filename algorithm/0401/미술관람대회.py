import sys, queue
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global N
    while not q.empty():
        color, r, c = q.get()
        if raw[r][c] == "G":
            raw[r][c] = "R"
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            if raw[nr][nc] != color:
                continue
            visited[nr][nc] = 1
            q.put((color, nr, nc))


N = int(input())
raw = [list(input().strip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count1 = 0
count2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            q = queue.Queue()
            q.put((raw[i][j], i, j))
            bfs()
            count1 += 1
bfs()
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            q = queue.Queue()
            q.put((raw[i][j], i, j))
            bfs()
            count2 += 1
print(count1, count2)
