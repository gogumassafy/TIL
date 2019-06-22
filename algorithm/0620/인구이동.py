dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def bfs(queue, visited):
    global N, L, R, result
    total, count = 0, 0
    temp = []
    while queue:
        r, c = queue.pop(0)
        total += raw[r][c]
        count += 1
        temp.append((r, c))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            if not (R >= abs(raw[r][c] - raw[nr][nc]) >= L):
                continue
            queue.append((nr, nc))
            visited[nr][nc] = 1
    if count == 1:
        return 0
    avg = total // count
    for r, c in temp:
        raw[r][c] = avg
    # result += 1
    return 1


def init():
    global N, result
    flag = 1
    while flag:
        flag = 0
        visited = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if visited[i][j]:
                    continue
                queue = [(i, j)]
                visited[i][j] = 1
                if bfs(queue, visited):
                    flag = 1
        if flag:
            result += 1


N, L, R = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
result = 0
init()
print(result)
