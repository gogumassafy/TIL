N = int(input())
input_list = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(N):
    row, col = map(int, input().split())

    for i in range(10):
        for j in range(10):
            if not input_list[row+i][col+j]:
                input_list[row+i][col+j] = 1

for i in range(100):
    for j in range(100):
        if input_list[i][j]:
            cnt += 1
print(cnt)