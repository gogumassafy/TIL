N = int(input())
map_info = [list(map(int, input())) for _ in range(N)]
cnt = 0
for row in range(1, N):
    for col in range(1, N):
        cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
        for i in range(row):
            for j in range(col):
                if map_info[i][j]:
                    cnt1 += 1
        for i in range(N - row):
            for j in range(col):
                if map_info[row + i][j]:
                    cnt2 += 1
        for i in range(row):
            for j in range(N - col):
                if map_info[i][col + j]:
                    cnt3 += 1
        for i in range(N - row):
            for j in range(N - col):
                if map_info[row + i][col + j]:
                    cnt4 += 1
        if cnt1 == cnt2 == cnt3 == cnt4:
            cnt += 1
if cnt:
    print(cnt)
else:
    print(-1)

