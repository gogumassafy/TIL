N = int(input())
raw = list(map(int, input().split()))
min_cost = 0
if N == 1:
    min_cost = raw[0]
else:
    raw.sort()
    for i in range(1, len(raw)):
        raw[i] += sum(raw[:i])
print(raw[-1])