import sys

sys.stdin = open("sample_input_bus.txt")

T = int(input())

for tc in range(T):
    count = 0
    location = 0
    K, N, M = map(int, input().split())  # 각각 보폭, 도착지점의 좌표, 쉬어갈 수 있는 장소의 수
    list_M = list(map(int, input().split()))  # 쉬어갈 수 있는 장소의 좌표

    for i in range(M-1):  # 쉬어갈 수 있는 모든 장소의 좌표를 고려한다.
        if list_M[i] <= (K + location) and list_M[i + 1] > (K + location):
            location = list_M[i]
            count += 1
        elif list_M[i] > (K + location) and list_M[i + 1] > (K + location): # 다음 쉼터에서 쉴 수 없는 경우
            count = 0
            break

    # 결과 판단 부분
    if (K + location) >= N:  # 첫번째 경우, 마지막 쉼터를 거치지 않고 이전 쉼터에서 바로 도착지로 갈 수 있는 경우
        pass
    elif (K + location) >= list_M[M-1] and (K + location) < N:  # 두번째 경우, 마지막 쉼터를 거쳐야만 도착지로 갈 수 있는 경우
        count += 1
    # else:   # 세번째 경우, 못 도착하는 경우
    #     count = 0

    print(f"#{tc + 1} {count}")