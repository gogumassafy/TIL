def DFS(node):
    visited[node] = 1
    stack.append(node)
    while stack:
        v = stack.pop()
        if v in info_dict:
            for i in info_dict[v]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = 1


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    info_dict = {}
    visited = [0] * (V + 1)
    stack = []
    for i in range(E):
        k, v = map(int, input().split())
        if k in info_dict:
            info_dict[k] += [v]
        else:
            info_dict[k] = [v]
    s, g = map(int, input().split())
    DFS(s)
    print('#{} {}'.format(tc, visited[g]))
