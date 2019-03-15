# 굉장히 단순한 BF
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     raw = list(map(int, input().split()))
#     maxArea = -float('inf')
#     for i in range(N):
#         for j in range(i + 1, N + 1):
#             area = (j - i) * min(raw[i:j])
#             if maxArea < area:
#                 maxArea = area
#     print(maxArea)

# 분할정복 알고리즘으로 풀기


def solve(start, end):
    if start == end:
        return raw[start]
    mid = (start + end) // 2
    ret = max(solve(start, mid), solve(mid + 1, end))

    lo = mid, hi = mid + 1
    height = min(raw[lo], raw[hi])
    ret = max(ret, height*2)
    while start < lo or hi < end:
        if




    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = list(map(int, input().split()))

