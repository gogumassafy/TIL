import sys
sys.stdin = open('shuffle.txt')

def dfs(depth, d, card):
    global result, raw, N
    if depth == 6 or depth >= result:
        return
    if card == sorted(raw) or card == sorted(raw, reverse=True):
        result = min(result, depth)
        return
    left = card[:int(N/2)]
    right = card[int(N/2):]
    if d >= N/2:
        temp = right[:int((d + 1) - N/2)]
        right = right[int((d + 1) - N/2):]
    else:
        temp = left[:int(N/2 - (d + 1))]
        left = left[int(N/2 - (d + 1)):]
    while (left or right):
        if left:
            temp.append(left.pop(0))
        if right:
            temp.append(right.pop(0))
    for i in range(1, N):
        if d == 1 and i == 1:
            continue
        dfs(depth + 1, i, temp)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = list(map(int, input().split()))
    result = float('inf')
    for i in range(1, N):
        dfs(0, i, raw)
    if result == float('inf'):
        result = -1
    print("#{} {}".format(tc, result))
