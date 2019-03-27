import sys, queue
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col):
    global R, C, time
    visited[row][col] = 3
    raw[row][col] = 0
    q.put((row, col))
    while not q.empty():
        r, c = q.get()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (R > nr >= 0 and C > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            if not raw[nr][nc]:
                continue
            raw[nr][nc] = 0
            visited[nr][nc] = visited[r][c] + 1
            q.put((nr, nc))
    time = visited[r][c]


C, R = map(int, input().split())
raw = [list(map(int, input().strip())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
zC, zR = map(int, input().split())
q = queue.Queue()
time = num = 0
bfs(zR - 1, zC - 1)
for i in range(R):
    num += sum(raw[i])
print(time)
print(num)
