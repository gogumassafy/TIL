a = [5, 10, 2, 4, 6, 7]

for i in range(len(a) - 1):
    min_idx = i
    for j in range(i + 1, len(a)):
        if a[min_idx] > a[j]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]

print(a)