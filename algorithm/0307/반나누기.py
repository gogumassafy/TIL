T = int(input())
for tc in range(1, T+1):
    N, K_min, K_max = map(int, input().split())
    input_list = list(map(int, input().split()))
    count_list = [0] * 101

    for i in input_list:
        count_list[i] += 1
    min_sum = float('inf')
    for i in range(1, len(count_list) - 1):
        for j in range(i+1, len(count_list)):
            C = sum(count_list[:i])
            B = sum(count_list[i:j])
            A = sum(count_list[j:])
            if not (K_max >= A >= K_min and K_max >= B >= K_min and K_max >= C >= K_min):
                continue
            each_sum = max(A, B, C) - min(A, B, C)
            if min_sum > each_sum:
                min_sum = each_sum
    if min_sum == float('inf'):
        print(-1)
    else:
        print(min_sum)