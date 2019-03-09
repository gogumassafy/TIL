ch, rh = map(int, input().split())
N = int(input())
sum_around = ch + rh
# 1북쪽 2남쪽 3서쪽 4동쪽
sum_distance = 0
distance = [0]*(N + 1)
for i in range(N + 1):
    n, d = map(int, input().split())
    info_table = [0, 2*(rh + ch) - d, rh + d, d, 2*rh + ch - d]
    distance[i] = info_table[n]
for i in range(N):
    each_distance = abs(distance[i] - distance[-1])
    if each_distance > sum_around:
        sum_distance += 2*sum_around - each_distance
    else:
        sum_distance += each_distance
print(sum_distance)
