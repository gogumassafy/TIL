def calcrow():
    total = 0
    for i in range(N):
        differ = 0
        count = 1
        for j in range(1, N):
            if raw[i][j] == raw[i][j - 1]:
                count += 1
                if differ:
                    if count >= X:
                        differ -= 1
                        count -= X
            elif abs(raw[i][j] - raw[i][j - 1]) == 1:
                # 땅이 솟은 경우
                if raw[i][j] > raw[i][j - 1]:
                    if count < X:
                        break
                    differ = 0
                    count = 1
                # 땅이 가라앉은 경우
                else:
                    if differ:
                        break
                    differ += 1
                    count = 1
            else:
                break
        else:
            if differ == 0:
                total += 1
    return total


def calccol():
    total = 0
    for j in range(N):
        differ = 0
        count = 1
        for i in range(1, N):
            if raw[i][j] == raw[i - 1][j]:
                count += 1
                if differ:
                    if count >= X:
                        differ -= 1
                        count -= X
            elif abs(raw[i][j] - raw[i - 1][j]) == 1:
                # 땅이 솟은 경우
                if raw[i][j] > raw[i - 1][j]:
                    if count < X:
                        break
                    differ = 0
                    count = 1
                # 땅이 가라앉은 경우
                else:
                    if differ:
                        break
                    differ += 1
                    count = 1
            else:
                break
        else:
            if differ == 0:
                total += 1
    return total


T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    print('#{} {}'.format(tc, calcrow() + calccol()))

#1 7
#2 4
#3 11
#4 11
#5 15
#6 4
#7 4
#8 1
#9 5
#10 8
