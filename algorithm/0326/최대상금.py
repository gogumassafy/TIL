def perm(n, c):
    global result, change
    if visited[c][int("".join(num))]:
        return
    else:
        visited[c][int("".join(num))] = 1
    # if k == len(num) - 1:
    #     return
    if change == c:
        money = int("".join(num))
        if result < money:
            result = money
    else:
        for i in range(n - 1):
            for j in range(i + 1, n):
                num[i], num[j] = num[j], num[i]
                # perm(n, k, c + 1)
                perm(n, c+1)
                num[i], num[j] = num[j], num[i]
                # perm(n, k + 1, c)


T = int(input())
for tc in range(1, T + 1):
    num, change = input().split()
    change = int(change)
    num = list(num)
    visited = [[0] * 1000000 for _ in range(change + 1)]

    result = 0
    perm(len(num), 0)
    print('#{} {}'.format(tc, result))

#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645