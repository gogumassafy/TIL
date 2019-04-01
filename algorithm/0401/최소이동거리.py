def dijkstra(s):
    global N
    U = [s]
    D = [float('inf')] * (N + 1)
    for k, v in adjacent[s].items():
        D[k] = v
    while U != V:
        w = 0
        for i in range(len(D)):
            if i not in U:
                if D[w] > D[i]:
                    w = i
        U.append(w)
        for k, v in adjacent[w].items():
            D[k] = min(D[k], D[w] + adjacent[w][k])
        U.sort()
    return D[-1]


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    V = list(range(N + 1))
    adjacent = [{} for _ in range(N + 1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        adjacent[s][e] = w
    print('#{} {}'.format(tc, dijkstra(0)))

