import queue

knight_dr = [-1, -1, -2, -2, 2, 2, 1, 1]
knight_dc = [-2, 2, -1, 1, -1, 1, -2, 2]

rook_dr = [0, 0, 1, -1]
rook_dc = [1, -1, 0, 0]

bishop_dr = [1, -1, 1, -1]
bishop_dc = [1, -1, -1, 1]


def BFS(r, c, p, s, t):
    global end
    visited[r][c][s][p] = 1
    q.put([r, c, p, s, t])
    while not q.empty():
        row, col, piece, start, time = q.get()
        if raw[row][col] == start + 1:
            start += 1
            if start == end:
                return time

        nexttime = time + 1
        for i in range(1, 3):
            nextpiece = (piece + i) % 3
            if visited[row][col][start][nextpiece] == -1:
                visited[row][col][start][nextpiece] = 1
                q.put([row, col, nextpiece, start, nexttime])

        if piece == 0:
            for i in range(8):
                nr = row + knight_dr[i]
                nc = col + knight_dc[i]
                if N > nr >= 0 and N > nc >= 0 and visited[nr][nc][start][piece] == -1:
                    visited[nr][nc][start][piece] = 1
                    q.put([nr, nc, piece, start, time + 1])

        elif piece == 1:
            for i in range(4):
                for dis in range(1, 11):
                    nr = row + rook_dr[i] * dis
                    nc = col + rook_dc[i] * dis
                    if N > nr >= 0 and N > nc >= 0:
                        if visited[nr][nc][start][piece] == -1:
                            visited[nr][nc][start][piece] = 1
                            q.put([nr, nc, piece, start, time + 1])
                    else:
                        break
        else:
            for i in range(4):
                for dis in range(1, 11):
                    nr = row + bishop_dr[i] * dis
                    nc = col + bishop_dc[i] * dis
                    if N > nr >= 0 and N > nc >= 0:
                        if visited[nr][nc][start][piece] == -1:
                            visited[nr][nc][start][piece] = 1
                            q.put([nr, nc, piece, start, time + 1])
                    else:
                        break
    return float('inf')


N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
start = 1
end = N*N
time = 0
min_time = float('inf')
for i in range(N):
    for j in range(N):
        if raw[i][j] == start:
            for p in range(3):
                q = queue.Queue()
                visited = [[[[-1] * 3 for _ in range(N * N + 1)] for _ in range(N)] for _ in range(N)]
                each = BFS(i, j, p, start, time)
                if min_time > each:
                    min_time = each
print(min_time)

