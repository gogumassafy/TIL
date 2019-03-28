def comb(n, r, sumtime, length):
    global max_length, result
    if sumtime >= result:
        return
    if r < len(raw) and length + raw[r] > max_length:
        return
    if n == r:
        result = min(result, sumtime)
        return
    comb(n, r + 1, sumtime + time[r], 0)
    comb(n, r + 1, sumtime, length + raw[r])


max_length = int(input())
N = int(input())
raw = list(map(int, input().split()))
time = list(map(int, input().split())) + [0]
result = float('inf')
comb(len(raw), 0, 0, 0)
print(result)

