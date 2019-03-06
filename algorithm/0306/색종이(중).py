N = int(input())
map_info = [[0] * 102 for _ in range(102)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for _ in range(N):
    row, col = map(int, input().split())
    for i in range(10):
        for j in range(10):
            map_info[row+i][col+j] = 1
cnt = 0
for i in range(1, 101):
    for j in range(1, 101):
        if map_info[i][j]:
            for k in range(4):
                if not map_info[i+dr[k]][j+dc[k]]:
                    cnt += 1
print(cnt)