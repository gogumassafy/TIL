def chess(row, N):
    cnt = 0
    if row == N:
        return 1
    for i in range(N):
        if not taken[i] and check(row, i):
            taken[i] = row + 1
            cnt += chess(row + 1, N)
            taken[i] = 0
    return cnt


def check(row, col):
    for i in range(N):
        if taken[i] and abs(row - (taken[i] - 1)) == abs(col - i):
            return False
    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    taken = [0] * N
    result = chess(0, N)
    print('#{} {}'.format(tc, result))
