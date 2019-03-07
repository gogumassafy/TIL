N = int(input())
map_info = [list(map(int, input().split())) for _ in range(6)]
cnt = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

sum_depth = 0
for i in range(1, N-1):
    for j in range(1, N - 1):
        if map_info[i][j]:
            for cnt in range(1, N):
                for k in range(4):
                    if not map_info[i+dr[k]*cnt][j+dc[k]*cnt]:
                        break
                else:
                    continue
                break
            sum_depth += cnt
print(sum_depth)