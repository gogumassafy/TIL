import sys
sys.stdin = open("미로.txt")

def find_way(stand_row, stand_col):
    for i in range(4):
        if maze[stand_row+row[i]][stand_col+col[i]] == "0":
            maze[stand_row + row[i]][stand_col + col[i]] = 1
            if find_way(stand_row+row[i], stand_col+col[i]):
                return 1
        elif maze[stand_row+row[i]][stand_col+col[i]] == "3":
            return 1
    return 0

T = int(input())

row = [1, -1, 0, 0]
col = [0, 0, 1, -1]


for tc in range(T):
    result = 0
    N = int(input())
    maze = [["1"] * (N+2)]
    maze += [list("1"+input()+"1") for _ in range(N)]
    maze += [["1"] * (N+2)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if maze[i][j] == "2":
                stand_row = i
                stand_col = j
    result = find_way(stand_row, stand_col)

    print(f'#{tc+1} {result}')