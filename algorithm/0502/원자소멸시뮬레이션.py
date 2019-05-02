import sys
sys.stdin = open('원자소멸시뮬레이션.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def bfs():
    global result, N
    t = 0
    while queue:
        n = len(queue)
        for _ in range(n):
            r, c = queue.pop(0)
            k, d = data[t % 2][r][c]
            if k == 0:
                continue
            if data[t % 2][r][c][1] == 9:
                result += k
                data[t % 2][r][c] = [0, 0]
                continue
            data[t % 2][r][c] = [0, 0]
            nr = r + dr[d]
            nc = c + dc[d]
            if not (2001 > nr >= 0 and 2001 > nc >= 0):
                continue
            if data[(t + 1) % 2][nr][nc][0]:
                result += k
                data[(t + 1) % 2][nr][nc][1] = 9
                continue
            if data[t % 2][nr][nc][0]:
                D = data[t % 2][nr][nc][1]
                K = data[t % 2][nr][nc][0]
                if (d == 0 or d == 2) and D == (d + 1):
                    result += (k + K)
                    data[t % 2][nr][nc] = [0, 0]
                    continue
                elif (d == 1 or d == 3) and D == (d - 1):
                    result += (k + K)
                    data[t % 2][nr][nc] = [0, 0]
                    continue
            data[(t + 1) % 2][nr][nc] = [k, d]
            queue.append((nr, nc))
        t += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # -1000 ~ 1000
    # 0 ~ 2000
    data = [[[[0, 0] for _ in range(2001)] for _ in range(2001)] for _ in range(2)]
    queue = []
    for i in range(N):
        c, r, d, k = map(int, input().split())
        r = 2000 - (r + 1000)
        c = c + 1000
        # r, c
        queue.append((r, c))
        data[0][r][c] = [k, d]
    result = 0
    bfs()
    print('#{} {}'.format(tc, result))
