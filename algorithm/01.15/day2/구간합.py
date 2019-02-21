# 숫자카드.py

import sys
sys.stdin = open("구간합_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    min = 987654321
    max = -987654321
    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += arr[i+j]
        if sum > max : max = sum
        if sum < min : min = sum

    print("#{0} {1}".format(test_case, max - min))