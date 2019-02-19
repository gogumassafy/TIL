import sys

sys.stdin = open("magnetic.txt")

for tc in range(10):
    N = int(input())
    count = 0
    input_list = [[] for _ in range(100)]
    for i in range(100):
        input_list[i] = list(map(int, input().split()))

    for i in range(100):
        red_flag = 0
        for j in range(100):
            if input_list[j][i] == 1:
                red_flag = 1
            elif red_flag == 1 and input_list[j][i] == 2:
                count += 1
                red_flag = 0

    print(f'#{tc+1} {count}')