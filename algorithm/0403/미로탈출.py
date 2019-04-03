import sys
import collections
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global R, C
    while q:
        b, r, c = q.popleft()
        if raw[r][c] == 4:
            return visited[b][r][c] - 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (R > nr >= 0 and C > nc >= 0):
                continue
            if visited[b][nr][nc]:
                continue
            if raw[nr][nc] == 1:
                continue
            elif raw[nr][nc] == 2:
                if b > 0:
                    nb = b - 1
                    visited[nb][nr][nc] = visited[b][r][c] + 1
                    q.append((nb, nr, nc))
            else:
                visited[b][nr][nc] = visited[b][r][c] + 1
                q.append((b, nr, nc))
    return -1


R, C = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(R)]
visited = [[[0] * C for _ in range(R)] for _ in range(4)]
q = collections.deque()
# 폭탄의 수와 위치를 들고있는다.
for i in range(R):
    for j in range(C):
        if raw[i][j] == 3:
            visited[3][i][j] = 1
            q.append((3, i, j))
print(bfs())
