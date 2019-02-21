def find(data, k, n, m):
    data.insert(0,0)    #출발점 - 맨앞에 삽입
    data.append(n)      #종점 - 맨뒤에 추가
    last = 0            #마지막 충전기
    cnt = 0             #충전횟수
    for i in range(1, m + 2):
        if data[i] - data[i-1] > k :    #충전기 사이가 k보다 멀때
            return 0
        if data[i] > last + k:          #i충전기까지 갈 수 없으면
            last = data[i-1]
            cnt += 1
    return cnt

import sys
sys.stdin = open("전기버스_input.txt")

T = int(input())
for tc in range(T):
    # K : 한번 충전으로 이동할 수 있는 정류장 수
    # N : 정류장 수
    # M : 충전기 설치된 정류장 번호
    K, N, M = map(int, input().split())  #1 ≤ K, N, M ≤ 100
    data = list(map(int, input().split()))
    print("#{} {}".format(tc+1, find(data, K, N, M)))