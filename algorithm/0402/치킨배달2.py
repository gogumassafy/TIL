def comb(n, k, r):
    global M, result
    if M == r:
        for i in range(len(h)):
            for j in range(M):
                dist[i][j] = abs(h[i][0] - selected[j][0]) + abs(h[i][1] - selected[j][1])
        temp = 0
        for i in range(len(dist)):
            temp += min(dist[i])
        result = min(result, temp)
        return
    if n == k:
        return
    selected.append(ch[k])
    comb(n, k + 1, r + 1)
    selected.pop()
    comb(n, k + 1, r)


N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
house = 0
h = []

chicken = 0
ch = []
selected = []
result = float('inf')
for i in range(N):
    for j in range(N):
        if raw[i][j] == 1:
            house += 1
            h.append((i, j))
        if raw[i][j] == 2:
            chicken += 1
            ch.append((i, j))
dist = [[0] * M for _ in range(house)]
comb(len(ch), 0, 0)
print(result)

# 조합으로 뽑아내고 bfs 할까 아니면 그냥 계산을 할까???
# 1. bfs
# 2. 계산
# 2.1. 계산을 정보 테이블 만들어서 그 값을 전부 계산해놓자
# 2.2. 그러기 위해서는 개별 카운트를 알고 있어야 한다.
# 2.3. 그런데 조합으로 먼저 뽑고 개별 거리를 계산해서 최소값을 다 더하는게 제일 간단할듯.

