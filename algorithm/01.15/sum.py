import sys
sys.stdin = open("sample_input_sum.txt")

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    list_num = list(map(int, input().split()))
    max_sum = -float("inf")
    min_sum = float("inf")

    for i in range(0, N+1 - M):
        each = 0 # 부분합을 받는 변수.
        for j in range(M):
            each += list_num[i+j] # i는 현재 인덱스, j는 부분합을 구성하는 부분들의 수.
        if each > max_sum: # 특정 부분합이 가장 크다면 새로운 부분합의 최대값이 된다.
            max_sum = each
        if each < min_sum: # 특정 부분합이 가장 작다면 새로운 부분합의 최소값이 된다.
            min_sum = each
    print(f"#{tc+1} {max_sum - min_sum}")