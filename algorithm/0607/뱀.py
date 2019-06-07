# 왼 = -1, 오 = +1
dr = (1, 0, -1, 0)
dc = (0, -1, 0, 1)


N = int(input())
raw = [[0] * N for _ in range(N)]
K = int(input())
for i in range(K):
    r, c = map(int, input().split())
    raw[r - 1][c - 1] = 9
L = int(input())
dir = []
for i in range(L):
    a, b = input().split()
    dir.append((int(a), b))
raw[0][0] = 1
count = 0
sd = 3
sr = 0
sc = 0
snake = [(0, 0)]
while 1:
    if dir and dir[0][0] == count:
        time, d = dir.pop(0)
        if d == "D":
            sd = (sd + 1) % 4
        elif d == "L":
            sd = (sd - 1) % 4
    count += 1
    sr = sr + dr[sd]
    sc = sc + dc[sd]
    if not (N > sr >= 0 and N > sc >= 0):
        break
    if raw[sr][sc] == 1:
        break
    if raw[sr][sc] == 0:
        tr, tc = snake.pop(0)
        raw[tr][tc] = 0
    raw[sr][sc] = 1
    snake.append((sr, sc))

print(count)
