import sys
sys.stdin = open("특별한_정렬_input.text")

test_num = int(input())

for tc in range(test_num):
    N = int(input())
    input_list = list(map(int, input().split()))

    max_index = 0
    min_index = 0
    for i in range(N-1):
        if i % 2:
            min_index = i
            for j in range(i+1, N):
                if input_list[min_index] > input_list[j]:
                    min_index = j
            input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

        else:
            max_index = i
            for j in range(i+1, N):
                if input_list[max_index] < input_list[j]:
                    max_index = j
            input_list[i], input_list[max_index] = input_list[max_index], input_list[i]

    print(f"#{tc + 1} {' '.join(map(str, input_list[:10]))}")