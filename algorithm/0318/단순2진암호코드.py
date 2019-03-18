import sys
sys.stdin = open('암호코드.txt')

pwd = [
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1],
]


T = int(input())
for i in range(10):
    pwd[i].reverse()
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    raw = [list(reversed(list(map(int, input())))) for _ in range(N)]
    for row in range(N):
        if not raw[row].count(1):
            continue
        num_list = [0] * 8
        idx = raw[row].index(1)
        for i in range(8):
            for j in range(10):
                if raw[row][idx + i*7:idx + (i + 1)*7] == pwd[j]:
                    num_list[i] = j
                    break
        break
    sum_num = 0
    for i in range(8):
        if i != 0 and i % 2:
            sum_num += 2 * num_list[i]
    sum_num += sum(num_list)
    print('#{} 0'.format(tc)) if sum_num % 10 else print('#{} {}'.format(tc, sum(num_list)))

#1 38
#2 0
#3 34
#4 28
#5 24
#6 26
#7 36
#8 30
#9 0
#10 34