import queue, time
start_time = time.time()


def bfs():
    global M
    while not q.empty():
        n = q.get()
        if n == M:
            return visited[n] - 1

        nr1 = n + 1
        if 0 <= nr1 <= 1000000 and not visited[nr1]:
            visited[nr1] = visited[n] + 1
            q.put(nr1)

        nr2 = n - 1
        if 0 <= nr2 <= 1000000 and not visited[nr2]:
            visited[nr2] = visited[n] + 1
            q.put(nr2)

        nr3 = n * 2
        if 0 <= nr3 <= 1000000 and not visited[nr3]:
            visited[nr3] = visited[n] + 1
            q.put(nr3)

        nr4 = n - 10
        if 0 <= nr4 <= 1000000 and not visited[nr4]:
            visited[nr4] = visited[n] + 1
            q.put(nr4)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    q = queue.Queue()
    visited[N] = 1
    q.put(N)
    print('#{} {}'.format(tc, bfs()))
print("--- %s seconds ---" %(time.time() - start_time))
