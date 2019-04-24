def quicksort(s, e):
    if s < e:
        pivot = a[s]
        left = s + 1
        right = e
        while left <= right:
            if a[left] <= pivot:
                left += 1
                continue
            if a[right] > pivot:
                right -= 1
                continue
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
        a[s], a[right] = a[right], a[s]
        quicksort(s, right - 1)
        quicksort(right + 1, e)


def hoare(s, e):
    if s < e:
        left = s
        right = e
        while left < right:
            while left <= e and a[s] >= a[left]:
                left += 1
            while a[s] < a[right]:
                right -= 1
            if left < right:
                a[left], a[right] = a[right], a[left]
        a[s], a[right] = a[right], a[s]
        hoare(s, right - 1)
        hoare(right + 1, e)


def lomuto(l, r):
    if l < r:
        



a = [1, 3, 49, 4, 69, 2, 1, 100, 59, 43]
# quicksort(0, len(a) - 1)
hoare(0, len(a) - 1)
print(a)
