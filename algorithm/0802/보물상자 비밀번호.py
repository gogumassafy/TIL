T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    input_string = input()
    head = 0
    result = []
    each_part = len(input_string) // 4
    for s in range(each_part):
        for i in range(4):
            each_sum = 0
            for j in range(each_part):
                idx = s + i * each_part + j
                if idx >= N:
                    idx = idx - N
                temp = input_string[idx]
                if temp == 'A':
                    temp = 10
                elif temp == 'B':
                    temp = 11
                elif temp == 'C':
                    temp = 12
                elif temp == 'D':
                    temp = 13
                elif temp == 'E':
                    temp = 14
                elif temp == 'F':
                    temp = 15
                else:
                    temp = int(temp)
                each_sum += temp * 16**(each_part - 1 - j)
            result.append(each_sum)
    result = list(set(result))
    result.sort(reverse=True)
    print('#{} {}'.format(tc, result[K - 1]))
