
N = int(input())
arr = [[0]*102 for i in range(102)]

for k in range(N):
    r, c = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            arr[i][j]=1 #색종이 붙이기

# 도화지에서 둘레 계산하기
sol=0
for i in range(102):
    for j in range(102):
        if arr[i][j] ==1:
            if arr[i-1][j]==0: sol+=1 #상
            if arr[i+1][j] == 0: sol += 1  # 하
            if arr[i][j-1] == 0: sol += 1  # 좌
            if arr[i][j+1] == 0: sol += 1  # 우

print(sol)
# for i in range(30):
#     for j in range(30):
#         print(arr[i][j], end=' ')
#     print()
