N = int(input())
arr =[]
for i in range(N):
    arr.append(list(map(int, input())))

for h in range(N):#높이 0부터 시작
    flag=0
    for i in range(1,N-1):
        for j in range(1,N-1):
          if arr[i][j]>h:#높이보다 크면
              flag = 1
              if arr[i-1][j]>h and arr[i+1][j]>h and arr[i][j-1]>h and arr[i][j+1]>h:
                  arr[i][j]+=1

    if flag ==0: break
print(h)