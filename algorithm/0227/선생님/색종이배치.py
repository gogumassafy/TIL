sr, sc, w, h = map(int, input().split())
arr = [[0]*100 for i in range(100)]

for i in range(sr-1, sr+h+1):
    for j in range(sc-1, sc+w+1):
        if i==sr-1 or i==sr+h or j==sc-1 or j==sc+w :
            arr[i][j]=2
        else:
            arr[i][j]=1

sr, sc, w, h = map(int, input().split())
cnt1=0
cnt2=0
for i in range(sr, sr+h):
    for j in range(sc, sc+w):
        if arr[i][j]==1:
            cnt1+=1
        elif arr[i][j]==2:
            cnt2+=1

if cnt1==0 and cnt2==1:
    sol=1
elif cnt1==0 and cnt2>1:
    sol=2
elif cnt1>0:
    sol=3
else:
    sol=4

print(sol)