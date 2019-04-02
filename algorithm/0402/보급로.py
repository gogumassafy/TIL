import collections


def bfs():
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            cost = raw[nr][nc]
            if D[nr][nc] > D[r][c] + cost:
                D[nr][nc] = D[r][c] + cost
                q.append((nr, nc))


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input())) for _ in range(N)]
    D = [[float('inf')] * N for _ in range(N)]
    q = collections.deque()
    q.append((0, 0))
    D[0][0] = 0
    bfs()
    print('#{} {}'.format(tc, D[N - 1][N - 1]))

