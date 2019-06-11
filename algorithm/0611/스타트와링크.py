def dfs():
    global N, result
    total = [0, 0]
    for i in range(N):
        for j in range(N):
            if team[i] == team[j]:
                total[team[i]] += raw[i][j]
    result = min(result, abs(total[0] - total[1]))


def perm(depth, n):
    global N
    half = N // 2
    if result == 0:
        return
    if depth == N:
        return
    if n == half:
        dfs()
        return
    team[depth] = 1
    perm(depth + 1, n + 1)
    team[depth] = 0
    perm(depth + 1, n)


N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
team = [0] * N
result = float('inf')
perm(0, 0)
print(result)

