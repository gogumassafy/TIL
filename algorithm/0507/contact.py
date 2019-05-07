import sys
sys.stdin = open('contact.txt')


def bfs():
    global result
    while queue:
        t = len(queue)
        who = []

        for i in range(t):
            s = queue.pop(0)
            who.append(s)
            if s in linked.keys():
                for next in linked[s]:
                    if visited[next]:
                        continue
                    queue.append(next)
                    visited[next] = 1
    result = max(who)


for tc in range(1, 11):
    N, S = map(int, input().split())
    raw = list(map(int, input().split()))
    linked = {}
    for i in range(0, len(raw), 2):
        if raw[i] in linked:
            linked[raw[i]].append(raw[i + 1])
        else:
            linked[raw[i]] = [raw[i + 1]]
    queue = []
    visited = [0] * (max(raw) + 1)
    result = -1
    queue.append(S)
    visited[S] = 1
    bfs()
    print('#{} {}'.format(tc, result))