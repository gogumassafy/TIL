my_bingo = []
for i in range(5):
    my_bingo += list(map(int, input().split()))
host_bingo = []
for i in range(5):
    host_bingo += list(map(int, input().split()))

for i in range(len(host_bingo)):
    number = host_bingo[i]
    idx = my_bingo.index(number)
    my_bingo[idx] = 0
    cnt = 0
    for j in range(5):
        if not sum(my_bingo[5*j:5*(j+1)]):
            cnt += 1
        if not sum(my_bingo[j:j+21:5]):
            cnt += 1
    if not sum(my_bingo[4:21:4]):
        cnt += 1
    if not sum(my_bingo[0:25:6]):
        cnt += 1
    if cnt >= 3:
        print(i+1)
        break