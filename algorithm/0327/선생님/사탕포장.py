import sys
sys.stdin = open("input.txt")

#main ----------------------------
N = int(input())
arr = list(map(int, input().split()))
sol =0
# 단순정렬 이용하여
for k in range(N-1):
    #K위치에서 2개씩만 정렬
    for i in range(k, k+2):
        for j in range(i+1, N):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    arr[k+1] += arr[k]#  K, K+1 번째 포장
    sol += arr[k+1] #  포장비용누계
# 삽입정렬 이용하여
arr.sort() # 정렬한 후 적용
for k in range(1, N):
    arr[k] += arr[k-1]#  K, K+1 번째 포장
    sol += arr[k] #  포장비용누계
    temp = arr[k]
    for i in range(k+1, N):
        if arr[i]< temp:# 크거나 같을때까지 교환
            arr[i], arr[i-1] = arr[i-1], arr[i]
        else: break

print(sol)
