def binarysearch(start, end, goal):
    mid = (start + end) // 2
    if start == end:
        return start
    else:
        if goal == raw[mid]:
            return mid
        elif goal >= raw[mid]:
            return binarysearch(start, mid, goal)
        else:
            return binarysearch(mid + 1, len(raw), goal)


N = int(input())
raw = list(map(int, input().split()))
M = int(input())
total = sum(raw)
if total <= M:
    print(max(raw))
else:
    raw.sort(reverse=True)
    money = 0
    while raw:
        avg = M // len(raw)
        idx = binarysearch(0, len(raw), avg)
        if idx == len(raw):
            money = avg
            break
        p = sum(raw[idx:])
        money = max(raw[idx:])
        M -= p
        del raw[idx:]
    print(money)
