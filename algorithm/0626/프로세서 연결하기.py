dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def runProcessor(pr, pc, d, depth):
    global N
    count = 0
    while 1:
        pr += dr[d]
        pc += dc[d]
        if not (N > pr >= 0 and N > pc >= 0):
            return count
        if raw[pr][pc]:
            return 0
        count += 1
        raw[pr][pc] = 10 + depth


def clearLine(pr, pc, d, depth):
    global N
    while 1:
        pr += dr[d]
        pc += dc[d]
        if not (N > pr >= 0 and N > pc >= 0):
            return
        if raw[pr][pc] != 10 + depth:
            return
        raw[pr][pc] = 0


def dfs(depth, total, K):
    global N, count, result, maxProcessor
    if depth == count:
        if K == maxProcessor:
            result = min(result, total)
        elif K > maxProcessor:
            maxProcessor = K
            result = total
        return
    r, c = processor[depth]
    for i in range(4):
        lineCount = runProcessor(r, c, i, depth)
        if lineCount:
            dfs(depth + 1, total + lineCount, K + 1)
        clearLine(r, c, i, depth)
    dfs(depth + 1, total, K)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    processor = []
    count = 0
    maxProcessor = 0
    result = float('inf')
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if raw[i][j]:
                processor.append((i, j))
                count += 1
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, result))
