def findset(n):
    if n != p[n]:
        p[n] = findset(p[n])
    return p[n]


def union(a, b):
    if findset(a) <= findset(b):
        p[findset(b)] = findset(a)
    else:
        p[findset(a)] = findset(b)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    _pair = list(map(int, input().split()))
    pair = []
    for i in range(0, len(_pair), 2):
        pair.append((min(_pair[i], _pair[i + 1]), max(_pair[i], _pair[i + 1])))
    pair.sort()
    p = list(range(N + 1))
    for f, s in pair:
        union(f, s)
    # print(p)
    result = set()
    for i in p[1:]:
        result.add(findset(i))
    print('#{} {}'.format(tc, len(result)))

