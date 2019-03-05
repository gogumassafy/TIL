N = int(input())
square = [list(map(int, input().split())) for _ in range(N)]

while 1:
    angle = int(input()) // 90
    if not angle:
        break
    for i in range(angle):
        square = [list(reversed(x)) for x in zip(*square)]
    for i in range(N):
        print(*square[i])