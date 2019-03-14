# 알고리즘북 6장 p.150
# 상 하 좌 우 대각선들
dr = [-1, 1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, -1, 1, 1, -1, 1, -1]

board = [
    ['U', 'R', 'L', 'P', 'M'],
    ['X', 'P', 'R', 'E', 'T'],
    ['G', 'I', 'A', 'E', 'T'],
    ['X', 'T', 'N', 'Z', 'Y'],
    ['X', 'O', 'Q', 'R', 'S']
]


def hasWord(r, c, word):
    if not (5 >= r >= 0 and 5 >= c >= 0):
        return False
    if board[r][c] != word[0]:
        return False
    if len(word) == 1:
        return True
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        ret = hasWord(nr, nc, word[1:])
        # 답을 찾았으면 더이상의 탐색은 필요없음.
        if ret:
            return ret
        # if hasWord(nr, nc, word[1:]):
        #     return True
    return False


for i in range(5):
    for j in range(5):
        sol = hasWord(i, j, 'ANQ')
        if sol:
            break
    else:
        continue
    break
print(sol)
