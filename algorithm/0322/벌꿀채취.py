import sys
sys.stdin = open('벌꿀채취.txt')


def bruteforce(num, value):
    global N, M, result
    if num == 2:
        result = max(value, result)
        return 0
    for i in range(N):
        for j in range(N - M + 1):
            if sum(visited[i][j:j + M]):
                continue
            sum_num = 0
            sol = 0
            temp = raw[i][j:j + M]
            # C에 따라서 어느 벌꿀통을 채취할 것인지가 중요한 이슈다.






            max_temp = 0
            for first in range(len(temp)):
                first_num = temp[first]
                if first_num <= C:
                    sum_num += first_num
                    sol = first_num ** 2
                for second in range(first + 1, len(temp)):
                    second_num = temp[second]
                    if sum_num + second_num <= C:
                        sum_num += second_num
                        sol += second_num ** 2
                    max_temp = max(max_temp, sol)




            visited[i][j:j + M] = [1]*M
            bruteforce(num + 1, value + sol)
            visited[i][j:j + M] = [0] * M


T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
    bruteforce(0, 0)
    print('#{} {}'.format(tc, result))

#1 174
#2 131
#3 145
#4 155
#5 166
#6 239
#7 166
#8 172
#9 291
#10 464
