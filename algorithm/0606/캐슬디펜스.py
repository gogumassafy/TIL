import itertools
import copy
import sys
sys.stdin = open('캐슬디펜스.txt')


def kill():
    global N, D, q, archer
    count = 0
    target = [[-1, -1] for _ in range(3)]
    for i in range(len(archer)):
        min_dist = float('inf')
        ar, ac = N, archer[i]
        for er, ec in q:
            dist = abs(ar - er) + abs(ac - ec)
            if dist <= D:
                if dist > min_dist:
                    continue
                if dist == min_dist and target[i][1] < ec:
                    continue
                min_dist = dist
                target[i] = [er, ec]
    for i in range(3):
        r, c = target.pop()
        if r == -1:
            continue
        if data[r][c]:
            data[r][c] = 0
            count += 1
    return count


def game():
    global N, M, archer, result, life, data
    count = 0
    while life:
        if result >= count + life:
            return
        kc = kill()
        count += kc
        life -= kc
        t = len(q)
        for i in range(t):
            r, c = q.pop(0)
            if data[r][c] == 0:
                continue
            if r == (N - 1):
                life -= 1
                continue
            q.append((r + 1, c))
        data = [[0] * M] + data[:N-1]
    result = max(result, count)


N, M, D = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
position = [i for i in range(M)]
archers = list(itertools.combinations(position, 3))
result = 0
total = 0
queue = []

for i in range(N):
    for j in range(M):
        if raw[i][j]:
            queue.append((i, j))
            total += 1


for archer in archers:
    life = total
    data = copy.deepcopy(raw)
    q = copy.deepcopy(queue)
    game()
print(result)