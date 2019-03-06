N = int(input())
map_info = [[0]*(N+2)] + [[0] + list(map(int, input())) + [0] for _ in range(N)] + [[0]*(N+2)]
#   상 우상 우 우하 하 좌하 좌 좌상
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
cnt = 0
for i in range(N):
    for j in range(N):
        if map_info[i][j] == 1:
            for k in range(8):
                row = i
                col = j
                while 1:
                    if map_info[row+dr[k]][col+dc[k]] == 2:
                        row += dr[k]
                        col += dc[k]
                        map_info[row][col] = 9
                        cnt += 1
                    elif map_info[row+dr[k]][col+dc[k]] == 9:
                        row += dr[k]
                        col += dc[k]
                    else:
                        break
print(cnt)
