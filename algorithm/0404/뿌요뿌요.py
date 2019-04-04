import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def gravity():
    for c in range(6):
        for r in range(11, 0, -1):
            if raw[r][c] == '.':
                for r2 in range(r, -1, -1):
                    if raw[r2][c] != '.':
                        raw[r][c], raw[r2][c] = raw[r2][c], raw[r][c]
                        break
                else:
                    break


def dfs():
    global flag
    target = []
    cnt = 1
    while stack:
        r, c = stack.pop()
        target.append((r, c))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (12 > nr >= 0 and 6 > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            if raw[nr][nc] != raw[r][c]:
                continue
            visited[nr][nc] = 1
            cnt += 1
            stack.append((nr, nc))
    if cnt >= 4:
        boom(target)
        flag = 1
    target.clear()


def boom(t):
    for i in t:
        raw[i[0]][i[1]] = '.'


T = int(input())
for tc in range(1, T + 1):
    raw = [list(input().strip()) for _ in range(12)]
    stack = []
    count = 0
    flag = 1
    while flag:
        visited = [[0] * 6 for _ in range(12)]
        flag = 0
        for i in range(11, -1, -1):
            for j in range(6):
                if visited[i][j]:
                    continue
                if raw[i][j] != '.':
                    visited[i][j] = 1
                    stack.append((i, j))
                    dfs()
        gravity()
        if flag:
            count += 1
    print(count)
