import sys
sys.stdin = open('활주로건설.txt')

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        count = 1
        for j in range(1, N):
            if raw[i][j] == raw[i][j - 1]:
                count += 1
            elif raw[i][j - 1] == raw[i][j] + 1 and count >= 0:
                count = -X + 1
            elif raw[i][j - 1] + 1 == raw[i][j] and count >= X:
                count = 1
            else:
                break
        else:
            if count >= 0:
                result += 1

    for j in range(N):
        count = 1
        for i in range(1, N):
            if raw[i - 1][j] == raw[i][j]:
                count += 1
            elif raw[i - 1][j] == raw[i][j] + 1 and count >= 0:
                count = -X + 1
            elif raw[i - 1][j] + 1 == raw[i][j] and count >= X:
                count = 1
            else:
                break
        else:
            if count >= 0:
                result += 1
    print('#{} {}'.format(tc, result))


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