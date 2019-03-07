def binary_search(start, end, value):
    while start <= end:
        mid = (start + end) // 2
        if leaf[mid] < value:
            start = mid + 1
            result = start
        else:
            end = mid - 1
    return result


N = int(input())
leaf = [int(input()) for _ in range(N)]
leaf.sort()

cnt = 0
for i in range(N - 2):
    for j in range(i+1, N-1):
        first_jump = leaf[j] - leaf[i]
        min_leaf = binary_search(0, N-1, leaf[j] + first_jump)
        max_leaf = binary_search(0, N-1, leaf[j] + 2*first_jump)
        cnt += max_leaf - min_leaf

        #완전 탐색 코드
        # for k in range(j+1, N):
        #     second_jump = leaf[k] - leaf[j]
        #     if second_jump < first_jump:
        #         continue
        #     elif second_jump > 2*first_jump:
        #         break
        #     cnt += 1
print(cnt)