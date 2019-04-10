import sys
sys.stdin = open('색종이.txt')


def dfs(depth):
    if depth == 0:
        return
    return -1


raw = [list(map(int, input().split())) for _ in range(10)]
data = [[] for _ in range(10)]
num_count = [5] * 6
for i in range(10):
    data[i] = raw[i][:]

count = 0
for i in range(10):
    for j in range(10):
        if raw[i][j]:
            count += 1
result = float('inf')
dfs(5)
print()
