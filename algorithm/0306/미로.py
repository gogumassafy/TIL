# DFS 복습을 위한 미로
def findStartIdx():
    for i in range(1, N+1):
        for j in range(1, N+1):
            if map_info[i][j] == 2:
                return i, j


def DFS(row, col):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    map_info[row][col] = 2
    flag = 0
    for i in range(4):
        if not map_info[row+dr[i]][col+dc[i]]:
            flag = DFS(row+dr[i], col+dc[i])
            if flag:
                return flag
        elif map_info[row+dr[i]][col+dc[i]] == 3:
            return 1
    return flag


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map_info = [[1] * (N+2)] + [[1] + list(map(int, input())) + [1] for _ in range(N)] + [[1] * (N+2)]
    r, c = findStartIdx()
    sol = DFS(r, c)
    print('#{} {}'.format(tc, sol))
