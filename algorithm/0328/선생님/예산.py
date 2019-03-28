import sys
sys.stdin = open("input.txt")

# 이진탐색 방법으로 ===========================
# def check(m):
#     # 상한액으로 지방에서 요청액을 배정가능하면 배정하고 아니면 상한액으로 합계 계산
#     tot =0
#     for i in range(N):
#         if arr[i]<=m : tot+=arr[i]
#         else: tot += m
#     # 합계가 총액 이하이면 성공 아니면 실패 리턴
#     if tot <=M : return 1
#     else: return 0
# #  main ----------------------------------
# N = int(input())
# arr = list(map(int, input().split()))
# M = int(input())
# e=max(arr)
# s=1
# sol=0
# while s<=e:
# # 1원에서 max원까지 상한가를  mid로 결정하여 총액이하이면 상한액을 늘리고 아니면 줄임
#     m=(s+e)//2
#     if check(m) : #성공하면 상한액을 늘리고
#         sol= m
#         s = m+1
#     else : # 초과하면 상한액을 줄임
#         e = m-1
# print(sol)


# 그리디 방법으로 ===================================

#  main ----------------------------------
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr.sort() # 오름차순 정렬
sol, tot = 0, 0
for i in range(N):
    if tot + arr[i]*(N-i) <=M: # 현재 예산액으로 배정 가능하면
        tot +=arr[i]
    else: #현재 예산액으로 배정 불가능
        sol = (M-tot)//(N-i)
        break
if sol : print(sol)
else : print(arr[N-1])














