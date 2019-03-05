N = int(input())
input_list = [list(map(int, input().split())) for _ in range(N)]
input_list = [x for x in zip(*input_list)]
score = [0] * 3

for i in range(3):
    score[i] = [sum(input_list[i]), input_list[i].count(3), input_list[i].count(2)]

max_score = max(score)
if score.count(max_score) == 1:
    max_idx = score.index(max(score))
    print('{} {}'.format(max_idx+1, max_score[0]))
else:
    print("0 {}".format(max_score[0]))