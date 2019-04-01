def comb(r, total, goal):
    global N, flag
    if flag:
        return
    if total == goal:
        flag = 1
        return
    if r == N:
        return
    comb(r + 1, total + raw1[r], goal)
    comb(r + 1, abs(total - raw1[r]), goal)
    comb(r + 1, total, goal)


N = int(input())
raw1 = list(map(int, input().split()))
M = int(input())
raw2 = list(map(int, input().split()))
result = ['N'] * M
for i in range(len(raw2)):
    flag = 0
    comb(0, 0, raw2[i])
    if flag:
        result[i] = 'Y'
print(*result)
