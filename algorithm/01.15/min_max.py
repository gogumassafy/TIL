import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    min_num = float("inf")
    max_num = -float("inf")
    input_list = list(map(int, input().split()))

    for i in input_list: #list에서 인덱스가 아닌 개별 객체를 받아온다.
        if i > max_num: # i가 최대값보다 크다면 최대값은 i가 된다.
            max_num = i
        elif i < min_num:
            min_num = i

    print(f"#{tc + 1} {max_num - min_num}")