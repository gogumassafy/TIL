dr = (-1, -1, -1, 0, 0, 1, 1, 1)
dc = (-1, 0, 1, -1, 1, -1, 0, 1)

H, W = map(int, input().split())
q = []
arr = [[] for _ in range(H)]

for r in range(H):
    temp = list(input())
    for c in range(W):
        if temp[c] == '.':
            temp[c] = 0
        else:
            temp[c] = int(temp[c])
    arr[r] = temp

life = [arr[r][:] for r in range(H)]

for r in range(H):
    for c in range(W):
        if arr[r][c] == 0:
            continue
        count = 0
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (H > nr >= 0 or W > nc >= 0):
                continue
            if arr[nr][nc] == 0:
                count += 1
        life[r][c] -= count
        if life[r][c] <= 0:
            q.append((r, c))

result = 0
while q:
    result += 1
    time = len(q)
    for _ in range(time):
        r, c = q.pop(0)z
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (H > nr >= 0 or W > nc >= 0):
                continue
            if life[nr][nc] <= 0:
                continue
            life[nr][nc] -= 1
            if life[nr][nc] <= 0:
                q.append((nr, nc))

print(result)