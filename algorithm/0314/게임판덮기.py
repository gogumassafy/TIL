def check():
    global H, W
    for i in range(H):
        for j in range(W):
            if not board[i][j]:
                r = i
                c = j
                break
        else:
            continue
        break
    else:
        return 1

    cnt = 0
    for i in range(4):
        if mark(r, c, i, 1):
            cnt += check()
        mark(r, c, i, -1)
    return cnt


def mark(r, c, type, value):
    global H, W
    flag = 1
    for i in range(3):
        nr = r + d[type][i][0]
        nc = c + d[type][i][1]
        if not (H > nr >= 0 and W > nc >= 0):
            flag = 0
            continue
        elif (board[nr][nc] + value) > 1:
            flag = 0
        board[nr][nc] += value
    return flag


d = [
    [[0, 0], [1, 0], [1, 1]],
    [[0, 0], [0, 1], [1, 1]],
    [[0, 0], [1, 0], [0, 1]],
    [[0, 0], [1, 0], [1, -1]]
]

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if board[i][j] == '#':
                board[i][j] = 1
            else:
                board[i][j] = 0
    print(check())

