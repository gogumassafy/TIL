import sys
sys.stdin = open('요리사.txt')


def dfs(n, k):
    global N
    if n == N // 2:
        calc()
        return
    for i in range(k, N):
        if visited[i]:
            continue
        visited[i] = 1
        A.append(i)
        dfs(n + 1, i + 1)
        A.pop()
        visited[i] = 0


def calc():
    global result, N
    taste = [0, 0]
    for i in range(N - 1):
        flag = visited[i]
        for j in range(i + 1, N):
            if flag == visited[j]:
                taste[flag] += raw[i][j] + raw[j][i]
    result = min(result, abs(taste[0] - taste[1]))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    A = []
    B = []
    result = float('inf')
    dfs(0, 0)
    print('#{} {}'.format(tc, result))
