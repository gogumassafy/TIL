import queue


def bfs():
    global N, result
    while not q.empty():
        r, c = q.get()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if raw[nr][nc] > raw[r][c]:
                ncost = raw[nr][nc] - raw[r][c] + D[r][c] + 1
            else:
                ncost = D[r][c] + 1
            if D[nr][nc] > ncost:
                D[nr][nc] = ncost
                q.put((nr, nc))


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    D = [[float('inf')] * N for _ in range(N)]
    q = queue.Queue()
    q.put((0, 0))
    D[0][0] = 0
    bfs()
    print('#{} {}'.format(tc, D[N-1][N-1]))

