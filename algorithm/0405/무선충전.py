dr = (0, -1, 0, 1, 0)
dc = (0, 0, 1, 0, -1)


def draw(idx, r, c, C, P):
    count = 0
    for i in range(r - C, r + C + 1):
        # 마름모 중간 이후
        if i >= r:
            for j in range(c - count, c + count + 1):
                if (10 > j >= 0) and (10 > i >= 0):
                    area[idx][i][j] = P
            count -= 1
        # 마름모 중간 이전
        else:
            for j in range(c - count, c + count + 1):
                if (10 > j >= 0) and (10 > i >= 0):
                    area[idx][i][j] = P
            count += 1


def calc(n, total):
    global user
    temp = 0
    if n == 2:
        return total
    r, c = user[n][0], user[n][1]
    for i in range(A):
        if check[i]:
            continue
        if area[i][r][c] == -1:
            continue
        check[i] = 1
        temp = max(temp, calc(n + 1, total + area[i][r][c]))
        check[i] = 0
    temp = max(temp, calc(n + 1, total))
    return temp


T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    userA = list(map(int, input().split()))
    userB = list(map(int, input().split()))
    area = [[[-1] * 10 for _ in range(10)] for _ in range(A)]
    for i in range(A):
        c, r, C, P = map(int, input().split())
        draw(i, r - 1, c - 1, C, P)

    check = [0] * A
    user = [[0, 0], [9, 9]]
    result = calc(0, 0)
    for i in range(M):
        user[0][0] += dr[userA[i]]
        user[0][1] += dc[userA[i]]
        user[1][0] += dr[userB[i]]
        user[1][1] += dc[userB[i]]
        result += calc(0, 0)
    print('#{} {}'.format(tc, result))

#1 1200
#2 3290
#3 16620
#4 40650
#5 52710