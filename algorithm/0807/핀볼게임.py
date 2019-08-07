import sys
sys.stdin = open('핀볼게임.txt')

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

# 상좌하우
blocks = (
    (0, 0, 0, 0), (2, 0, 3, 1),
)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if raw[i][j]:
                continue

    print("#{} {}".format(tc, result))