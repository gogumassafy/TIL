import sys
import collections
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global N
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if D[nr][nc] > D[r][c] + raw[nr][nc]:
                D[nr][nc] = D[r][c] + raw[nr][nc]
                q.append((nr, nc))


N = int(input())
raw = [list(map(int, input().strip())) for _ in range(N)]
D = [[float('inf')] * N for _ in range(N)]
q = collections.deque()
q.append((0, 0))
D[0][0] = raw[0][0]
bfs()
print(D[N - 1][N - 1])
