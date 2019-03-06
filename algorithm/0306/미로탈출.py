def iswall(r, c):
    if r > N - 1 or r < 0 or c > N - 1 or c < 0:
        return True
    if maze[r][c] == 1:
        return True
    return False


N = int(input())
maze = [list(map(int, list(input()))) for _ in range(N)]
direction = list(map(int, input().split()))
# 하1 좌2 상3 우4
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

cnt = 0
row = 0
col = 0
maze[row][col] = 3
flag = 1
while flag:
    for i in direction:
        while not iswall(row+dr[i-1], col+dc[i-1]):
            row += dr[i-1]
            col += dc[i-1]
            if maze[row][col] == 3:
                flag = 0
                break
            maze[row][col] = 3
            cnt += 1
        if not flag:
            break
print(cnt)