def fibo(num):
    if num < 3:
        return 1
    return fibo(num-1) + fibo(num-2)

print(fibo(8))