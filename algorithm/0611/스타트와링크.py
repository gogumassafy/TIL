def dfs():
    global N, result
    total =[0, 0]
    for i in range(N):
        for j in range(N):
            if team[i] == team[j]:
                total[team[i]] += raw[i][j]
    result = min(result, abs(total[0] - total[1]))


def perm(depth, n):
    global N
    half = N // 2
    if depth == N:
        if n == half:
            print(team)
        dfs()
        return
    team[depth] = 1
    perm(depth + 1, n + 1)
    team[depth] = 0
    perm(depth + 1, n)

    # for i in range(n, N):
    #     team[i] = 1
    #     perm(depth + 1, i + 1)
    #     team[i] = 0


N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
team = [0] * N
result = float('inf')
perm(0, 0)
print(result)

