# import sys
# sys.stdin = open('로마숫자만들기.txt')

N = int(input())
cnt = 0
num_list = [0] * (50*20 + 1)
a = b = c = 0
for i in range(N + 1):
    a = i
    for j in range(N + 1 - i):
        b = j
        for k in range(N + 1 - (i + j)):
            c = k
            d = N - (a + b + c)
            num_list[a + 5*b + 10*c + 50*d] = 1
print(sum(num_list))
