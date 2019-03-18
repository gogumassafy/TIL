binary_num = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
]

pwd = [
    [0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1],
]

raw = list(input())
temp = []
for i in range(len(raw)):
    if raw[i].isalpha():
        idx = ord(raw[i]) - ord('A') + 10
    else:
        idx = int(raw[i])
    for j in binary_num[idx]:
        temp.append(j)

sol = []
cnt = 0
for i in range(len(temp) - 6):
    if cnt:
        cnt -= 1
        continue
    for j in range(9):
        flag = 1
        for k in range(6):
            if pwd[j][k] != temp[i + k]:
                flag = 0
                break
        if flag:
            cnt = 5
            sol.append(j)
            break
print(*sol)
