N = int(input())
input_list = []
max_mul = -float("inf")
each_mul = 0
for _ in range(N):
    input_list.append(float(input()))

for i in range(N):
    each_mul = 1
    for j in range(i, N):
        each_mul *= input_list[j]
        if each_mul <= 1:
            if each_mul > max_mul:
                max_mul = each_mul
            break
        if each_mul > max_mul:
            max_mul = each_mul

print("{:.3f}".format(max_mul))


# 한줄 코드
# n = int(input())
# data = [float(input()) for i in range(n)]
#
# max_product = 1
# now = 1
# count = 0
# for i in range(n):
#     if now*data[i] < 1:
#         now = 1
#     else:
#         if now*data[i] > max_product:
#             max_product = now*data[i]
#         now = now*data[i]
#
# if max_product > 1:
#     print('%.3f' % max_product)
# else:
#     print('%.3f' % max(data))