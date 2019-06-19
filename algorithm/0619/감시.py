# 상, 좌, 하, 우
cctv = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]


def dfs(N, depth, sum):
    global result
    if depth == N:
        result = min(result, sum)
        return
    for i in range(4):
        num = check()
        depth(N, depth + 1,sum - num)



def check():



N, M = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
count = 0
stack = []
for i in range(N):
    for j in range(M):
        if raw[i][j] == 0:
            count += 1
        if 6 > raw[i][j] > 0:
            stack.append((i, j))
result = count
dfs(len(stack), 0, count)
print(result)