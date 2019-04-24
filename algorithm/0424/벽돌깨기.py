import sys
sys.stdin = open('벽돌깨기.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DFS(depth, count):
    global result, W, H
    if depth == 0 or count == 0:
        result = min(result, count)
        return
    cpy(depth)
    for i in range(W):
        for j in range(H):
            if data[depth][j][i]:
                # 1. 벽돌을 깨고
                stack = [(data[depth][j][i], j, i)]
                data[depth - 1][j][i] = 0
                count -= boom(depth, stack)
                # 2. 다음 뎊스로 보낸다.
                DFS(depth - 1, count)
                break
        cpy(depth)


def cpy(depth):
    for i in range(H):
        data[depth - 1][i] = data[depth][i][:]


def boom(depth, stack):
    cnt = 1
    while stack:
        dist, r, c = stack.pop()
        for i in range(4):
            nr = r
            nc = c
            for j in range(1, dist):
                nr += dr[i]
                nc += dc[i]
                if not (H > nr >= 0 and W > nc >= 0):
                    break
                if data[depth - 1][nr][nc] == 0:
                    continue
                stack.append((data[depth - 1][nr][nc], nr, nc))
                data[depth - 1][nr][nc] = 0
                cnt += 1
    gravity(depth)
    return cnt


def gravity(depth):
    global W, H
    nw = []
    for i in range(W):
        for j in range(H - 1, -1, -1):
            if data[depth - 1][j][i]:
                nw.append(data[depth - 1][j][i])
        nw += [0] * (H - len(nw))
        for j in range(H):
            data[depth - 1][j][i] = nw.pop()


def init():
    global N
    for i in range(H):
        data[N][i] = raw[i][:]


T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(H)]
    result = 0
    for i in range(H):
        for j in range(W):
            if raw[i][j]:
                result += 1
    data = [[[] for _ in range(H)] for _ in range(N + 1)]
    init()
    DFS(N, result)
    print('#{} {}'.format(tc, result))