import sys
sys.stdin = open('차량정비소.txt')


def bf():
    global result, A, B, K, N, M
    reception_count = 0
    repair_count = 0
    time = 0
    pointer = 0
    while 1:
        for i in range(pointer, K):
            if reception_count == N or t[i] > time:
                break
            idx = reception.index(0)
            reception[idx] = t[pointer] + a[idx]
            reception_count += 1
            pointer += 1

        for i in range(N):
            if repair_count == M or reception_count == 0:
                break
            if reception[i] == 0:
                continue
            idx = repair.index(0)
            if i == A and idx == B:
                result += 1
            repair[idx] = reception[i] + b[idx]
            reception[i] = 0
            repair_count += 1
            reception_count -= 1
        time += 1


T = int(input())
for tc in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    reception = [0] * N
    repair_waiting = []
    repair = [0] * M
    t = list(map(int, input().split()))
    result = 0
    bf()

    if result == 0:
        result = -1
    print('#{} {}'.format(tc, result))