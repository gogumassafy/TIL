import time, itertools
start_time = time.time()


def check():
    global D, W, K
    for col in range(W):
        flag = 0
        count = 1
        for row in range(D - 1):
            if D - row < K and count == 1:
                break
            if data[row][col] == data[row + 1][col]:
                count += 1
            else:
                count = 1
            if count == K:
                flag = 1
                break
        if not flag:
            return False
    return True


def solve(depth):
    global D, W, result, data
    if depth == D:
        result = min(result, D)
        return

    comb = list(itertools.combinations(idx, depth))
    perm = list(itertools.product([1, 0], repeat=depth))
    for c in comb:
        for p in perm:
            for i in range(depth):
                data[c[i]] = drug[p[i]]
            if check():
                result = min(result, depth)
                return
            data = raw[:]


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(D)]
    data = raw[:]
    drug = [[0]*W, [1]*W]
    idx = list(range(D))
    visited = [0] * D
    result = float('inf')
    if check() or K <= 1:
        result = 0
    else:
        for i in range(1, D + 1):
            if i >= result:
                break
            solve(i)
    print('#{} {}'.format(tc, result))
print("--- %s seconds ---" %(time.time() - start_time))