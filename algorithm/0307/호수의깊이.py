N = int(input())
map_info = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
sum_num = 0
for i in range(1, N - 1):
    for j in range(1, N - 1):
        if map_info[i][j]:
            for cnt in range(1, N):
                for direction in range(4):
                    if not map_info[i + dr[direction] * cnt][j + dc[direction] * cnt]:
                        map_info[i][j] = cnt
                        sum_num += cnt
                        break
                else:
                    continue
                break
print(sum_num)