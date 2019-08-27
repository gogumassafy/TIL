def dfs(v):
    stack = [v]
    while stack:
        now = stack.pop()
        for next in connect[now]:
            if visited[next]:
                continue
            visited[next] = 1
            stack.append(next)
    return


N, M = map(int, input().split())

connect = [[] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 0
for i in range(M):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)

for i in range(1, N + 1):
    if visited[i]:
        continue
    visited[i] = 1
    count += 1
    dfs(i)

print(count)
