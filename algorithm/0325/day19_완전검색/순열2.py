# def myprint(n):
#     for i in range(n):
#         print(" %d" % (a[i]), end="")
#     print()
def perm(n, k):
    if n == k:
        print(a)
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]

a = [1,2,3]

perm(3, 0)
