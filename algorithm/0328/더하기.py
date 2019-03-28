def comb(n, total):
    global K, N, flag
    if total > K or flag:
        return
    if n == N:
        if total == K:
            flag = 1
        return
    else:
        comb(n + 1, total + raw[n])
        comb(n + 1, total)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    raw = list(map(int, input().split()))
    flag = 0
    comb(0, 0)
    print('YES' if flag else 'NO')
