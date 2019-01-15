import sys
sys.stdin = open("sample_input_bus.txt")

T = int(input())

for tc in range(T):
    count = 0
    location = 0
    K, N, M = map(int, input().split())
    list_M = list(map(int, input().split()))

    for i in range(len(list_M)):
        if len(list_M) - 1 == i:
            if (K + location) >= N:
                break
            elif (K + location) >= list_M[i] and (K + list_M[i]) >= N:
                count += 1
                break
            else:
                count =0
        elif list_M[i] <= (K + location) and list_M[i+1] > (K + location):
            location = list_M[i]
            count += 1

    print(f"#{tc+1} {count}")






















