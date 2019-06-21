dr = (-1, 0, 1, 0)
dc = (0, 1, -1, 0)

# 상우하좌
# 하우상좌

def clear(t):
    global R, C
    for i in range(R):
        for j in range(C):
            raw[t][i][j] = 0


def airclean(t, aircleaner):
    d = 0
    r, c = aircleaner[0]
    total = 0
    while 1:
        nr = r + dr[d]
        nc = c + dc[d]
        if raw[t][r][c] == -1:
            total += raw[t][nr][nc]
        else:
            raw[t][r][c] = raw[t][nr][nc]

        if raw[t][nr][nc]:




def bfs(q, t):
    global R, C
    next = (t + 1) % 2
    while q:
        r, c = q.pop(0)
        count = 0
        temp = []
        if raw[t][r][c] >= 5:
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (R > nr >= 0 and C > nc >= 0):
                    continue
                count += 1
                temp.append((nr, nc))
        each = raw[t][r][c] // 5
        raw[next][r][c] += raw[t][r][c] - each * count
        for nr, nc in temp:
            raw[next][nr][nc] += each



def init():
    global R, C, T
    aircleaner = []
    for i in range(2, R - 2):
        if raw[i][0] == -1:
            aircleaner.append((i, 0))

    for t in range(T):
        now = t % 2
        queue = []
        total = 0
        for i in range(R):
            for j in range(C):
                if raw[now][i][j] == -1 or raw[now][i][j] == 0:
                    continue
                queue.append((i, j))
        bfs(queue, now)
        airclean((now + 1) % 2)
        clear(now)


R, C, T = map(int, input().split())
raw = [[[0] * R for _ in range(C)] for _ in range(2)]
for i in range(R):
    raw[0][i] = list(map(int, input().split()))
init()
