T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    desk = []
    wait = [0] * N
    time = 0
    for _ in range(N):
        time = int(input())
        desk.append(time)
    while M:
        time = 0
        minIdx = 0
        minTime = float('inf')
        for i in range(N):
            each = wait[i] + desk[i]
            if minTime > each:
                minTime = each
                minIdx = i
        wait[minIdx] += desk[minIdx]
        M -= 1
        time += 1
        for i in range(N):
            if wait[i] < time:
                wait[i] = time
    print('#{} {}'.format(tc, max(wait)))
