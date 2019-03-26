import sys
input = sys.stdin.readline

dr = [1, 0]
dc = [0, 1]


def bf(r, c, total):
    global result, N
    if total > result:
        return

    if r == N - 1 and c == N - 1:
        if total < result:
            result = total
            return

    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (N > nr >= 0 and N > nc >= 0):
            continue
        bf(nr, nc, total + raw[nr][nc])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    bf(0, 0, raw[0][0])
    print('#{} {}'.format(tc, result))