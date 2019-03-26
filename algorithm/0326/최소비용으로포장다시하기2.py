import queue

N = int(input())
raw = list(map(int, input().split()))
sum_cost = 0
if N == 1:
    sum_cost = raw[0]
else:
    raw.sort(reverse=True)
    big = raw.pop()
    while raw:
        small = raw.pop()
        if big > raw[-1]:
            temp = raw.pop()
            raw.append(big)
            big = temp
            sum_cost += small + big
            small, big = min(small, big), max(small, big)
        else:
            sum_cost += small + big
            big += small

        sum_cost += small + temp

print(sum_cost)