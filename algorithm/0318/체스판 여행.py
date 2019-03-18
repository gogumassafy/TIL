import queue

knight_dr = [-1, -1, -2, -2, 2, 2, 1, 1]
knight_dc = [-2, 2, -1, 1, -1, 1, -2, 2]

rook_dr = [0, 0, 1, -1]
rook_dc = [1, -1, 0, 0]

bishop_dr = [1, -1, 1, -1]
bishop_dc = [1, -1, -1, 1]


def BFS(r, c, p, n):
    global N
    q.put([r, c, p, n])
    visited[r][c] = 1
    while not q.empty():
        row, col, piece, now = q.get()
        if raw[row][col] == n + 1:
            return visited[row][col]
        for i in range(8):
            nr = row + knight_dr[i]
            nc = col + knight_dc[i]
            if N > nr >= 0 and N > nc >= 0 and not visited[nr][nc]:
                q.put([nr, nc, p, n])
                visited[nr][nc] = visited[row][col] + 1
    return 0


N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
q = queue.Queue()
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if raw[i][j] == 1:
            row = i
            col = j
            break
    else:
        continue
    break
# 0: knight, 1: rook, 2: bishop
# wall = N*N
print(BFS(row, col, 0, 1))



# min_length = float('inf')
# for p in range(3):
#     each = BFS(row, col, 0, 1)
#     if min_length > each:
#         min_length = each
# print(min_length)
#
# n = 1
# wall = N*N
# while n < wall:
#     each = BFS(row, col, 0, n)
