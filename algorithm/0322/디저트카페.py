import sys
sys.stdin = open('디저트카페.txt')

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

# 시작 위치는 각 벽의 끝, 아래에서 2번째까지는 될 수 없다.
# 모서리로는 갈 수가 없다.

# 행, 열, 방향, 들린 카페의 리스트, 우하향, 좌하향
def dfs(row, col, direction, cafe, dis1, dis2):
    global result, N
    if direction == 4:
        result = max(result, len(cafe))
        return
    if direction < 2:
        while 1:
            if direction == 0:
                dis1 += 1
            if direction == 1:
                dis2 += 1
            row += dr[direction]
            col += dc[direction]
            if N > row >= 0 and N > col >= 0:
                if raw[row][col] in cafe:
                    return
                cafe += (raw[row][col],)
                dfs(row, col, direction + 1, cafe, dis1, dis2)
            else:
                return
    elif direction == 2:
        for i in range(1, dis1 + 1):
            row += dr[direction]
            col += dc[direction]
            if N > row >= 0 and N > col >= 0:
                if raw[row][col] in cafe:
                    return
                cafe += (raw[row][col],)
            else:
                return
        dfs(row, col, direction + 1, cafe, dis1, dis2)
    elif direction == 3:
        for i in range(1, dis2):
            row += dr[direction]
            col += dc[direction]
            if N > row >= 0 and N > col >= 0:
                if raw[row][col] in cafe:
                    return
                cafe += (raw[row][col],)
            else:
                return
        dfs(row, col, direction + 1, cafe, dis1, dis2)
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    for i in range(N - 2):
        for j in range(1, N - 1):
            dfs(i, j, 0, (raw[i][j],), 0, 0)
    print('#{} {}'.format(tc, result))
