dr = (1, 0)
dc = (0, 1)


def dfs(r, c, total):
    global N
    if r == N - 1 and c == N - 1:
        calc(total)
        return
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (N > nr >= 0 and N > nc >= 0):
            continue
        if raw[nr][nc] == 0:
            continue
        dfs(nr, nc, total * raw[nr][nc])


def calc(number):
    global result
    cnt = 0
    number = reversed(str(number))
    # reversed(number)
    for i in number:
        if i != '0':
            break
        if cnt >= result:
            return
        cnt += 1
    result = min(result, cnt)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    dfs(0, 0, raw[0][0])
    print('#{} {}'.format(tc, result))
