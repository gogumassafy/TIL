def perm(n, k, total):
    global result
    if visited[5000][]
    if total >= result:
        return
    if n == k:
        result = min(result, total)
        return
    for i in range(n - 1):
        for j in range(i + 1, n):



            if len(per) > 1 and (so[per[-1]][0] > so[per[-2]][0] or so[per[-1]][0] > so[per[-2]][1]):
                perm(n, k + 1, total + 1)
            else:
                perm(n, k + 1, total)
            visited[i] = 0


N = int(input())
raw = list(map(int, input().split()))
so = []
for i in range(0, len(raw), 2):
    so.append((raw[i], raw[i+1]))
visited = [[0] * N for _ in range(N)]
result = float('inf')
per = []
perm(N, 0, 1)
print(result)
