def solve(selected):
    global result
    total = 0
    for i in range(len(house)):
        each = float('inf')
        for j in selected:
            each = min(each, calculated[i][j])
        total += each
    result = min(result, total)


def calculate(k, depth):
    global M
    if depth == M:
        solve(selected)
        return
    for i in range(k, len(store)):
        selected.append(i)
        calculate(i + 1, depth + 1)
        selected.pop()


N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
store = []
house = []
selected = []
result = float('inf')
for i in range(N):
    for j in range(N):
        if raw[i][j] == 1:
            house.append((i, j))
        if raw[i][j] == 2:
            store.append((i, j))
calculated = [[float('inf')] * len(store) for _ in range(len(house))]
for i in range(len(house)):
    for j in range(len(store)):
        calculated[i][j] = abs(store[j][0] - house[i][0]) + abs(store[j][1] - house[i][1])
calculate(0, 0)
print(result)
