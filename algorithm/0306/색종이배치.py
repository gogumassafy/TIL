lr, lc, c, r = map(int, input().split())
lr2, lc2, c2, r2 = map(int, input().split())

map_info = [[0] * 102 for _ in range(102)]

for i in range(r+2):
    for j in range(c+2):
        if i == 0 or i == r+1 or j == 0 or j == c+1:
            map_info[lr+i-1][lc+j-1] = 1
        else:
            map_info[lr + i - 1][lc + j - 1] = 2

cnt1 = 0
cnt2 = 0
for i in range(r2):
    for j in range(c2):
        if map_info[lr2 + i][lc2 + j] == 1:
            cnt1 += 1
        elif map_info[lr2 + i][lc2 + j] == 2:
            cnt2 += 2
if cnt1 == 0:
    print(4)
elif cnt1 >= 1:
    if cnt2:
        print(3)
    elif cnt1 == 1:
        print(1)
    else:
        print(2)


