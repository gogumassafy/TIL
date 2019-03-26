def perm(n, k, total):
    global result
    if total >= result:
        return
    if n == k:
        total += raw[sunseo[-2]][sunseo[-1]]
        if result > total:
            result = total
            return
    else:
        for i in range(k, n):
            sunseo[i], sunseo[k] = sunseo[k], sunseo[i]
            perm(n, k+1, total + raw[sunseo[k - 1]][sunseo[k]])
            sunseo[i], sunseo[k] = sunseo[k], sunseo[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    sunseo = [i for i in range(N)] + [0]
    result = float('inf')
    perm(N, 1, 0)
    print('#{} {}'.format(tc, result))
