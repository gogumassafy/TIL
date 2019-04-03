import sys, collections
input = sys.stdin.readline


def bfs():
    global R, C, result
    while q:
        time = len(water)
        for i in range(time):
            r, c = water.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (R > nr >= 0 and C > nc >= 0):
                    continue
                if raw[nr][nc] == 'X':
                    continue
                if raw[nr][nc] == '*':
                    continue
                if raw[nr][nc] == 'D':
                    continue
                raw[nr][nc] = '*'
                water.append((nr, nc))
        time = len(q)
        for i in range(time):
            r, c = q.popleft()
            if raw[r][c] == 'D':
                result = visited[r][c] - 1
                return
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (R > nr >= 0 and C > nc >= 0):
                    continue
                if raw[nr][nc] == 'X':
                    continue
                if raw[nr][nc] == '*':
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    result = 'KAKTUS'


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
raw = [list(input().strip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
q = collections.deque()
water = collections.deque()
for i in range(R):
    for j in range(C):
        if raw[i][j] == 'S':
            visited[i][j] = 1
            q.append((i, j))
        elif raw[i][j] == '*':
            water.append((i, j))
result = float('inf')
bfs()
print(result)
