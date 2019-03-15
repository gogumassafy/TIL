def DFS(idx):
    ret = 1
    for i in range(1, N + 1):
        if edge[idx][i] and not visited[i]:
            visited[i] = visited[idx] + 1
            ret = max(DFS(i), ret)
            visited[i] = 0
    return max(ret, visited[idx])


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    node = list(range(1, N + 1))
    edge = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    result = 1
    for i in range(M):
        s, e = map(int, input().split())
        edge[s][e] = 1
        edge[e][s] = 1
    for i in range(1, N + 1):
        visited[i] = 1
        length = DFS(i)
        visited[i] = 0
        result = max(result, length)
    print('#{} {}'.format(tc, result))

