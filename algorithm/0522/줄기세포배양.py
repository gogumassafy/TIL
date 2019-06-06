import sys
import copy
sys.stdin = open('줄기세포배양.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global N, M, K, result
    for t in range(K):
        length = len(q)
        for l in range(length):
            r, c = q.pop(0)
            size, wait, life = data[t % 2][r][c]

            if wait > 0:
                data[(t + 1) % 2][r][c] = [size, wait - 1, life]
                q.append((r, c))
            elif size == life:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if not (K + N > nr >= 0 and K + M > nc >= 0):
                        continue
                    if data[t % 2][nr][nc] != 0:
                        continue
                    if data[(t + 1) % 2][nr][nc] != 0 and data[(t + 1) % 2][nr][nc][0] > size:
                        continue
                    if data[(t + 1) % 2][nr][nc] == 0:
                        q.append((nr, nc))
                    data[(t + 1) % 2][nr][nc] = [size, size, size]
            if wait == 0 and life > 0:
                data[(t + 1) % 2][r][c] = [size, 0, life - 1]
                if life > 1:
                    q.append((r, c))
    result = len(q)


T = int(input())
for tc in range(1, T + 1):
    q = []
    N, M, K = map(int, input().split())
    raw = [[0] * (M + K) for _ in range(N + K)]
    data =[copy.deepcopy(raw) for _ in range(2)]
    for row in range(N):
        cell = list(map(int, input().split()))
        raw[K//2 + row][K//2:K//2 + M] = cell
    result = 0
    for i in range(K + N):
        for j in range(K + M):
            if raw[i][j]:
                data[0][i][j] = [raw[i][j], raw[i][j], raw[i][j]]
                q.append((i, j))
    bfs()
    print('#{} {}'.format(tc, result))
