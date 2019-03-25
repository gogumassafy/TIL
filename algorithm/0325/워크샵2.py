import sys, time
from time import strftime
sys.stdin = open('test_input.txt')
start_time = time.time()


def bf(num, now, length):
    global N, result
    x = now[0]
    y = now[1]
    if length >= result:
        return
    if num == N:
        nx = home[0]
        ny = home[1]
        length += abs(nx - x) + abs(ny - y)
        result = min(length, result)
        return
    for i in range(len(N_list)):
        if not visited[i]:
            nx = N_list[i][0]
            ny = N_list[i][1]
            next_length = abs(nx - x) + abs(ny - y)
            visited[i] = 1
            bf(num + 1, N_list[i], length + next_length)
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = list(map(int, input().split()))
    work = [raw[0], raw[1]]
    home = [raw[2], raw[3]]
    N_list = []
    visited = [0 for _ in range(N)]
    for i in range(4, len(raw), 2):
        N_list.append([raw[i], raw[i + 1]])
    result = float('inf')
    bf(0, work, 0)

    print('#{} {}'.format(tc, result))

print(time.time() - start_time, 'seconds')
