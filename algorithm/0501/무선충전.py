import sys
sys.stdin = open('무선충전.txt')


dr = (0, -1, 0, 1, 0)
dc = (0, 0, 1, 0, -1)


def draw(idx, r, c, C, p):
    count = 0
    for i in range(r - C, r + C + 1):
        for j in range(c - count, c + count + 1):
            if not (10 > i >= 0):
                break
            if not (10 > j >= 0):
                continue
            data[idx][i][j] = p
        if i < r:
            count += 1
        else:
            count -= 1


def dfs(n, total):
    global A, each
    if n == 2:
        each = max(each, total)
        return
    for i in range(A):
        if selected[i] or data[i][people[n][0]][people[n][1]] == 0:
            continue
        selected[i] = 1
        dfs(n + 1, total + data[i][people[n][0]][people[n][1]])
        selected[i] = 0
    dfs(n + 1, total)


T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    direction = [list(map(int, input().split())) + [0] for _ in range(2)]
    data = [[[0] * 10 for _ in range(10)] for _ in range(A)]
    people = [[0, 0], [9, 9]]
    result = 0
    for i in range(A):
        c, r, C, p = map(int, input().split())
        draw(i, r - 1, c - 1, C, p)

    for i in range(M + 1):
        selected = [0] * A
        each = 0
        dfs(0, 0)
        result += each
        for j in range(2):
            people[j][0] += dr[direction[j][i]]
            people[j][1] += dc[direction[j][i]]
    print('#{} {}'.format(tc, result))
