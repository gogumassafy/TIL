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
            k, d, r, c = queue.pop(0)
            if visited[t % 2][r][c] > 1:
                result += k
                visited[t % 2][r][c] = 0
                continue
            visited[t % 2][r][c] = 0
            nr = r + dr[d]
            nc = c + dc[d]
            if not (2001 > nr >= 0 and 2001 > nc >= 0):
                continue
            if visited[(t + 1) % 2][nr][nc]:
                result += k
                visited[(t + 1) % 2][nr][nc] += 1
                continue
            visited[(t + 1) % 2][nr][nc] += 1
            queue.append((k, d, nr, nc))
        t += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # -1000 ~ 1000
    # 0 ~ 2000
    visited = [[[0] * 2001 for _ in range(2001)] for _ in range(2)]
    queue = []
    for i in range(N):
        c, r, d, k = map(int, input().split())
        r = 2000 - (r + 1000)
        c = c + 1000
        # 크기, 방향, r, c
        queue.append((k, d, r, c))
        visited[0][r][c] = 1
    result = 0
    bfs()
    print('#{} {}'.format(tc, result))
