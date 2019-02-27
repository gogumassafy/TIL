import sys
sys.stdin = open("input.txt")

R, C = map(int, input().split())
arr = []
for i in range(R):
    arr.append(list(map(int, input().split())))

for i in range(R):
    for j in range(1, C):
        if arr[i][j]==1:
            arr[i][j] += arr[i][j-1]

for i in range(R):
    for j in range(C):
        print(arr[i][j], end=' ')
    print()
