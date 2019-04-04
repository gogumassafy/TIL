def calc(start, floor):
    global N, result
    if start == N:
        result = max(result, floor)
        return
    for i in range(1, 4):
        if start + i > N:
            break
        if start != N - 1:
            if i == 1 and (1 in raw[start:start + i] or 3 in raw[start:start + i]):
                continue
        if raw[start:start + i].count(1) > 1 or raw[start:start + i].count(2) > 1 or raw[start:start + i].count(3) > 1:
            break
        calc(start + i, floor + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = list(map(int, input().split()))
    result = -1
    temp = []
    calc(0, 0)
    print(result)
