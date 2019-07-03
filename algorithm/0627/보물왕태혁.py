T = int(input())
for tc in range(1, T + 1):
    P = int(input())
    raw = list(map(int, input().split()))
    maxNum = max(raw)
    for n in raw:
        result = maxNum * n
        for x in raw:
            q, r = divmod(result, x)
            if r or q not in raw:
                break
        else:
            break
    print("#{} {}".format(tc, result))
