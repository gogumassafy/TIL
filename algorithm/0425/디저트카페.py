import sys
sys.stdin = open('디저트카페.txt')

# 이동 경로
# 1. 맵을 벗어나면 안됨
# 2. 같은 종류의 디저트를 먹으면 안됨.
# 3. 왔던 길을 되돌아 가면 안됨.

# 0: 우하, 1: 좌하, 2: 좌상, 3: 우상
dr = (1, 1, -1, -1)
dc = (1, -1, -1, 1)


# 방향, 행, 열
def DFS(d, r, c, cafe, d1, d2):
    global N, result
    if d == 0 or d == 1:
        nr = r
        nc = c
        while 1:
            if d == 0:
                d1 += 1
            elif d == 1:
                d2 += 1
            nr += dr[d]
            nc += dc[d]
            if not (N > nr >= 0 and N > nc >= 0):
                return
            if raw[nr][nc] in cafe:
                return
            cafe += (raw[nr][nc],)
            DFS(d + 1, nr, nc, cafe, d1, d2)
    elif d == 2:
        for i in range(d1):
            r += dr[d]
            c += dc[d]
            if not (N > r >= 0 and N > c >= 0):
                return
            if raw[r][c] in cafe:
                return
            cafe += (raw[r][c],)
        DFS(d + 1, r, c, cafe, d1, d2)
    elif d == 3:
        if result // 2 > len(cafe) - 1:
            return
        for i in range(d2 - 1):
            r += dr[d]
            c += dc[d]
            if not (N > r >= 0 and N > c >= 0):
                return
            if raw[r][c] in cafe:
                return
            cafe += (raw[r][c],)
        DFS(d + 1, r, c, cafe, d1, d2)
    elif d == 4:
        result = max(len(cafe), result)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    for i in range(N - 2):
        for j in range(1, N - 1):
            # 방향 순서
            DFS(0, i, j, (raw[i][j],), 0, 0)
    print('#{} {}'.format(tc, result))


#1 6
#2 -1
#3 4
#4 4
#5 8
#6 6
#7 14
#8 12
#9 18
#10 30