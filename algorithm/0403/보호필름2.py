import time
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
    global D, W, result
    if depth >= result:
        return
    if depth == D:
        result = min(result, D)
        return
    for i in range(D):
        if visited[i]:
            continue
        visited[i] = 1
        for j in range(2):
            data[i] = drug[j]
            if check():
                result = min(result, depth)
                visited[i] = 0
                data[i] = raw[i]
                return
            else:
                solve(depth + 1)
        visited[i] = 0
        data[i] = raw[i]


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(D)]
    data = raw[:]
    drug = [[0]*W, [1]*W]
    visited = [0] * D
    result = float('inf')
    if check() or K <= 1:
        result = 0
    else:
        solve(1)
    print('#{} {}'.format(tc, result))
print("--- %s seconds ---" %(time.time() - start_time))