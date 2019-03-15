T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input())) for _ in range(N)]
    mid = N // 2
    result = 0
    for row in range(mid + 1):
        for col in range(mid - row, mid + row + 1):
            result += raw[row][col]
    for row in range(1, N - mid):
        for col in range(row, N - row):
            result += raw[mid + row][col]
    print('#{} {}'.format(tc, result))