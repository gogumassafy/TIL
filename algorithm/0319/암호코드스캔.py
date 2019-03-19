import sys
sys.stdin = open('암호코드스캔.txt')

# 각 암호코드 1자리는 2진법 숫자 7자리로 이루어져 있음.


def check(r, c):
    print()


def makeBinary(r):
    temp = ""
    for i in range(M):
        if raw[r][i].isalpha():
            
    print()


pwd = [
    [3, 2, 1, 1],
    [2, 2, 2, 1],
    [2, 1, 2, 2],
    [1, 4, 1, 1],
    [1, 1, 3, 2],
    [1, 2, 3, 1],
    [1, 1, 1, 4],
    [1, 3, 1, 2],
    [1, 2, 1, 3],
    [3, 1, 1, 2]
]

num = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
]

for i in range(10):
    pwd[i].reverse()

for i in range(16):
    num[i].reverse()

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    raw = [list(reversed(input())) for _ in range(M)]

    for i in range(N):
        for j in range(M):
            if raw[i][j] and not raw[i-1][j]:
                check(i, j)
            break


