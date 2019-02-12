# 4869

import sys
sys.stdin = open("종이붙이기_input.txt")

def fact(num):
    if num <= 1:
        return 1
    else:
        return num*fact(num-1)

T = int(input())

for tc in range(T):
    N = int(input())
    sum = 0

    numOfBig = int(N//20)
    if N%20:
        numOfsmall = 1
    else:
        numOfsmall = 0

    for i in range(numOfBig, -1, -1):
        sum += fact(numOfsmall + numOfBig) / fact(numOfsmall) / fact(numOfBig) * (2**numOfBig)
        numOfBig -= 1
        numOfsmall += 2

    print(f'#{tc+1} {int(sum)}')

