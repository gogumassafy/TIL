def calc(selected):
    global result
    waiting = [[], []]
    for i in range(len(selected)):
        doorNumber = selected[i]
        hr, hc = human[i]
        dr, dc = door[doorNumber]
        time = abs(hr - dr) + abs(hc - dc) + 1
        waiting[doorNumber].append(time)
    start = 0
    stair = [[], []]

    while len(max(*stair)) + len(max(*waiting)):
        start += 1
        if start >= result:
            return
        for i in range(2):
            for s in reversed(range(len(stair[i]))):
                if start >= stair[i][s]:
                    stair[i].pop(s)
            for w in reversed(range(len(waiting[i]))):
                if len(stair[i]) < 3 and start >= waiting[i][w]:
                    time = max(waiting[i].pop(w), start)
                    dr, dc = door[i]
                    down = raw[dr][dc]
                    stair[i].append(start + down)
    result = min(result, start)


def selectDoor(M, depth):
    if depth == M:
        calc(doorSelected)
        return
    selectDoor(M, depth + 1)
    doorSelected[depth] = 1
    selectDoor(M, depth + 1)
    doorSelected[depth] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    human = []
    door = []
    result = float('inf')
    for i in range(N):
        for j in range(N):
            if raw[i][j] == 1:
                human.append((i, j))
            elif raw[i][j] >= 2:
                door.append((i, j))
    M = len(human)
    doorSelected = [0] * M
    selectDoor(M, 0)
    print('#{} {}'.format(tc, result))