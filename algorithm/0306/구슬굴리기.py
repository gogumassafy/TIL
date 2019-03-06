ROW, COL = map(int, input().split())
map_info = [[1]*(COL+2)] + [[1] + list(map(int, input())) + [1] for _ in range(ROW)] + [[1]*(COL+2)]
N = int(input())
direction_list = list(map(int, input().split()))

# 0 상 하 좌 우
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
point = 0
direction = direction_list[point]
for i in range(ROW):
    for j in range(COL):
        if map_info[i][j] == 2:
            r = i
            c = j
cnt = 1
while point < N:
    direction = direction_list[point]
    r += dr[direction]
    c += dc[direction]
    if map_info[r][c] == 1:
        r -= dr[direction]
        c -= dc[direction]
        point += 1
    elif map_info[r][c] == 0:
        cnt += 1
        map_info[r][c] = 2
print(cnt)