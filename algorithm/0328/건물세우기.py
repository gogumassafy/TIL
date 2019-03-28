def bf(row, total):
    global N, sol
    if total >= sol:
        return
    if row == N:
        sol = min(sol, total)
        return
    else:
        for i in range(N):
            if visited[i]:
                continue
            visited[i] = 1
            bf(row + 1, total + raw[row][i])
            visited[i] = 0


N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
sol = float('inf')
bf(0, 0)
print(sol)
