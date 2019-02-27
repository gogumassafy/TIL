def findtype(y, x, w, h):
    cnt = 0
    for i in range(w):
        for j in range(h):
            if matrix[y + j][x + i] == 3:
                print(3)
                return
            elif matrix[y + j][x + i] == 1:
                cnt += 1
    if cnt == 1:
        print(1)
        return
    elif cnt > 1:
        print(2)
        return
    print(4)
    return

y1, x1, width1, height1 = map(int, input().split())
y2, x2, width2, height2 = map(int, input().split())

matrix = [[0]*20 for _ in range(20)]

for i in range(width1):
    for j in range(height1):
        matrix[y1+j][x1+i] = 2

for i in range(width1+2):
    for j in range(height1+2):
        matrix[y1+j-1][x1+i-1] += 1

# 선생님 코드
# r, c, w, h = map(int,input().split())
# for i in range(r-1, r+h+1):
#     for j in range(c-1, c+w+1):
#         if i ==r-1 or i == r+h or j ==c-1 or j==c+w: # 가장자리는 2로
#             arr[i][j] = 2
#         else: # 사각형 내부는 1로
#             arr[i][j]=1

findtype(y2, x2, width2, height2)