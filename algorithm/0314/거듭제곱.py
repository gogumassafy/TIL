def myPow(n, m):
    if m == 1:
        return n
    return n * myPow(n, m - 1)


for tc in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, myPow(N, M)))
