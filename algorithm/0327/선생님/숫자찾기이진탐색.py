import sys
sys.stdin = open("input.txt")
def binSearch(s, e, data):
    while s<=e:
        m = (s+e)//2
        # data가 mid번째값이면 mid위치 + 1리턴
        if data == arr[m] : return m +1
        # data가 mid번째값보다 크면 오른쪽영역 재탐색
        elif data>arr[m] : s = m+1
        # data가 mid번째값보다 작으면 왼쪽영역 재탐색
        else : e = m-1
    return 0 # 못찾았으므로 0리턴

#main ----------------------------
N = int(input())
arr = list(map(int, input().split()))
T = int(input())
Tarr = list(map(int, input().split()))

for i in range(T):
    print(binSearch(0, N-1, Tarr[i]))

