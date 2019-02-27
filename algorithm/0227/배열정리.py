row, col = map(int, input().split())

input_list = [list(map(int, input().split())) for _ in range(row)]

for i in range(row):
    for j in range(col-1):
        if input_list[i][j] and input_list[i][j+1]:
            input_list[i][j+1] = input_list[i][j] + 1

for i in range(row):
    for j in range(col):
        print(input_list[i][j], end=" ")
    print()