T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight = sorted(list(map(int, input().split())), reverse=True)
    load = list(map(int, input().split()))
    result = 0
    for l in load:
        for w in range(len(weight)):
            if l >= weight[w]:
                result += weight[w]
                weight.pop(w)
                break
    print('#{} {}'.format(tc, result))