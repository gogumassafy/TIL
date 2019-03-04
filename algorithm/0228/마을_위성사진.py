N = int(input())
input_list = [[0]+list(map(int, list(input()))) + [0] for _ in range(N)]
input_list.insert(0, [0]*(N+2))
input_list.append([0]*(N+2))

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
max_height = 0

for n in range(1, N+1):
    for i in range(n, N+1-n):
        for j in range(n, N+1-n):
            min_height = float("inf")
            if input_list[i][j]:
                for k in range(4):
                    if not input_list[i + dr[k]][j + dc[k]]:
                        break
                    elif input_list[i + dr[k]][j + dc[k]] < min_height:
                        min_height = input_list[i + dr[k]][j + dc[k]]
                else:
                    input_list[i][j] = min_height + 1
            if input_list[i][j] > max_height:
                max_height = input_list[i][j]

print(max_height)