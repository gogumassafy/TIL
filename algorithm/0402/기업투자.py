def comb(n, r, total, money):
    global M, result
    if M == money:
        result = max(result, total)
        return
    if n == r:
        return
    for i in range(M + 1):
        comb(n, r + 1, total + co[r][i], money + i)
    return


M, N = map(int, input().split())
co = [[0] for _ in range(N)]
for i in range(M):
    profit = list(map(int, input().split()))
    for j in range(N):
        co[j].append(profit[j + 1])
result = 0
comb(N, 0, 0, 0)
print(result)
