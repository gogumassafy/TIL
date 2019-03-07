def BFS(s):
    global G
    queue.append(s)
    visited[s] = 1
    while queue:
        v = queue.pop(0)
        for i in range(1, V+1):
            if D[v][i] == 1:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = visited[v] + 1

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    visited = [0] * (V+1)
    D = [[0] * (V+1) for _ in range(V+1)]
    queue = []
    for i in range(E):
        k, v = map(int, input().split())
        D[k][v] = 1
        D[v][k] = 1

    S, G = map(int, input().split())
    BFS(S)
    print('#{} {}'.format(tc+1, visited[G] - 1))