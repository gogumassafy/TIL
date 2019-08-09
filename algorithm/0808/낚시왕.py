# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
# 상 하 우 좌
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, 1, -1)


def check(human):
    global result
    for r in range(1, R + 1):
        if raw[human % 2][r][human] == [0, 0, 0]:
            continue
        result += raw[human % 2][r][human][2]
        raw[human % 2][r][human] = [0, 0, 0]
        return


def move(time):
    oneTime = len(que)
    for i in range(oneTime):
        r, c = que.pop(0)
        if raw[time % 2][r][c] == [0, 0, 0]:
            continue
        s, d, z = raw[time % 2][r][c]
        raw[time % 2][r][c] = [0, 0, 0]
        nr = r
        nc = c
        for j in range(s):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (R + 1 > nr > 0 and C + 1 > nc > 0):
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 4
                elif d == 4:
                    d = 3
                nr = r + dr[d]
                nc = c + dc[d]
            r = nr
            c = nc
        if raw[(time + 1) % 2][nr][nc] != [0, 0, 0] and z < raw[(time + 1) % 2][nr][nc][2]:
            continue
        raw[(time + 1) % 2][nr][nc] = [s, d, z]

        que.append((nr, nc))


R, C, M = map(int, input().split())
rcsdz = [list(map(int, input().split())) for _ in range(M)]
raw = [[[[0, 0, 0] for _ in range(C + 1)] for _ in range(R + 1)] for _ in range(2)]
que = []
for i in range(len(rcsdz)):
    r, c, s, d, z = rcsdz[i]
    que.append((r, c))
    raw[1][r][c] = [s, d, z]
result = 0
for i in range(1, C + 1):
    check(i)
    move(i)
print(result)
