def calc(r, c):
    global K
    for i in range(K + 1):
        if not N > r - i >= 0:
            continue
        for j in range(-(K - i), K - i + 1):
            if not N > c + j >= 0:
                continue
            visited[r - i][c + j] = 1
    for i in range(1, K + 1):
        if not N > r + i >= 0:
            continue
        for j in range(-(K - i), K - i + 1):
            if not N > c + j >= 0:
                continue
            visited[r + i][c + j] = 1


N = int(input())
K = int(input())
visited = [[0] * N for _ in range(N)]
calc(2, 2)
print(visited)
