import sys
sys.stdin = open("input.txt")

# def lowerSearch(s, e, data):
#     sol = -1
#     while s<=e:
#         m = (s+e)//2
#         # data가 mid번째값이면 왼쪽영역 재탐색
#         if data == arr[m] :
#             sol = m
#             e = m-1
#         # data가 mid번째값보다 크면 오른쪽영역 재탐색
#         elif data>arr[m]: s = m+1
#         # data가 mid번째값보다 작으면 왼쪽영역 재탐색
#         else : e = m-1
#     return sol # 못찾았으므로 -1리턴
# def upperSearch(s, e, data):
#     sol=-1
#     while s<=e:
#         m = (s+e)//2
#         # data가 mid번째값이면 오른쪽영역 재탐색
#         if data == arr[m] :
#             sol = m
#             s = m+1
#         # data가 mid번째값보다 크면 오른쪽영역 재탐색
#         elif data>arr[m]: s = m+1
#         # data가 mid번째값보다 작으면 왼쪽영역 재탐색
#         else : e = m-1
#     return sol # 못찾았으므로 -1리턴
# # -------------------------------
# N = int(input())
# arr = list(map(int, input().split()))
# T = int(input())
# Tarr = list(map(int, input().split()))
# for i in range(T):
#     lo = lowerSearch(0, N-1, Tarr[i])
#     if lo>=0:
#         up = upperSearch(0, N-1, Tarr[i])
#         print( up-lo +1, end= ' ')
#     else : print(0, end=' ')





# upperSearch 함수 1개로만 구현

def upperSearch2(s, e, data):
    sol =-1
    while s<=e:
        m = (s+e)//2
        # data 보다 작은값중에서 가장 큰 값의 위치 찾기
        # data 보다 작으면 오른쪽 영역 재탐색
        if arr[m] < data :
            s = m+1; sol = m
        # 아니면 (크거나 같으면 ) 왼쪽영역 재탐색
        else : e = m -1
    return sol # 못찾았으므로 -1리턴

# main ---------------------------------
N = int(input())
arr = list(map(int, input().split()))
T = int(input())
Tarr = list(map(int, input().split()))
for i in range(T):
    print(upperSearch2(0, N-1, Tarr[i]+1) - upperSearch2(0, N-1, Tarr[i]))


