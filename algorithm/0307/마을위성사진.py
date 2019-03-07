N = int(input())
map_info = [list(map(int, input())) for _ in range(N)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

max_height = -float('inf')
for h in range(1, N+1):
    for i in range(1, N-1):
        for j in range(1, N-1):
            if map_info[i][j] == h:
                min_height = float('inf')
                for k in range(4):
                    neighbor = map_info[i+dr[k]][j+dc[k]]
                    if min_height > neighbor:
                        min_height = neighbor
                map_info[i][j] = min_height + 1
                if max_height < map_info[i][j]:
                    max_height = map_info[i][j]

print(max_height)
