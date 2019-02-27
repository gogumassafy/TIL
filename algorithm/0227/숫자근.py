n = int(input())

def findnum(x, y):
    digitx = digitroot(x)
    digity = digitroot(y)
    if digitx < digity:
        return y
    elif digitx == digity:
        return x if x < y else y
    else:
        return x

def digitroot(x):
    total = 0
    while x//10:
        for i in str(x):
            total += int(i)
        x = total
        total = 0
    return x

# 선생님 정리 코드
# def root_calc(num):
#     while True:
#         temp = list(map(int, str(num)))
#         tot=sum(temp)
#         if tot<10:
#             return tot
#         num = tot
#     # while True:
#     #     tot=0
#     #     while num:
#     #         tot += num%10
#     #         num/=10
#     #     if tot < 10:
#     #         return num
#     #     num = tot
#             

x = int(input())
for i in range(n-1):
    y = int(input())
    x = findnum(x,y)

print(x)



