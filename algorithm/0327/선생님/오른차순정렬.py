import sys
sys.stdin = open("input.txt")

def sort(s, e):
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def Qsort(s, e):
    if s>=e: return
    p, t = e, s
    for l in range(s, e):
        if arr[l]<arr[p]:
            arr[l], arr[t] = arr[t], arr[l]
            t+=1
    arr[p], arr[t] = arr[t], arr[p]
    Qsort(s, t-1)
    Qsort(t+1, e)

def Msort(s, e):
    if s>=e: return
    m=(s+e)//2
    Msort(s, m)
    Msort(m+1, e)
    l, r, t = s, m+1, s # 왼쪽시작, 오른쪽시작, 임시버퍼시작 위치
    while l<=m and r<=e:
        if arr[l]<arr[r]: # 왼쪽영역이 작으면 왼쪽영역값을 임시버퍼로
            temp[t] = arr[l]
            t+=1; l+=1
        else : # 오른쪽값을 임시버퍼로
            temp[t] = arr[r]
            t += 1; r += 1
    while l<=m: #왼쪽영역이 아직 남아있으면 나머지 임시버퍼로
        temp[t] = arr[l]
        t += 1; l += 1
    while r<=e: #오른쪽영역이 아직 남아있으면 나머지 임시버퍼로
        temp[t] = arr[r]
        t += 1; r += 1
    for i in range(s, e+1): arr[i] = temp[i] # 원본배열로 복사

# main -----------------------------------
N = int(input())
arr = list(map(int, input().split()))
temp = [0]*N
#sort(0, N-1)
#Qsort(0, N-1)
Msort(0, N-1)
for i in range(N): print(arr[i], end=' ')










