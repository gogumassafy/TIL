N = int(input())
raw = list(map(int, input().split()))
for i in range(len(raw) - 1):
    min_idx = i
    for j in range(i + 1, len(raw)):
        if raw[min_idx] > raw[j]:
            min_idx = j
    raw[i], raw[min_idx] = raw[min_idx], raw[i]
print(*raw)