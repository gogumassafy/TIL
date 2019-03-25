import sys, time
from time import strftime
sys.stdin = open('test_input.txt')

start_time = time.time()

def perm(n, k, length):
    global result
    if length >= result:
        return
    if n == k:
        length = 0
        stack = []
        stack.append(work)
        for i in N_list:
            stack.append(i)
        stack.append(home)
        for i in range(len(stack) - 1):
            x = stack[i][0]
            y = stack[i][1]
            nx = stack[i + 1][0]
            ny = stack[i + 1][1]
            length += abs(nx - x) + abs(ny - y)
        result = min(result, length)
    else:
        for i in range(k, n):
            N_list[i], N_list[k] = N_list[k], N_list[i]
            perm(n, k + 1)
            N_list[i], N_list[k] = N_list[k], N_list[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = list(map(int, input().split()))
    work = [raw[0], raw[1]]
    home = [raw[2], raw[3]]
    N_list = []
    for i in range(4, len(raw), 2):
        N_list.append([raw[i], raw[i + 1]])
    result = float('inf')
    perm(N, 0, 0)

    print('#{} {}'.format(tc, result))

print(time.time() - start_time, 'seconds')