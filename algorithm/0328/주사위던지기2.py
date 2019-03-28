def perm(n, k, s):
    global M
    if M > s + (n - k)*6:
        return
    if n == k:
        if sum(A) == M:
            print(*A)
        return
    else:
        for i in range(1, 7):
            A.append(i)
            perm(n, k + 1, s + i)
            A.pop()


N, M = map(int, input().split())
A = []
perm(N, 0, 0)




