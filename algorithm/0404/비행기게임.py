import sys
input = sys.stdin.readline

dr = [-1, -1, -1]
dc = [-1, 0, 1]


def dfs():
    global result
    while stack:
        bomb, life, score, r, c = stack.pop()
        if result >= score + sum(coin[0:r]) * 10:
            continue
        if r == 0:
            result = max(result, score)
        for i in range(3):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (13 > nr >= 0 and 5 > nc >= 0):
                continue
            if raw[nr][nc] == 'X' and life < 1:
                # 폭탄 사용
                if bomb == 1:
                    stack.append((0, 4, score, nr, nc))
                # 폭탄 미사용
                nscore = score - 7
                stack.append((bomb, life - 1, nscore, nr, nc))
            else:
                if raw[nr][nc] == '*':
                    nscore = score + 10
                else:
                    nscore = score
                stack.append((bomb, life - 1, nscore, nr, nc))


T = int(input())
for tc in range(1, T + 1):
    raw = [list(input().strip()) for _ in range(13)]
    data = [[[] * 5 for _ in range(13)] for _ in range(2)]
    for i in range(13):
        data[1][i] = raw[i][:]
    coin = [0] * 13
    for i in range(13):
        count = 0
        for j in range(5):
            if raw[i][j] == '*':
                count = 1
        coin[i] = count
    result = -float('inf')
    stack = []
    stack.append((1, 0, 0, 12, 2))
    dfs()
    print(result)

