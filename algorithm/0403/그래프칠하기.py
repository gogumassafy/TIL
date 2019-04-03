N, M = map(int, input().split())
color = []
for i in range(N):
    raw = list(map(int, input().split()))
    c = 1
    meet = []
    for j in range(i):
        if raw[j] and c == color[j]:
            c += 1
    if c > M:
        color.clear()
        break
    color.append(c)
if color:
    print(*color)
else:
    print(-1)
