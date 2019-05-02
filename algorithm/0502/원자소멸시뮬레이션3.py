import sys
sys.stdin = open('원자소멸시뮬레이션.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def bfs():
    global result, N
    t = 0
    while queue:
        n = len(queue)
        for i in range(n):
            flag = 0
            k = queue.pop(0)
            d, r, c = data[t % 2].pop(0)
            if d == 9:
                result += k
                continue
            nr = r + dr[d]
            nc = c + dc[d]
            if not (2001 > nr >= 0 and 2001 > nc >= 0):
                continue
            for x in range(len(data[t % 2])):
                D, R, C = data[t % 2][x]
                if nr == R and nc == C:
                    if (d == 0 or d == 2) and D == (d + 1):
                        result += k
                        flag = 1
                        data[t % 2][x][0] = 9
                        break
                    elif (d == 1 or d == 3) and D == (d - 1):
                        result += k
                        flag = 1
                        data[t % 2][x][0] = 9
                        break
            if flag:
                continue

            for x in range(len(data[(t + 1) % 2])):
                D, R, C = data[(t + 1) % 2][x]
                if nr == R and nc == C:
                    result += k
                    flag = 1
                    data[(t + 1) % 2][x][0] = 9
                    break

            if flag:
                continue

            data[(t + 1) % 2].append([d, nr, nc])
            queue.append(k)
        t += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # -1000 ~ 1000
    # 0 ~ 2000
    data = [[] for _ in range(2)]
    queue = []
    for i in range(N):
        c, r, d, k = map(int, input().split())
        r = 2000 - (r + 1000)
        c = c + 1000
        # r, c
        queue.append(k)
        data[0].append([d, r, c])
    result = 0
    bfs()
    print('#{} {}'.format(tc, result))
