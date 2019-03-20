import sys
sys.stdin = open('암호코드스캔.txt')


def check(r):
    first = raw[r].index(1)
    first_num = 1
    row_idx = 0
    col_idx = 0
    cnt = 0
    quotient = 0
    for i in range(first, len(raw[r])):
        if row_idx == 7 and col_idx == 3:
            num_count[row_idx][col_idx] = 7 * quotient - sum(num_count[row_idx])
            break
        if first_num == raw[r][i]:
            cnt += 1
        else:
            num_count[row_idx][col_idx] = cnt
            if first_num:
                first_num = 0
                cnt = 1
                col_idx += 1
            else:
                first_num = 1
                cnt = 1
                col_idx += 1
            if col_idx == 4:
                if not quotient:
                    quotient = sum(num_count[row_idx]) // 7
                row_idx += 1
                col_idx = 0
                first_num = 1

    col = 0
    for i in range(len(num_count)):
        col += sum(num_count[i])
    row = countrow(r, first)
    clear(r, first, row, col)

    if quotient:
        for i in range(len(num_count)):
            for j in range(4):
                num_count[i][j] //= quotient

    for i in range(len(num_count)):
        for j in range(len(pwd)):
            if num_count[i] == pwd[j]:
                num_count[i] = j
                break
        else:
            num_count[i] = -float('inf')


def countrow(r, c):
    count = 0
    while raw[r][c] != '0':
        count += 1
        r += 1
    return count


def clear(r, c, rowcount, colcount):
    global N, M
    for i in range(r, r+rowcount):
        if i >= N:
            break
        for j in range(c, c+colcount):
            if j >= M:
                break
            raw[i][j] = '0'


pwd = [
    [3, 2, 1, 1],
    [2, 2, 2, 1],
    [2, 1, 2, 2],
    [1, 4, 1, 1],
    [1, 1, 3, 2],
    [1, 2, 3, 1],
    [1, 1, 1, 4],
    [1, 3, 1, 2],
    [1, 2, 1, 3],
    [3, 1, 1, 2]
]

num = [
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

for i in range(10):
    pwd[i].reverse()

for i in range(16):
    num[i].reverse()

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    raw = [list(reversed(input())) for _ in range(N)]
    sum_nums = 0
    for i in range(len(raw)):
        temp = []
        for j in range(M):
            if raw[i][i].isalpha():
                idx = ord(raw[i][j]) - ord('A') + 10
            else:
                idx = int(raw[i][j])
            temp += num[idx]
        raw[i] = temp
    for i in range(len(raw)):
        num_count = [[0] * 4 for _ in range(8)]
        col = check(i)






    print('#{} {}'.format(tc, sum_nums))

#1 38
#2 0
#3 36
#4 36
#5 44
#6 80
#7 76
#8 72
#9 182
#10 166
#11 212
#12 192
#13 1164
#14 1196
#15 1272
#16 1584
#17 4378
#18 6908
#19 7736
#20 6604

