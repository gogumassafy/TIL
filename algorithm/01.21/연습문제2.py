input_num = list(map(int, input().split()))

for i in range(1, 1 << len(input_num)):
    sum = 0
    for j in range(len(input_num)):
        if i & (1 << j):
            sum += input_num[j]
    if not sum:
        print("존재!")