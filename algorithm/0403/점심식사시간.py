import queue, collections


# def solve(s0, s1):
#     time = 0
#     while len(s0ing) < 3 and s0:
#         s0ing.append(s0.get())
#     while len(s1ing) < 3 and s1:
#         s1ing.append(s1.get())
#     for


def solve(s0, s1):
    time = 0
    s0ing = 3
    s1ing = 3
    while s0 or s1:
        for i in range(len(s0)):
            s0[i] -= 1
        for i in range(len(s1)):
            s1[i] -= 1

        time += 1
    return time


def perm(n, k):
    if n == k:
        s0 = queue.PriorityQueue()
        s1 = queue.PriorityQueue()
        # print(p)
        # print(time)
        for i in range(len(p)):
            if p[i]:
                s1.put(time[i])
            else:
                s0.put(time[i])
        print(s0.queue)
        print(s1.queue)
        # solve(s0, s1)
        return
    p[k] = 1
    time.append((abs(men[k][0] - stairs[1][0]) + abs(men[k][1] - stairs[1][1]) + 1))
    perm(n, k + 1)
    time.pop()
    p[k] = 0
    time.append((abs(men[k][0] - stairs[0][0]) + abs(men[k][1] - stairs[0][1]) + 1))
    perm(n, k + 1)
    time.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    men = []
    stairs = []
    K = []
    for i in range(N):
        for j in range(N):
            if raw[i][j] == 1:
                men.append((i, j))
            elif raw[i][j] > 1:
                K.append(raw[i][j])
                stairs.append((i, j))
    # print(stairs)
    # print(men)
    result = float('inf')
    time = []
    s0ing = collections.deque()
    s1ing = collections.deque()
    p = [0] * len(men)
    perm(len(men), 0)
