# 우 상 좌 하
dr = (0, -1, 0, 1)
dc = (1, 0, -1, 0)


def dragonCurve(r, c, n, depth):
    if depth == n:
        return
    for i in reversed(range(len(stack))):
        r += dr[stack[i]]
        c += dc[stack[i]]
        raw[r][c] = 1
        newDir = (stack[i] + 1) % 4
        stack.append(newDir)
    dragonCurve(r, c, n, depth + 1)


N = int(input())
raw = [[0] * 101 for _ in range(101)]
result = 0
for i in range(N):
    c, r, d, g = map(int, input().split())
    stack = []
    raw[r][c] = 1
    r += dr[d]
    c += dc[d]
    raw[r][c] = 1
    stack.append((d + 1) % 4)
    dragonCurve(r, c, g, 0)

for i in range(100):
    for j in range(100):
        if raw[i][j] and raw[i][j + 1] and raw[i + 1][j] and raw[i + 1][j + 1]:
            result += 1
print(result)
