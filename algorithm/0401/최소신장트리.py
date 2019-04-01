import queue

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    visited = [0] * (V + 1)
    dist = [[] for _ in range(V+1)]
    q = queue.PriorityQueue()
    q.put((0, 0))
    for i in range(E):
        f, t, v = map(int, input().split())
        dist[f].append((t, v))
        dist[t].append((f, v))
    # print(dist)
    nsum = 0
    while not q.empty():
        value, to = q.get()
        if visited[to]:
            continue
        visited[to] = 1
        nsum += value
        for i in dist[to]:
            q.put((i[1], i[0]))

    print('#{} {}'.format(tc, nsum))
