def perm(n, k, c):
    global result, change
    if visit[c][k][int("".join(num))]:
        return
    else:
        visit[c][k][int("".join(num))] = 1
    if k == len(num) - 1:
        return
    if change == c:
        money = int("".join(num))
        if result < money:
            result = money
    else:
        for i in range(1, n):
            num[i], num[k] = num[k], num[i]
            perm(n, k, c + 1)
            perm(n, k + 1, c+1)
            num[i], num[k] = num[k], num[i]
            perm(n, k + 1, c)


T = int(input())
for tc in range(1, T + 1):
    num, change = input().split()
    change = int(change)
    num = list(num)
    visit = [[[0] * 1000000 for _ in range(len(num))] for _ in range(change + 1)]
    result = 0
    perm(len(num), 0, 0)
    print('#{} {}'.format(tc, result))
