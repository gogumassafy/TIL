import sys
sys.stdin = open('벌꿀채취.txt')


def dfs(n, honey, money, lst):
    global M, C
    if honey > C:
        return 0
    if n == M:
        return money
    return max(dfs(n + 1, honey, money, lst), dfs(n + 1, honey + lst[n], money + lst[n]**2, lst))


T = int(input())
for tc in range(1, T + 1):
    # 배열의 크기, 선택하는 통의 수, 최대 자원의 양
    N, M, C = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # dfs(0, 0, 0, raw[0][0:0 + M])
    for r1 in range(N):
        for c1 in range(N - M + 1):
            a = dfs(0, 0, 0, raw[r1][c1:c1 + M])
            for r2 in range(N):
                s = 0
                if r1 == r2:
                    s = c1 + M
                for c2 in range(s, N - M + 1):
                    b = dfs(0, 0, 0, raw[r2][c2:c2 + M])
                    result = max(result, a + b)
    print('#{} {}'.format(tc, result))
