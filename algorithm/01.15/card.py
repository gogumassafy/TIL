import sys
sys.stdin = open("sample_input_card.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    case_input = input()
    max_count = -float("inf")
    index_num = 0
    count_num = [0] * 10

    for i in case_input:
        count_num[int(i)] += 1

    for i in range(10):
        if count_num[i] >= max_count and i > index_num:
            max_count = count_num[i]
            index_num = i

    print(f"#{tc+1} {index_num} {max_count}")

