import sys

sys.stdin = open("contact.txt")


def contact(v):
    queue = []
    queue.append(v)
    visited = [0] * 101
    visited[v] = 1
    result = []

    while queue:
        t = queue.pop(0)
        if t in connects:
            for i in connects[t]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = visited[t] + 1
    print(f'#{tc} {len(visited) - 1 - visited[::-1].index(max(visited))}')


for tc in range(1, 11):
    a, b = map(int, input().split())
    data = list(map(int, input().split()))
    connects = {}
    for i in range(0, len(data), 2):
        if data[i] in connects and data[i + 1] not in connects[data[i]]:
            connects[data[i]] += [data[i + 1]]
        else:
            connects[data[i]] = [data[i + 1]]

    contact(b)