def binarysearch(start, end):
    global M
    sol = 0
    while start <= end:
        mid = (start + end) // 2
        ret = calc(mid)
        if ret == M:
            return mid
        # 계산값이 M보다 더 크다면 톱을 높여야 함.
        elif ret >= M:
            start = mid + 1
        else:
            end = mid - 1
            sol = end
    return sol


def calc(num):
    sum_num = 0
    for i in raw:
        if i > num:
            sum_num += i - num
    return sum_num


N, M = map(int, input().split())
raw = list(map(int, input().split()))
print(binarysearch(min(raw), max(raw)))
