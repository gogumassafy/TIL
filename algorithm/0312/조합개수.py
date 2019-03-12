def comb(n, r, q):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return comb(n-1, r-1, q) + comb(n-1, r, q)


A = [1, 2, 3, 4]
T = [0] * 3

print(comb(100, 49, 3))