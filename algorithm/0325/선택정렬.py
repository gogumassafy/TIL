def selectionsort(a):
    n = len(a)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        temp = a[min]
        a[min] = a[i]
        a[i] = temp


def recursionselectionsort(a, idx):
    if idx == len(a) - 1:
        return
    min_idx = idx
    for i in range(idx+1, len(a)):
        if a[i] < a[min_idx]:
            min_idx = i
        temp = a[min_idx]
        a[min_idx] = a[idx]
        a[idx] = temp
    recursionselectionsort(a, idx + 1)


# a = [4, 3, 6, 1]
# selectionsort(a)
# print(a)

a = [4, 3, 6, 1]
recursionselectionsort(a, 0)
print(a)
