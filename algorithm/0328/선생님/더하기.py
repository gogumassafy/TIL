
import sys
sys.stdin = open("input.txt")

def DFS(no, nsum):
    global N, K, flag, arr, rec
    if nsum > K or nsum + rec[no] < K : return
    if nsum == K:
        flag = 1
        return

    if no>=N: return

    DFS(no+1, nsum + arr[no])
    if flag: return
    DFS(no+1, nsum)

# main ==================================

N, K = 0, 0
flag = 0
arr = tuple()
rec = [0] * 21
T = int(input())
for i in range(T):
    N , K = map(int, input().split())
    arr = tuple(map(int, input().split()))
    for i in range(N):
        rec[i]=0
        for j in range(i, N):
            rec[i] += arr[j]
    flag=0
    DFS(0, 0)
    if flag: print("YES")
    else: print("NO")