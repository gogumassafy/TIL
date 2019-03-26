import queue, sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(k):
    global N, M
    q.put((0, 0, k))
    visited[0][0] = [1] * (k + 1)
    while not q.empty():
        row, col, canbreak = q.get()
        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            if nr == N - 1 and nc == M - 1:
                return visited[row][col][canbreak] + 1
            if not (M > nc >= 0 and N > nr >= 0) or visited[nr][nc][canbreak]:
                continue
            if not raw[nr][nc]:
                q.put((nr, nc, canbreak))
                visited[nr][nc][canbreak] = visited[row][col][canbreak] + 1
            elif raw[nr][nc] and canbreak:
                q.put((nr, nc, canbreak - 1))
                visited[nr][nc][canbreak - 1] = visited[row][col][canbreak] + 1
    return -1


N, M, K = map(int, input().split())
raw = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
q = queue.Queue()
print(bfs(K))
