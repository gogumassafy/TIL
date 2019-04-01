def acomb(n, r, atotal, btotal):
    global result
    if n == r:
        result = max(result, atotal + btotal)
        return
    if not visited[r] and (not a or a[-1] > raw[r]):
        visited[r] = 1
        a.append(raw[r])
        acomb(n, r + 1, atotal + raw[r], btotal)
        visited[r] = 0
        a.pop()
    if not visited[r] and (not b or b[-1] < raw[r]):
        visited[r] = 1
        b.append(raw[r])
        acomb(n, r + 1, atotal, btotal + raw[r])
        visited[r] = 0
        b.pop()
    acomb(n, r + 1, atotal, btotal)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = list(map(int, input().split()))
    result = 0
    visited = [0] * N
    a = []
    b = []
    acomb(N, 0, 0, 0)
    print(result)
