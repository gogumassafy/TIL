T = int(input())
for tc in range(1, T + 1):
    raw = list(map(int, input()))
    cnt = 0
    for i in range(len(raw)):
        if not raw.count(1):
            break
        if raw[i]:
            cnt += 1
            raw[i] = 0
            for j in range(i + 1, len(raw)):
                if raw[j]:
                    raw[j] = 0
                else:
                    raw[j] = 1

    print('#{} {}'.format(tc, cnt))