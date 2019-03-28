import sys
sys.stdin = open("input.txt")

# def lowerSearch(s, e, data):
#     # data 이상중에서 가장 작은 값의 위치를 리턴\
#     sol= -1
#     while s<=e:
#         m = (s+e)//2
#         if arr[m] >= data : # 데이타 이상이면 왼쪽영역재탐색 (더작은값을 찾기위해)
#             sol=m
#             e = m-1
#         else : s = m+1 # 오른쪽 탐색
#     return sol
#
# def upperSearch(s, e, data):
#     # data 이하중에서 가장 큰 값의 위치를 리턴
#     sol = -1
#     while s <= e:
#         m = (s + e) // 2
#         if arr[m] <= data: # 데이타 이하이면 오른쪽영역 재탐색(더 큰값을 찾기위해)
#             sol = m
#             s = m+1
#         else:
#             e = m-1
#     return sol
#
# #main ---------------------------------------
# N = int(input())
# arr = []
# for i in range(N):
#     arr.append(int(input()))
# arr.sort()
# cnt = 0
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         start = arr[j] + (arr[j] - arr[i])
#         end = arr[j] + (arr[j] - arr[i])*2
#         lo = lowerSearch(j+1, N-1, start)
#         # 예외 경우 : 못찾았거나 2배이상 초과시 스킵
#         if lo==-1 or arr[lo]>end: continue
#         up = upperSearch(j+1, N-1, end)
#         cnt += (up-lo+1)
# print(cnt)


def upperSearch2(s, e, data):
    sol = -1
    while s <= e:
        m = (s + e) // 2
        # data 보다 작은값중에서 가장 큰 값의 위치 찾기
        # data 보다 작으면 오른쪽 영역 재탐색
        if arr[m] < data:
            s = m + 1
            sol = m
        # 아니면 (크거나 같으면 ) 왼쪽영역 재탐색
        else:
            e = m - 1
    return sol  # 못찾았으므로 -1리턴
# main ---------------------------------
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        start = arr[j] + (arr[j] - arr[i])
        end = arr[j] + (arr[j] - arr[i])*2
        cnt += upperSearch2(j, N-1, end+1) - upperSearch2(j, N-1, start)



print(cnt)
