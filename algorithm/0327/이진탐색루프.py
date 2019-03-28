def binarysearch(start, end, value):
    while start < end:
        mid = (start + end) // 2
        if value == a[mid]:
            return mid
        elif value > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return start


a = [1, 2, 3, 4, 5, 7, 8]
print(binarysearch(0, len(a), 3))


