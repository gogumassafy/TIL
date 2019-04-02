import queue


def bfs():
    global M
    while not q.empty():
        n = q.get()
        if n == M:
            return visited[n] - 1
        for i in range(4):
            if i == 0:
                nr = n + 1
                if 0 <= nr <= 1000000 and not visited[nr]:
                    visited[nr] = visited[n] + 1
                    q.put(nr)
            elif i == 1:
                nr = n - 1
                if 0 <= nr <= 1000000 and not visited[nr]:
                    visited[nr] = visited[n] + 1
                    q.put(nr)
            elif i == 2:
                nr = n * 2
                if 0 <= nr <= 1000000 and not visited[nr]:
                    visited[nr] = visited[n] + 1
                    q.put(nr)
            else:
                nr = n - 10
                if 0 <= nr <= 1000000 and not visited[nr]:
                    visited[nr] = visited[n] + 1
                    q.put(nr)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    q = queue.Queue()
    visited[N] = 1
    q.put(N)
    print('#{} {}'.format(tc, bfs()))
