import sys
sys.stdin = open('회전.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))

    M  %= N

    print(f'#{tc+1} {input_list[M]}')