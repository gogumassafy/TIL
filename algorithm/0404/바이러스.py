def dfs(v):
    global count
    for i in range(1, V + 1):
        if edge[v][i]:
            if not visited[i]:
                visited[i] = 1
                count += 1
                dfs(i)


V = int(input())
E = int(input())
edge = [[0] * (V + 1) for _ in range(V + 1)]
visited = [0] * (V + 1)
count = 0
for i in range(E):
    s, e = map(int, input().split())
    edge[s][e] = 1
    edge[e][s] = 1
visited[1] = 1
dfs(1)
print(count)
