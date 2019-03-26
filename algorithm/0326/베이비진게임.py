T = int(input())
for tc in range(1, T + 1):
    raw = list(map(int, input().split()))
    player1 = raw[0::2]
    player2 = raw[1::2]
    winner = 0
    count1 = [0] * 10
    count2 = [0] * 10
    for i in range(6):
        count1[player1[i]] += 1
        if count1[player1[i]] == 3:
            winner = 1
            break

        if i > 1:
            for j in range(0, 8):
                if count1[j] and count1[j+1] and count1[j+2]:
                    winner = 1
                    break
        if winner:
            break
        count2[player2[i]] += 1
        if count2[player2[i]] == 3:
            winner = 2
            break

        if i > 1:
            for j in range(0, 8):
                if count2[j] and count2[j+1] and count2[j+2]:
                    winner = 2
                    break
    print('#{} {}'.format(tc, winner))
