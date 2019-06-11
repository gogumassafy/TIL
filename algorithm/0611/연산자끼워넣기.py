def dfs(depth, total):
    global N, minNum, maxNum
    if depth == N - 1:
        minNum = min(minNum, total)
        maxNum = max(maxNum, total)
    for i in range(4):
        if oper[i] == 0:
            continue
        oper[i] -= 1
        if i == 0:
            dfs(depth + 1, total + raw[depth + 1])
        elif i == 1:
            dfs(depth + 1, total - raw[depth + 1])
        elif i == 2:
            dfs(depth + 1, total * raw[depth + 1])
        elif i == 3:
            if total < 0:
                dfs(depth + 1, -(-total // raw[depth + 1]))
            else:
                dfs(depth + 1, total // raw[depth + 1])
        oper[i] += 1


N = int(input())
raw = list(map(int, input().split()))
# +, -, x, /
oper = list(map(int, input().split()))
minNum = float('inf')
maxNum = -float('inf')
dfs(0, raw[0])
print(maxNum)
print(minNum)
