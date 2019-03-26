import queue

# dr = [-3, -3, -2, -2, 2, 2, 3, 3]
# dc = [-2, 2, -3, 3, -3, 3, -2, 2]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
dr2 = [[-1, -1], [1, 1], [-1, 1], [-1, 1]]
dc2 = [[-1, 1], [-1, 1], [-1, -1], [1, 1]]


def bfs(r, c):
    visited[r][c] = 1
    q.put((r, c))
    while not q.empty():
        row, col = q.get()
        if raw[row][col] == 1:
            return visited[row][col] - 1
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if not (10 > nr >= 0 and 9 > nc >= 0):
                continue
            if raw[nr][nc]:
                continue
            for j in range(2):
                for dis in range(1, 3):
                    nnr = nr + dr2[i][j]*dis
                    nnc = nc + dc2[i][j]*dis
                    if not (10 > nnr >= 0 and 9 > nnc >= 0):
                        break
                    if dis == 1 and raw[nnr][nnc]:
                        break
                else:
                    if visited[nnr][nnc]:
                        continue
                    visited[nnr][nnc] = visited[row][col] + 1
                    q.put((nnr, nnc))


eRow, eCol = map(int, input().split())
kRow, kCol = map(int, input().split())
raw = [[0] * 9 for _ in range(10)]
visited = [[0] * 9 for _ in range(10)]
raw[kRow][kCol] = 1
q = queue.Queue()
count = bfs(eRow, eCol)
print(count)
