def isWall(row, col):
    global N
    if row < 0 or row > N-1 or col < 0 or col > N - 1:
        return True
    elif snail[row][col]:
        return True
    return False


N = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
snail = [[0] * N for _ in range(N)]

cnt = 1
row = 0
col = 0
snail[row][col] = cnt
while cnt < N**2:
    for j in range(4):
        while not isWall(row + dr[j], col + dc[j]):
            row += dr[j]
            col += dc[j]
            cnt += 1
            snail[row][col] = cnt

for i in range(N):
    print(*snail[i])