a = [5, 10, 2, 4, 6, 7]


for i in range(1, len(a) - 1):
    for j in range(len(a) - i):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]

print(a)