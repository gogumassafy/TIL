import sys
sys.stdin = open("input.txt")
def DFS1( no, nsum): # 현재 행에서 모든 열을 사용하는 경우의 수
    global nmin
    if nsum > nmin: return  # 가지치기 : 합이 min을 초과시 리턴
    if no>=N:
        #for i in range(N): print(rec[i], end=' ')
        #print(nsum)
        if nsum<nmin: nmin =nsum
        return
    for i in range(N): # 열
        rec[no] = arr[no][i] # 고른 값을기록
        DFS1(no+1, nsum + arr[no][i])

def DFS2(no, nsum):
    global nmin
    if nsum > nmin: return  # 가지치기 : 합이 min을 초과시 리턴
    if no>=N:
        #for i in range(N): print(rec[i], end=' ')
        #print(nsum)
        if nsum<nmin: nmin =nsum
        return
    for i in range(N): # 열
        if chk[i]: continue
        chk[i]=1
        rec[no] = arr[no][i] # 고른 값을기록
        DFS2(no+1, nsum + arr[no][i])
        chk[i]=0

#main -----------------------------
N = int(input())
arr = []
rec = [0] * N # 고른 값을 기록배열(디버깅용)
chk = [0] * N # 열 체크배열
for i in range(N):
    arr.append(list(map(int, input().split())))
#첫번째 방법 : 열의 중복을 허용한 중복순열
nmin = 100000
DFS1(0, 0) # 0행부터 시작, 합계는 0
print(nmin)
#두번째 방법 : 열의 중복을 배제한 순열
nmin = 100000
DFS2(0, 0)
print(nmin)