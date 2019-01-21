def binary_search(a, key):
    start = 0
    end = len(a) - 1

    while start <= end:
        middle = (start + end) // 2

        if a[middle] == key:
            return middle
        elif a[middle] < key:
            start = middle + 1
        else:
            end = middle - 1

    return -1

key = 2
data = [2, 4, 7, 9, 11, 19, 23]
print(binary_search(data, key))
