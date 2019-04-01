import sys
sys.stdin = open('input.txt')


def dijkstra(s):
    global N, V, result
    D = [float('inf')] * N
    U = [s]
    for k, v in adjacent[s].items():
        D[k] = v
    while U != V:
        nsum = 0
        for i in D:
            if i != float('inf'):
                nsum += i
        if nsum > result:
            return
        difference = list(set(V) - set(U))
        w = difference[0]
        for i in difference:
            if D[w] > D[i]:
                w = i
        U.append(w)
        for k, v in adjacent[w].items():
            D[k] = min(D[k], D[w] + adjacent[w][k])
        U.sort()
    result = min(result, sum(D))


T = int(input())
for tc in range(1, T + 1):
    raw = list(reversed(list(map(int, input().split()))))
    N = raw.pop()
    V = list(range(N))
    adjacent = [{} for _ in range(N)]
    for i in range(0, N):
        for j in range(0, N):
            if raw[-1] or i == j:
                adjacent[i][j] = raw.pop()
            else:
                adjacent[i][j] = float('inf')
                raw.pop()
    result = float('inf')
    for i in range(N):
        dijkstra(i)
    print('#{} {}'.format(tc, result))
