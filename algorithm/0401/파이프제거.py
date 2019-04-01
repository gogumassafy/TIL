import sys, queue
input = sys.stdin.readline

# 상좌하우
pipe = [(0, 0, 0, 0), (0, 1, 0, 1), (1, 0, 1, 0), (0, 0, 1, 1), (0, 1, 1, 0), (1, 1, 0, 0), (1, 0, 0, 1), (1, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 0), (1, 1, 0, 1), (1, 1, 1, 1)]
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def bfs():
    global N, count
    while not q.empty():
        p, r, c = q.get()
        count -= 1
        for i in range(4):
            if not pipe[p][i]:
                continue
            nr = r + dr[i]
            nc = c + dc[i]
            npi = (i + 2) % 4
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            if not pipe[raw[nr][nc]][npi]:
                continue
            visited[nr][nc] = 1
            q.put((raw[nr][nc], nr, nc))
            raw[nr][nc] = 0


N = int(input())
C, R = map(int, input().split())
raw = [list(input().strip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if raw[i][j].isalpha():
            raw[i][j] = ord(raw[i][j]) - ord('A') + 10
        else:
            raw[i][j] = int(raw[i][j])
        if raw[i][j]:
            count += 1
q = queue.Queue()
q.put((raw[R][C], R, C))
visited[R][C] = 1
bfs()
print(count)
