import sys
sys.stdin = open("수영장.txt")


def dfs(month, cost):
    global ans
    if month > 11:
        if ans > cost:
            ans = cost
        return
    if not plan[month]:
        dfs(month + 1, cost)
        return

    dfs(month + 1, cost + fee[0] * plan[month])
    dfs(month + 1, cost + fee[1])
    dfs(month + 3, cost + fee[2])
    dfs(month + 12, fee[3])


T = int(input())
for tc in range(1, T + 1):
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    ans = float('inf')
    dfs(0, 0)
    print('#{} {}'.format(tc, ans))
