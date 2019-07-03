def run():
    global result, N, raw
    idx = 0
    total = 0
    for i in range(N):
        waiting = []
        outCount = 0
        while outCount < 3:
            now = order[idx]
            score = raw[i][now]
            if score == 0:
                outCount += 1
            else:
                waiting = [i + score for i in waiting]
                waiting.append(score)
            idx = (idx + 1) % 9
        total += sum(1 for s in waiting if s > 3)
    result = max(total, result)


def ordering(depth):
    if depth == 9:
        run()
        return
    if depth == 3:
        order.append(0)
        ordering(depth + 1)
        order.pop()
    for i in range(1, 9):
        if select[i]:
            continue
        select[i] = 1
        order.append(i)
        ordering(depth + 1)
        order.pop()
        select[i] = 0


N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
select = [0] * 9
order = []
result = 0
ordering(0)
print(result)