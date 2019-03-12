def H(n, r, q):
    if r == 0:
        myprint(q)
    elif n == 0:
        return
    else:
        T[r-1] = A[n-1]
        H(n, r - 1, q)
        H(n - 1, r, q)


def myprint(q):
    while q > 0:
        q -= 1
        print(T[q], end=' ')
    print()


A = [1, 2, 3, 4]
T = [0, 0, 0]
H(4, 3, 3)
