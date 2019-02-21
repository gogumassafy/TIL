import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(T):
    N = int(input())
    input_num = map(int, input().split())

    max_num = -float("inf")
    min_num = float("inf")

    for i in input_num:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

    print(f'#{tc+1} {max_num-min_num}')
