import sys
sys.stdin = open('사칙연산유효성검사.txt')


def dfs(n):
    if n in child.keys():
        if numbers[n].isdigit():
            return False
        l = int(child[n][0])
        r = int(child[n][1])
        if not (dfs(l) and dfs(r)):
            return False
        return True
    elif numbers[n].isdigit():
        return True


for tc in range(1, 11):
    N = int(input())
    numbers = [0] * (N + 1)
    child = {}
    result = 1
    for i in range(N):
        raw = input().split()
        n = int(raw[0])
        v = raw[1]
        numbers[n] = v
        if len(raw) > 2:
            if len(raw) == 3:
                result = 0
            child[n] = raw[2:]

    if result:
        result = int(dfs(1))
    print('#{} {}'.format(tc, result))

#1 0
#2 0
#3 0
#4 1
#5 0
#6 1
#7 1
#8 0
#9 0
#10 0
