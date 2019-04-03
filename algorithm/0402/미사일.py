def cpy(depth):
    for i in range(len(ships)):
        if depth == 0:
            temp[depth][i] = ships[i][:]
        else:
            temp[depth][i] = temp[depth - 1][i][:]


def boom(depth):
    global power, radius
    count = 0
    while stack:
        hp, r, c = stack.pop()
        if hp <= 0:
            count += 1
        for i in range(len(temp[depth])):
            if temp[depth][i][0] <= 0:
                continue
            nr = temp[depth][i][1]
            nc = temp[depth][i][2]
            dist = abs(nr - r) + abs(nc - c)
            if not (radius >= dist > 0):
                continue
            # 스택에서 꺼내는순간 피를 깎을것인가 고민
            temp[depth][i][0] -= power
            if temp[depth][i][0] <= 0:
                count += 1
    return count


def start(depth, total):
    global M, power, result
    if depth == M:
        result = max(result, total)
        return

    for i in range(len(ships)):
        cpy(depth)
        if temp[depth][i][0] <= 0:
            continue
        temp[depth][i][0] -= power
        stack.append(temp[depth][i])
        cnt = boom(depth)
        start(depth + 1, total + cnt)
    return


N = int(input())
ships = []
for i in range(N):
    c, r, hp = map(int, input().split())
    ships.append([hp, r, c])
M, power, radius = map(int, input().split())
temp = [[[] for _ in range(N)] for _ in range(M)]
stack = []
result = 0
start(0, 0)
print(N - result)
