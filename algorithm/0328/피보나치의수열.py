def fibo(N):
    if visited[N]:
        return visited[N]
    else:
        if N <= 2:
            visited[N] = 1
        else:
            visited[N] = fibo(N - 1) + fibo(N - 2)
    return visited[N]


N = int(input())
visited = [0] * (N + 1)
print(fibo(N))
