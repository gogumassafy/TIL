# 동 서 북 남
# 1, 2, 3, 4
dr = (0, 0, 0, -1, 1)
dc = (0, 1, -1, 0, 0)

# 주사위
dice = [0] * 7


N, M, r, c, K = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
opr = list(map(int, input().split()))

for i in range(K):
    nr = r + dr[opr[i]]
    nc = c + dc[opr[i]]
    if not (N > nr >= 0 and M > nc >= 0):
        continue
    if opr[i] == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif opr[i] == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif opr[i] == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif opr[i] == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    if raw[nr][nc] == 0:
        raw[nr][nc] = dice[6]
    else:
        dice[6] = raw[nr][nc]
        raw[nr][nc] = 0
    r = nr
    c = nc
    print(dice[1])

