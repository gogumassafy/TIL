N, M, D = map(int, input().split())
dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    a, b, l = map(int, input().split())
    dist[a][b] = l
    dist[b][a] = l

for row in range(1, N + 1):
    for col in range(1, N + 1):
        if dist[row][col] != float('inf'):
            for i in range(1, N + 1):
                if dist[col][i] != float('inf') and row != i:
                    dist[row][i] = min(dist[row][i], dist[row][col] + dist[col][i])
                    dist[i][row] = dist[row][i]

result = 0

for i in range(1, N + 1):
    count = 1
    for j in range(1, N + 1):
        if dist[i][j] < D:
            count += 1
    result = max(result, count)
print(result)
