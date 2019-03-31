N = int(input())
raw = []
for i in range(N):
    raw.append(tuple(map(int, input().split())))
raw.sort()
print(raw)
