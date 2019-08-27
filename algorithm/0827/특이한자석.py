import sys
sys.stdin = open('특이한자석.txt')


def dfs(i, d):
    visited[i] = 1
    if (i > 0):
        if gear[i][6] != gear[i - 1][2] and visited[i - 1] == 0:
            dfs(i - 1, -d)
    if (i < 3):
        if gear[i][2] != gear[i + 1][6] and visited[i + 1] == 0:
            dfs(i + 1, -d)

    if d == 1:
        gear[i] = [gear[i][-1]] + gear[i][:-1]
    else:
        gear[i] = gear[i][1:] + [gear[i][0]]


T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    gear = []
    result = 0
    for i in range(4):
        gear.append(list(map(int, input().split())))
    for i in range(K):
        visited = [0] * 4
        idx, d = map(int, input().split())
        dfs(idx - 1, d)
    result = gear[0][0] + gear[1][0] * 2 + gear[2][0] * 4 + gear[3][0] * 8
    print("#{} {}".format(tc, result))
