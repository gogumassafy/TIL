import sys
sys.stdin = open('숫자만들기.txt')

operator = "+-*/"


def dfs(n):
    global N
    if n == N - 1:
        # print(oprOrder)
        calc()
        return
    for i in range(4):
        if opr[i] == 0:
            continue
        opr[i] -= 1
        oprOrder.append(i)
        dfs(n + 1)
        oprOrder.pop()
        opr[i] += 1


def calc():
    global maxN, minN
    each = num[0]
    for i in range(N - 1):
        o = oprOrder[i]
        if o == 0:
            each += num[i + 1]
        elif o == 1:
            each -= num[i + 1]
        elif o == 2:
            each *= num[i + 1]
        else:
            q, r = divmod(each, num[i + 1])
            if q < 0 and r:
                q += 1
            each = q
    maxN = max(maxN, each)
    minN = min(minN, each)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    opr = list(map(int, input().split()))
    num = list(map(int, input().split()))
    maxN = -float('inf')
    minN = float('inf')
    oprOrder = []
    dfs(0)
    print('#{} {}'.format(tc, maxN - minN))
