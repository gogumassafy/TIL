N = int(input())
card = [list(map(int, input().split())) for _ in range(N)]
score = [0] * N
set_card = [x for x in zip(*card)]

for i in range(3):
    for j in range(N):
        if set_card[i].count(set_card[i][j]) == 1:
            score[j] += set_card[i][j]

for i in range(N):
    print(score[i])