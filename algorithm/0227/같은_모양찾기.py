def matching(x, y, P):
    for i in range(P):
        for j in range(P):
            if pattern[i][j] != input_list[x + i][y + j]:
                return 0
    return 1

M = int(input())

input_list = [list(input()) for _ in range(M)]
P = int(input())
pattern = [list(input()) for _ in range(P)]
cnt = 0
for i in range(M - P + 1):
    for j in range(M - P + 1):
        cnt += matching(i, j, P)
print(cnt)
