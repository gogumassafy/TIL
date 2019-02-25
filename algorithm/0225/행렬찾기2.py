import sys
sys.stdin = open("행렬찾기.txt")

def countRow(i, j, col_cnt): # row, column, column_count
    global N
    row_cnt = 0
    # 몇 행인지 셈.
    for row in range(i, N):
        row_cnt += 1
        if row == (N - 1) or not input_list[row+1][j]:
            break
    # 행렬을 파악하고 해당 행렬을 제거하는 함수 호출
    clean(i, j, row_cnt, col_cnt)
    return row_cnt

# 행렬의 숫자를 전부 0으로 바꿈.
def clean(i, j, row_cnt, col_cnt):
    for row in range(i, i+row_cnt):
        for col in range(j-col_cnt+1, j+1):
            input_list[row][col] = 0
    return row_cnt

T = int(input())

for tc in range(T):
    N = int(input())
    input_list = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    matrix = []
    row_cnt = 0
    col_cnt = 0
    for i in range(N):
        for j in range(N):
            if input_list[i][j] != 0:
                col_cnt += 1
                if j == (N-1) or input_list[i][j+1] == 0:
                    row_cnt = countRow(i, j, col_cnt)
                    matrix.append([row_cnt*col_cnt, row_cnt, col_cnt])
                    cnt += 1
                    row_cnt = 0
                    col_cnt = 0

    matrix.sort()

    print(f'#{tc+1} {cnt}', end=" ")
    for i in range(cnt):
        for j in range(1, 3):
            print(matrix[i][j], end=" ")
    print()