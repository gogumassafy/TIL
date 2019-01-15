import sys
sys.stdin = open("sample_input_bus.txt")

T = int(input())


for tc in range(T):
    count = 0
    location = 0
    K, N, M = map(int, input().split()) # 각각 보폭, 도착지점의 좌표, 쉬어갈 수 있는 장소의 수
    list_M = list(map(int, input().split())) # 쉬어갈 수 있는 장소의 좌표

    for i in range(M): # 쉬어갈 수 있는 모든 장소의 좌표를 고려한다.

        if M - 1 == i: #결과 판단 부분
            if (K + location) >= N: # 첫번째 경우, 마지막 쉼터를 거치지 않고 이전 쉼터에서 바로 도착지로 갈 수 있는 경우
                break
            elif (K + location) >= list_M[i] and (K + list_M[i]) >= N: # 두번째 경우, 마지막 쉼터를 거쳐야만 도착지로 갈 수 있는 경우
                count += 1
                break
            else:
                count =0

        elif list_M[i] <= (K + location) and list_M[i+1] > (K + location): # 세번째 경우, 최대한 안쉬고 다음 쉼터를 고르는 경우
            location = list_M[i]
            count += 1

    print(f"#{tc+1} {count}")