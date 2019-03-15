def _insert(x, y, s):
    for i in range(y):
        raw.insert(x+i, s[i])


def _delete(x, y):
    for i in range(y):
        raw.pop(x + i)


def _append(y, s):
    for i in range(y):
        raw.append(s[i])


for tc in range(1, 11):
    N = int(input())
    raw = list(map(int, input().split()))
    M = int(input())
    opr = input().split()
    for i in range(M):
        first = opr.pop(0)
        if first == "I":
            idx = int(opr.pop(0))
            times = int(opr.pop(0))
            nums = []
            for j in range(times):
                nums.append(opr.pop(0))
            _insert(idx, times, nums)
        elif first == "D":
            idx = int(opr.pop(0))
            times = int(opr.pop(0))
            _delete(idx, times)
        else:
            times = int(opr.pop(0))
            nums = []
            for j in range(times):
                nums.append(opr.pop(0))
            _append(times, nums)
    print('#{} '.format(tc), *raw[:10])
