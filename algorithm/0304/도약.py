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
        for k in range(j+1, N):
            third_distance = leaf[k] - leaf[j]
            if third_distance > 2*second_distance:
                break
            if second_distance > third_distance:
                continue
            cnt += 1
print(cnt)
