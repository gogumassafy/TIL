def dfs(n, k, now, total):
    global result
    if total >= result:
        return
    if n == k:
        if raw[now][0] == 0:
            return
        total += raw[now][0]
        result = min(result, total)
        if result == 84:
            print(a)
        return
    for i in range(n):
        if raw[now][i] == 0:
            continue
        if visited[i]:
            continue
        visited[i] = 1
        a.append(i)
        dfs(n, k + 1, i, total + raw[now][i])
        a.pop()
        visited[i] = 0


N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
result = float('inf')
visited = [0] * N
visited[0] = 1
a = []
dfs(N, 1, 0, 0)
print(result)
