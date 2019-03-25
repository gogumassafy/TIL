count = 0
N = 3
A = [0 for _ in range(N)]
data = [1, 2, 3]


def powerset(n, k):
    if n == k:
        print(A)
    else:
        A[k] = 1
        powerset(n, k + 1)
        A[k] = 0
        powerset(n, k + 1)


powerset(N, 0)
