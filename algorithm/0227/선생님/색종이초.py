
N = int(input())
arr = [[0]*100 for i in range(100)]

for k in range(N):
    r, c = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            arr[i][j]=1 #색종이 붙이기

# 도화지에서 면적구하기
sol=0
for i in range(100):
    for j in range(100):
        sol += arr[i][j]

print(sol)
# for i in range(30):
#     for j in range(30):
#         print(arr[i][j], end=' ')
#     print()
