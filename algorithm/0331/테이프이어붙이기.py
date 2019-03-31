def comb(n, r, nsum):
    global result
    if nsum < 0:
        return
    if n == length:
        result = min(result, nsum)
        return
    if N == r:
        return
    comb(n + 1, r + 1, nsum - 2*raw[r])
    comb(n, r + 1, nsum)


N = int(input())
raw = list(map(int, input().split()))
total = sum(raw)
length = N // 2
result = total + 1
comb(0, 0, total)
print(result)
