N, M = map(int, input().split())
color = []
for i in range(N):
    raw = list(map(int, input().split()))
    c = 1
    meet = set()
    for j in range(i):
        if raw[j]:
            meet.add(color[j])
    meet = list(meet)
    meet.sort()
    for j in meet:
        if c == j:
            c += 1
        else:
            break
    if c > M:
        color.clear()
        break
    color.append(c)
if color:
    print(*color)
else:
    print(-1)
