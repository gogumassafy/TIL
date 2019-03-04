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
leaf = []
cnt = 0

for _ in range(N):
    leaf.append(int(input()))
leaf.sort()

for i in range(len(leaf)):
    max_distance = ((leaf[-1] - leaf[i]) // 2) + 1
    for j in range(i+1, N):
        second_distance = leaf[j] - leaf[i]
        if second_distance > max_distance:
            break
        cnt += binary_search(j, N-1, leaf[j] + 2*second_distance+1) - binary_search(j, N-1, leaf[j] + second_distance)
print(cnt)
