def isWall(i, j):
    if i+delta_row[k] < 0 or j+delta_col[k] < 0 or i+delta_row[k] > 99 or j+delta_col[k] > 99:
        return True
    else:
        return False

N = int(input())
input_list = [[0]*100 for _ in range(100)]
cnt = 0
delta_row = [1, -1, 0, 0]
delta_col = [0, 0, 1, -1]

for _ in range(N):
    row, col = map(int, input().split())

    for i in range(10):
        for j in range(10):
            if not input_list[row+i][col+j]:
                input_list[row+i][col+j] = 1

for i in range(100):
    for j in range(100):
        if input_list[i][j]:
            for k in range(4):
                if isWall(i, j) or not input_list[i+delta_row[k]][j+delta_col[k]]:
                    cnt += 1
print(cnt)

