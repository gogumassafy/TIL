# 흑 1 백 2
def check(r, c, color):
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        cnt = 0
        flag = 0
        while table[nr][nc] and flag == 0:
            cnt += 1
            if table[nr][nc] == color:
                cnt -= 1
                flag = 1
                break
            elif table[nr][nc] == 0:
                cnt -= 1
                break
            nr += dr[i]
            nc += dc[i]
        if flag:
            for _ in range(cnt):
                nr -= dr[i]
                nc -= dc[i]
                if color == 1:
                    table[nr][nc] = 1
                else:
                    table[nr][nc] = 2


dr = [0, 1, 0, -1, 1, -1, 1, -1]
dc = [1, 0, -1, 0, 1, -1, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [[0]*(N+2) for _ in range(N+2)]
    stack = []
    for i in range(2):
        for j in range(2):
            if i == j:
                table[N//2 - i + 1][N//2 - j + 1] = 2
            else:
                table[N // 2 - i + 1][N // 2 - j + 1] = 1

    for i in range(M):
        row, col, color = map(int, input().split())
        table[row][col] = color
        check(row, col, color)

    white_sum = 0
    black_sum = 0
    for i in range(1, N + 1):
        white_sum += table[i].count(2)
        black_sum += table[i].count(1)
    print('#{} {} {}'.format(tc, black_sum, white_sum))
