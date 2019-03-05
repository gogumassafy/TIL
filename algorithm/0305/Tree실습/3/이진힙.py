import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    input_list = [0] + list(map(int, input().split()))

    for i in range(1, len(input_list)):
        node = i
        while node > 1:
            if input_list[node] < input_list[node//2]:
                input_list[node], input_list[node//2] = input_list[node//2], input_list[node]
            node //= 2
    key = N
    sum_num = 0
    while key > 1:
        key //= 2
        sum_num += input_list[key]
    print('#{} {}'.format(tc, sum_num))