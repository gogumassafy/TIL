import sys
sys.stdin = open('수영장.txt')


def calc(c, f):
    money = float('inf')
    if c == 12:
        return f

    for i in range(3):
        if i == 0:
            calculated[c] = 1
            f += plan[c] * fee[i]
            for j in range(c + 1, 13):
                if j == 12 or not calculated[j]:
                    money = min(calc(j, f), money)
                    break
            calculated[c] = 0
            f -= plan[c] * fee[i]
        elif i == 1:
            calculated[c] = 1
            f += fee[i]
            for j in range(c + 1, 13):
                if j == 12 or not calculated[j]:
                    money = min(calc(j, f), money)
                    break
            calculated[c] = 0
            f -= fee[i]
        else:
            temp = calculated[c:c + 3]
            calculated[c:c + 3] = [1] * len(temp)
            f += fee[i]
            for j in range(min(c + 3, 12), 13):
                if j == 12 or not calculated[j]:
                    money = min(calc(j, f), money)
                    break
            calculated[c:c + 3] = temp
            f -= fee[i]
    return money


T = int(input())
for tc in range(1, T + 1):
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    calculated = [0 if i else 1 for i in plan]
    for i in range(len(plan)):
        if plan[i]:
            result = min(calc(i, 0), fee[3])
            break
    print('#{} {}'.format(tc, result))
