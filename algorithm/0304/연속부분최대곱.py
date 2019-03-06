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