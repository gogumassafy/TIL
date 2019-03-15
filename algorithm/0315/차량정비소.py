T = int(input())
for tc in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    # 접수
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    k = list(map(int, input().split()))

    a_queue = []
    b_queue = []
    time = 0
    while 1:
        for i in range(len(k)):
            if k[i] == time:
                a_queue.append(i)
                continue
            break


        time += 1

    print('#{} {}'.format(tc, 1))