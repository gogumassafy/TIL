# 개구리 행동
# 1. 점프
# 1.1. 오른쪽으로만 뜀
# 1.2. 두 번만 뜀
# 1.3 두 번째 거리 = 첫 점프 이상, 2배 이하

# 2. 시작
# 2.1. 어느 잎에서나 시작 가능


def binarysmallsearch(start, end, goal):
    mid = (start + end) // 2
    if start == end:
        return start
    else:
        if goal > leaves[mid]:
            return binarysmallsearch(mid + 1, end, goal)
        else:
            return binarysmallsearch(start, mid, goal)


def binarybigsearch(start, end, goal):
    mid = (start + end) // 2
    if start == end:
        return start
    else:
        if goal >= leaves[mid]:
            return binarybigsearch(mid + 1, end, goal)
        else:
            return binarybigsearch(start, mid, goal)


N = int(input())
leaves = [int(input()) for _ in range(N)]
leaves.sort()
count = 0
for i in range(len(leaves) - 2):
    for j in range(i + 1, len(leaves) - 1):
        first = leaves[j] - leaves[i]
        small = binarysmallsearch(j + 1, len(leaves), leaves[j] + first)
        big = binarybigsearch(j + 1, len(leaves), leaves[j] + 2*first)
        count += big - small
print(count)
