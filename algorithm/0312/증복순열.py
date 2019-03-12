

def pi(n, r, q):
    if not r:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):
            a[i], a[n-1] = a[n-1], a[i]
            t[r - 1] = a[n - 1]
            pi(n, r - 1, q)
            a[i], a[n-1] = a[n-1], a[i]


def myprint(q):
    while q:
        q -= 1
        print(t[q], end=' ')
    print()


t = [0] * 3 # 얘는 r의 개수와 같다.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pi(4, 3, 3)