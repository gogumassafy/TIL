import sys, queue
sys.stdin = open('탈주범검거.txt')

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 상 하 좌 우
pump = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]


def bfs(r, c, limit):
    global N, M
    t = 1
    count = 1
    q.put([r, c, t])
    raw[r][c] = -1
    while not q.empty():
        row, col, time = q.get()
        if time <= limit:
            count += 1
        else:
            break
        nt = time + 1
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if N > nr >= 0 and M > nc >= 0 and pump[raw[r][c]][i] and pump[raw[nr][nc]][i] and raw[nr][nc] != -1:
                q.put([nr, nc, nt])
                raw[nr][nc] = -1
    return count


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]
    q = queue.Queue()
    result = bfs(R, C, L)
    print('#{} {}'.format(tc, result))
