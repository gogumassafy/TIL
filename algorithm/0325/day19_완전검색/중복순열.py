def myprint(q):

    while(q):
        q -= 1
        print(" %d" % (t[q]), end="")
    print()
def PI(n, r, q):
    if r==0:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):
            a[i], a[n-1] = a[n-1], a[i]
            t[r-1] = a[n-1]
            PI(n, r-1, q)
            a[i], a[n - 1] = a[n - 1], a[i]

a = [1,2,3]
t = [0] * 3

PI(3, 2, 2)