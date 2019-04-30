import sys, itertools
sys.stdin = open('점심식사시간.txt')


def calc():
    global result
    down = []
    time = 0
    while waiting[0] or waiting[1]:
        time += 1
        if down:
            pass
        if

    result = min(result, time)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    people = []
    stair = []
    cost = []
    for i in range(N):
        for j in range(N):
            if raw[i][j] == 1:
                people.append((i, j))
            elif raw[i][j]:
                stair.append((i, j))
                cost.append(raw[i][j])
    select = list(itertools.product([0, 1], repeat=len(people)))

    for s in select:
        waiting = [[], []]
        down = [[], []]
        for i in range(len(s)):
            waiting[s[i]].append(abs(people[i][0] - stair[s[i]][0]) + abs(people[i][1] - stair[s[i]][1]) + 1)
        waiting[0].sort()
        waiting[1].sort()
        calc()
    print('#{} {}'.format(tc, result))