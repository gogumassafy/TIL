import sys
sys.stdin = open('원자소멸시뮬레이션.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def bfs():
    global result

    while queue:
        collision = []
        visited = []
        n = len(queue)
        for _ in range(n):
            r, c, d, k = queue.pop(0)
            if (r, c) in collision:
                result += k
                continue
            nr = r + dr[d]
            nc = c + dc[d]
            if not (4001 > nr >= 0 and 4001 > nc >= 0):
                continue
            if (nr, nc) not in visited:
                visited.append((nr, nc))
                queue.append((nr, nc, d, k))
                continue
            collision.append((nr, nc))
            result += k

        for i in reversed(range(len(queue))):
            r, c, d, k = queue[i]
            if (r, c) in collision:
                result += k
                queue.pop(i)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atom = []
    queue = []
    for i in range(N):
        c, r, d, k, = map(int, input().split())
        r = 4000 - (1000 + r)*2
        c = (1000 + c)*2
        queue.append((r, c, d, k))
        # queue.append(i)
    result = 0
    bfs()
    print('#{} {}'.format(tc, result))
