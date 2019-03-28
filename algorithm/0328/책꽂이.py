def comb(n, r, total):
    global result, B
    if B > total + sum(H[r:]):
        return
    if n == r:
        if B > total:
            return
        result = min(result, total)
        return
    visited[r] = 1
    comb(n, r + 1, total + H[r])
    visited[r] = 0
    comb(n, r + 1, total)


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = []
    for i in range(N):
        H.append(int(input()))
    H.sort(reverse=True)
    visited = [0] * len(H)
    result = float('inf')
    comb(len(H), 0, 0)
    print(result - B)
