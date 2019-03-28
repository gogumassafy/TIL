def perm(n, k):
    global count
    if n == k:
        count += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        if check(k, i):
            continue
        visited[i] = 1
        mapping.append((k, i))
        perm(n, k + 1)
        visited[i] = 0
        mapping.pop()


def check(r, c):
    for i in range(r):
        queen = mapping[i]
        if not abs(queen[0] - r) - abs(queen[1] - c):
            return True
    return False


N = int(input())
visited = [0] * N
mapping = []
count = 0
perm(N, 0)
print(count)
