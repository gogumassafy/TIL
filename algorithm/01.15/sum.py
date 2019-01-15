import sys
sys.stdin = open("sample_input_sum.txt")

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    list_num = list(map(int, input().split()))
    max_sum = -float("inf")
    min_sum = float("inf")

    for i in range(0, N+1 - M):
        each = 0
        for j in range(M):
            each += list_num[i+j]
        if each > max_sum:
            max_sum = each
        if each < min_sum:
            min_sum = each
    print(f"#{tc+1} {max_sum - min_sum}")