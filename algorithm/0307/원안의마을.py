N = int(input())
map_info = [list(map(int, input())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if map_info[i][j] == 2:
            x2 = i
            y2 = j

max_d = 0
for i in range(N):
    for j in range(N):
        if map_info[i][j] == 1:
            d = ((x2 - i)**2 + (y2 - j)**2)
            if d > max_d:
                max_d = d

for i in range(1, 10):
    if i*i >= max_d:
        print(i)
        break