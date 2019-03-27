import queue

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col):
    global N, M, max_count, result
    q = queue.Queue()
    visited = [[0] * N for _ in range(N)]
    count = 0
    if raw[row][col]:
        count = 1
    visited[row][col] = depth = 1
    q.put((row, col))
    while not q.empty():
        num = q.qsize()
        profit = count * M
        cost = cost_list[depth]
        if profit - cost >= 0:
            result = max(result, count)
        if count == max_count or depth == 23:
            return
        if cost_list[depth] > max_profit or result == max_count:
            return
        for i in range(num, 0, -1):
            r, c = q.get()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (N > nr >= 0 and N > nc >= 0):
                    continue
                if visited[nr][nc]:
                    continue
                if raw[nr][nc]:
                    count += 1
                visited[nr][nc] = depth
                q.put((nr, nc))
        depth += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visited = [[0] * N for _ in range(N)]
    cost_list = [1]
    max_count = 0
    for i in range(N):
        for j in range(N):
            if raw[i][j]:
                max_count += 1
    max_profit = max_count * M
    for K in range(1, 24):
        cost_list.append(cost_list[-1] + 4*(K-1))
    for R in range(N):
        if result == max_count:
            break
        for C in range(N):
            bfs(R, C)
            if result == max_count:
                break

    print('#{} {}'.format(tc, result))

# 1 5
# 2 4
# 3 24
# 4 48
# 5 3
# 6 65
# 7 22
# 8 22
# 9 78
# 10 400

