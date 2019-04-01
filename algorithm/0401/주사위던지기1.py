def perm1(n, k):
    if n == k:
        print(*a)
        return
    for i in range(1, 7):
        a.append(i)
        perm1(n, k + 1)
        a.pop()


def perm2(n, k):
    global N
    if n == k:
        if len(b) == N:
            print(*b)
        return
    for i in range(1, 7):
        if not b:
            b.append(i)
            perm2(n, k + 1)
            b.pop()
        elif i >= b[-1]:
            b.append(i)
            perm2(n, k + 1)
            b.pop()


def perm3(n, k):
    if n == k:
        print(*c)
        return
    for i in range(1, 7):
        if visited[i]:
            continue
        visited[i] = 1
        c.append(i)
        perm3(n, k + 1)
        visited[i] = 0
        c.pop()


N, M = map(int, input().split())
if M == 1:
    a = []
    perm1(N, 0)
elif M == 2:
    b = []
    perm2(N, 0)
else:
    visited = [0] * 7
    c = []
    perm3(N, 0)

