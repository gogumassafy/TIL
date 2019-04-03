# def cpy(depth):
#     for i in range(D):
#         data[depth][i] = data[depth - 1][i][:]


def check(depth):
    global D, W, K
    for col in range(W):
        flag = 0
        count = 1
        for row in range(D - 1):
            if raw[depth][row][col] == data[depth][row + 1][col]:
                count += 1
            else:
                count = 1
            if count == K:
                flag = 1
                break
        if not flag:
            return False
    return True


def solve(depth, drug):
    global D, W, result
    # if depth > result:
    #     return
    if depth > D:
        return
    # cpy(depth)
    for i in range(D):
        if visited[i]:
            continue
        visited[i] = 1
        # temp = data[depth][i][:]
        # data[depth][i] = [drug] * W
        temp = raw[i][:]
        raw[i] = [drug] * W
        if check(depth):
            result = min(result, depth)
            return
        else:
            solve(depth + 1, 0)
            solve(depth + 1, 1)
        visited[i] = 0
        raw[i] = temp


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(D)]
    # data = [[[] for _ in range(D)] for _ in range(D + 1)]
    visited = [0] * D
    # for i in range(D):
    #     data[0][i] = raw[i][:]
    result = float('inf')
    if check(0):
        result = 0
    else:
        solve(1, 0)
        solve(1, 1)

    print('#{} {}'.format(tc, result))

#1 2
#2 0
#3 4
#4 2 x
#5 2
#6 0
#7 3 x
#8 2
#9 3
#10 4 x