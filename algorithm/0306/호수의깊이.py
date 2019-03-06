N = int(input())
input_list = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
for i in range(1, N - 1):
    for j in range(1, N - 1):
        min_depth = float('inf')
        if input_list[i][j]:
            for cnt in range(1, N):
                for k in range(4):
                    if input_list[i+dr[k]*cnt][j+dc[k]*cnt] == 0:
                        break
                else:
                    continue
                break
            input_list[i][j] = cnt
total_num = 0
for i in range(N):
    total_num += sum(input_list[i])

print(total_num)