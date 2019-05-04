import sys
sys.stdin = open('요리사.txt')


def dfs(n, k):
    global N
    if n == N:
        print(cook)
        # calc(cook)
        return
    for i in range(k, N):
        if visited[i]:
            continue
        visited[i] = 1
        cook.append(i)
        dfs(n + 1, k + 1)
        cook.pop()
        visited[i] = 0


def calc(cook):
    global result, N
    half = N // 2
    A = 0
    B = 0
    for i in range(half - 1):
        for j in range(i + 1, half):
            a = raw[cook[i]][cook[j]]
            b = raw[cook[j]][cook[i]]
            A += a + b
    for i in range(half, N - 1):
        for j in range(i + 1, N):
            a = raw[cook[i]][cook[j]]
            b = raw[cook[j]][cook[i]]
            B += a + b
    result = min(result, abs(A - B))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    cook = []
    result = float('inf')
    dfs(0, 0)
    print('#{} {}'.format(tc, result))
