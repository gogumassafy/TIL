ch, rh = map(int, input())
N = int(input())
# 1북 2남 3서 4동
info = [0, [rh - 1, 0], [0, 0], [rh - 1, 0], [rh - 1, ch - 1]]
for i in range(N):
    i, x = int(input())