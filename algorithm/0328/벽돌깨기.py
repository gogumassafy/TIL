def bfs():
    return


def bomb():
    return


def gravity():
    return


def perm(n, k):
    global W
    if k == n:
        print(target)
        return
    for i in range(W):
        if not raw[H - 1][i]:
            continue
        target[k] = i
        perm(n, k + 1)
        target[k] = 0


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(H)]
    result = 0
    target = [0] * N
    perm(N, 0)

    print('#{} {}'.format(tc, result))