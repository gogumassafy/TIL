import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    min_num = float("inf")
    max_num = -float("inf")
    input_list = list(map(int, input().split()))

    for i in input_list:
        if i > max_num:
            max_num = i
        elif i < min_num:
            min_num = i

    print(f"#{tc + 1} {max_num - min_num}")