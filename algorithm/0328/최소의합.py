def bf1(row, ret):
    global result1
    if ret >= result1:
        return
    if row == N:
        result1 = min(result1, ret)
        return
    else:
        for i in range(N):
            bf1(row + 1, ret + raw[row][i])


def bf2(row, ret):
    global result2
    if ret >= result2:
        return
    if row == N:
        result2 = min(result2, ret)
        return
    else:
        for i in range(N):
            if visited[i]:
                continue
            visited[i] = 1
            bf2(row + 1, ret + raw[row][i])
            visited[i] = 0


N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
result1 = float('inf')
result2 = float('inf')
bf1(0, 0)
bf2(0, 0)
print(result1)
print(result2)
