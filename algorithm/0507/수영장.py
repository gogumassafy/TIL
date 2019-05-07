import sys
sys.stdin = open('수영장.txt')
# 1일, 1달, 3달, 1년


def dfs(n, total):
    global result
    if total >= result:
        return
    if n >= 12:
        result = min(result, total)
        return
    dfs(n + 1, total + plan[n]*fee[0])
    dfs(n + 1, total + fee[1])
    dfs(n + 3, total + fee[2])
    

T = int(input())
for tc in range(1, T + 1):
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    result = fee[-1]
    dfs(0, 0)
    print('#{} {}'.format(tc, result))