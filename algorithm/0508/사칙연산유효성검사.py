import sys
sys.stdin = open('사칙연산유효성검사.txt')

for tc in range(1, 11):
    N = int(input())
    numbers = [0] * (N + 1)
    result = 0
    for i in range(N):
        n, v, left, right = map(str, input().split())
        n = int(n)
        # left = int(left)
        # right = int(right)
        numbers[n] = v
    for i in

    print('#{} {}'.format(tc, result))
