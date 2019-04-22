def quicksort(s, e):
    pivot = (s + e) // 2
    quicksort(s, pivot)
    quicksort(pivot + 1, e)


a = [1, 3, 49, 4, 69, 2, 1, 100, 59, 43]
quicksort(0, len(a) - 1)
