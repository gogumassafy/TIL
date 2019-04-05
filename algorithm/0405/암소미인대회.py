import sys
import collections
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs():
    global count, N, M
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and M > nc >= 0):
                continue
            if raw[nr][nc] != 'X':
                continue
            raw[nr][nc] = count
            stack.append((nr, nc))


def bfs():
    global N, M
    while q:
        r, c = q.popleft()
        if raw[r][c] == 2:
            return visited[r][c] - 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and M > nc >= 0):
                continue
            if visited[nr][nc] > visited[r][c] + 1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))


N, M = map(int, input().split())
raw = [list(input().strip()) for _ in range(N)]
visited = [[float('inf')] * M for _ in range(N)]
count = 0
q = collections.deque()
for i in range(N):
    for j in range(M):
        if raw[i][j] == 'X':
            count += 1
            raw[i][j] = count
            stack = []
            stack.append((i, j))
            dfs()
for i in range(N):
    for j in range(M):
        if raw[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 0
print(bfs())
