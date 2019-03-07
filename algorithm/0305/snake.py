def iswall(_row, _col):
    if _row < 0 or _row > N - 1 or _col < 0 or _col > N - 1:
        return True
    if worldMap[_row][_col] == 1:
        return True
    return False


N = int(input())
K = int(input())
worldMap = [[0] * N for _ in range(N)]
input_list = []

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
# idx가 양수 더해지면 L, 음수 더해지면 D

for i in range(K):
    r, c = map(int, input().split())
    worldMap[r-1][c-1] = 2

L = int(input())
for i in range(L):
    X, C = input().split()
    input_list += [[int(X), C]]


direction = 0
totalTime = 0
row = 0
col = 0
worldMap[row][col] = 1
snake = [[row, col]]
while not iswall(row + dr[direction], col + dc[direction]):
    totalTime += 1
    snake.append([row + dr[direction], col + dc[direction]])
    if not worldMap[row + dr[direction]][col + dc[direction]]:
        worldMap[snake[0][0]][snake[0][1]] = 0
        snake = snake[1:] # idx 에러?
    worldMap[row + dr[direction]][col + dc[direction]] = 1
    row += dr[direction]
    col += dc[direction]
    if input_list and totalTime == input_list[0][0]:
        if input_list[0][1] == "L":
            direction += 1
            if direction > 0:
                direction %= 4
        else:
            direction -= 1
            if direction < 0:
                direction %= -4
        input_list = input_list[1:]
print(totalTime+1)
