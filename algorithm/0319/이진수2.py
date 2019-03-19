import sys
sys.stdin = open('이진수2.txt')

T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    binary = ''
    cnt = 0
    while N:
        cnt += 1
        if cnt >= 13:
            binary = 'overflow'
            break
        N *= 2
        temp = N // 1
        N -= temp
        binary += str(int(temp))
    print('#{} {}'.format(tc, binary))

