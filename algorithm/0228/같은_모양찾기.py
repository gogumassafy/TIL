def matching(row, col, m):
    for i in range(m):
        for j in range(m):
            if input_list[row + i][col + j] != pattern[i][j]:
                return 0
    return 1


N = int(input())
input_list = [list(map(int, input())) for _ in range(N)]
M = int(input())
pattern = [list(map(int, input())) for _ in range(M)]
cnt = 0

# for i in range(N-M+1):
#     for j in range(N-M+1):
#         for k in range(4):
#             pattern = list(zip(*pattern[::-1]))
#             cnt += matching(i, j, M)
print(list(zip(*pattern)))
print(pattern)