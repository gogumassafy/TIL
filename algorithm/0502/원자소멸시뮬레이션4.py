import sys
sys.stdin = open('원자소멸시뮬레이션.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def bfs():
    global result, N
    while queue:
        n = len(queue)
        for _ in range(n):
            k, d, r, c = queue.pop(0)
            visited[r][c] -= 1
            if visited[r][c] < 2:
                collision[r][c] = 0
            nr = r + dr[d]
            nc = c + dc[d]
            if not (4001 > nr >= 0 and 4001 > nc >= 0):
                continue
            visited[nr][nc] += 1
            if visited[nr][nc] > 1:
                collision[nr][nc] = 1
            queue.append((k, d, nr, nc))

        for i in reversed(range(len(queue))):
            k, d, r, c = queue[i]
            if collision[r][c]:
                result += k
                queue.pop(i)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [[0] * 4001 for _ in range(4001)]
    collision = [[0] * 4001 for _ in range(4001)]
    queue = []
    for i in range(N):
        c, r, d, k = map(int, input().split())
        r = 4000 - 2*(r + 1000)
        c = 2*(c + 1000)
        # 크기, 방향, r, c
        queue.append((k, d, r, c))
        visited[r][c] = 1
    result = 0
    bfs()
    print('#{} {}'.format(tc, result))
