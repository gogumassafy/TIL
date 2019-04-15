a = [5, 10, 2, 4, 6, 7]

for i in range(len(a)):
    key = a[i]
    for j in range(i - 1, -1, -1):
        if key > a[j]:
            a[j + 1] = key
            break
        a[j + 1], a[j] = a[j], a[j + 1]

print(a)
