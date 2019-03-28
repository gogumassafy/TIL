import queue

fr = [-1, 1, 0, 0]
fc = [0, 0, -1, 1]
sr = [[-1, -1], [1, 1], [-1, 1], [-1, 1]]
sc = [[-1, 1], [-1, 1], [-1, -1], [1, 1]]


def bfs():
    global N, M
    while not q.empty():
        r, c = q.get()
        for i in range(4):
            nr = r + fr[i]
            nc = c + fc[i]
            if not (N > nr >= 0 and M > nc >= 0):
                continue
            if visited[nr][nc] == -1:
                continue
            for j in range(2):
                nnr = nr + sr[i][j]
                nnc = nc + sc[i][j]
                if not (N > nnr >= 0 and M > nnc >= 0):
                    continue
                if visited[nnr][nnc] == -1:
                    return visited[r][c]
                if visited[nnr][nnc]:
                    continue
                visited[nnr][nnc] = visited[r][c] + 1
                q.put((nnr, nnc))


N, M = map(int, input().split())
# 말: R, C
# 졸: S, K
R, C, S, K = map(int, input().split())
visited = [[0] * M for _ in range(N)]
q = queue.Queue()
visited[R][C] = 1
q.put((R, C))
visited[S][K] = -1
print(bfs())
