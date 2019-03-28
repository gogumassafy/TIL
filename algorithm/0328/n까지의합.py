def sumnum(n):
    if n == 1:
        return 1
    return n + sumnum(n-1)

N = int(input())
print(sumnum(N))


