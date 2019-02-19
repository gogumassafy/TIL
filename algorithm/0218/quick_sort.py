def PrintArray():
    for i in range(len(arr)):
        print("%3d" %arr[i], end=" ")
    print()

def partition(a, l, r):
    pivot = a[l]
    i = l
    j = r

    while i < j:
        while a[i] <= pivot:
            i += 1
            if(i == r): break
        while a[j] >= pivot:
            j -= 1
            if(j == l): break
        if i < j:
            a[i], a[j] = a[j], a[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quicksort(a, low, high):
    if low < high:
        pivot = partition(a, low ,high)
        quicksort(a, low, pivot-1)
        quicksort(a, pivot+1, high)

arr = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
#arr = [69, 10, 30, 2, 16, 8, 31, 22]

PrintArray()
quicksort(arr, 0, len(arr)-1)
PrintArray()