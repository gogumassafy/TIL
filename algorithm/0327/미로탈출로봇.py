import sys, queue
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(startrow, startcol):
    global result, C, R, eCol, eRow
    visited[startrow][startcol] = 1
    q.put((startrow, startcol))
    while not q.empty():
        row, col = q.get()
        if row == eRow and col == eCol:
            result = visited[row][col] - 1
            return
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if not (R + 1 > nr >= 0 and C + 1 > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = visited[row][col] + 1
            q.put((nr, nc))


C, R = map(int, input().split())
sCol, sRow, eCol, eRow = map(int, input().split())
raw = [[1] * (C+2)] + [[1] + list(map(int, input().strip())) + [1] for _ in range(R)] + [[1] * (C + 2)]
visited = raw[:]
result = 0
q = queue.Queue()
bfs(sRow, sCol)
print(result)
