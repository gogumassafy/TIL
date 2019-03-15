def cycle(value):
    first = raw.pop(0)
    first -= value
    if first < 0:
        first = 0
    raw.append(first)


for tc in range(10):
    n = int(input())
    raw = list(map(int, input().split()))
    while raw[-1]:
        for i in range(1, 6):
            cycle(i)
            if raw[-1] == 0:
                break
    print('#{} '.format(tc + 1), *raw)


