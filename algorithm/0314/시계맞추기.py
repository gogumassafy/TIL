linked = [
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],

        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],

        [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],

        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],

        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],

        [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],

        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
]


def areDone():
    flag = 1
    for i in range(16):
        if raw[i] != 12:
            flag = 0
            return flag
    return flag


def push(swtch):
    for i in range(16):
        if linked[swtch][i]:
            raw[i] += 3
            if raw[i] == 15:
                raw[i] = 3


def solve(swtch):
    if swtch == 10:
        return 0 if areDone() else 999
    result = float('inf')
    for cnt in range(4):
        result = min(result, cnt + solve(swtch + 1))
        push(swtch)
    return result


T = int(input())
for tc in range(1, T+1):
    raw = list(map(int, input().split()))
    print(solve(0))