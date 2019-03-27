def binarysmallsearch(start, end, goal):
    mid = (start + end) // 2
    if start == end:
        return start
    else:
        if goal > raw[mid]:
            return binarysmallsearch(mid + 1, end, goal)
        else:
            return binarysmallsearch(start, mid, goal)


def binarybigsearch(start, end, goal):
    mid = (start + end) // 2
    if start == end:
        return end
    else:
        if goal >= raw[mid]:
            return binarybigsearch(mid + 1, end, goal)
        else:
            return binarybigsearch(start, mid, goal)



def countnum(goal):
    smallidx = binarysmallsearch(0, len(raw), goal)
    bigidx = binarybigsearch(0, len(raw), goal)
    return bigidx - smallidx


N = int(input())
raw = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))
cnt = [0] * M
for i in range(len(num)):
    cnt[i] = countnum(num[i])
print(*cnt)
