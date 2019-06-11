# def dfs(depth, total):
#     global N, result
#     for i in range(depth, N):
#         t, p = raw[i]
#         if i + t >= N:
#             result = max(result, total)
#             continue
#         dfs(depth + t, total + p)


def dfs(depth, day, total):
    global N, result
    if depth == N:
        result = max(result, total)
        return
    if depth + raw[depth][0] <= N and day <= depth:
        dfs(depth + 1, depth + raw[depth][0], total + raw[depth][1])
    dfs(depth + 1, day, total)


N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
result = 0
dfs(0, 0, 0)
print(result)
