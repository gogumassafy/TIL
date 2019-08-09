import sys
sys.stdin = open('원자소멸시뮬레이션.txt')

global raw = [[[0, 0, 0] for _ in range(4000)] for _ in range(4000)]

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())


    result = 0
    print("#{} {}".format(tc, result))