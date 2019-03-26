T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    reservation = [list(map(int, input().split())) for _ in range(N)]
    reservation.sort(key=lambda x:x[1])
    start, end = reservation[0][0], reservation[0][1]
    count = 1
    for i in range(1, len(reservation)):
        selectedS, selectedE = reservation[i][0], reservation[i][1]
        if selectedS >= end:
            count += 1
            start, end = selectedS, selectedE

    print('#{} {}'.format(tc, count))
