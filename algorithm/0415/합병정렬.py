def merge(s, m, e):
    sort_list = []
    left = s
    right = m + 1

    while left <= m and right <= e:
        if a[left] < a[right]:
            sort_list.append(a[left])
            left += 1
        else:
            sort_list.append(a[right])
            right += 1
    if left > m:
        sort_list += a[right:e + 1]
    else:
        sort_list += a[left:m + 1]
    a[s:e + 1] = sort_list


def merge_sort(start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        merge(start, mid, end)


a = [5, 10, 2, 4, 6, 7]
merge_sort(0, len(a) - 1)
print(a)
