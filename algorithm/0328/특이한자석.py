# 자석 회전
# 1. 방향
# 1.1. 1: 시계 방향, -1 반시계 방향
# 2. 이동
# 2.1. 이동하는 녀석과 붙어있는 부분의 극이 서로 다르다면 반대로 이동

# 자석
# 1. 자성
# 1.1. N: 0
# 1.2. S: 1
# 2. 순서
# 2.1. 빨간색 표시부분부터 시계방향으로 순서

import queue

dt = [-1, 1]


def check(index, direction):
    for j in range(2):
        ni = index + dt[j]
        if not (4 > ni >= 0):
            continue
        if raw[index][2 * dt[j]] == raw[ni][-2 * dt[j]]:
            continue
        if visited[ni]:
            continue
        visited[ni] = 1
        q.put((ni, -direction))
        check(ni, -direction)


def rotate():
    while not q.empty():
        i, d = q.get()
        if d == 1:
            raw[i] = [raw[i][7]] + raw[i][:7]
        else:
            raw[i] = raw[i][1:8] + [raw[i][0]]


T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    raw = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        visited = [0] * 4
        q = queue.Queue()
        gearidx, geardir = map(int, input().split())
        visited[gearidx - 1] = 1
        q.put((gearidx - 1, geardir))
        check(gearidx - 1, geardir)
        rotate()
    ret = 0
    for i in range(len(raw)):
        ret += raw[i][0] * 2**i
    print('#{} {}'.format(tc, ret))
