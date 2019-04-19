def merge(s, m, e):
    sort_list = []
    l = s
    r = m + 1

    while l <= m and r <= e:
        if a[l] < a[r]:
            sort_list.append(a[l])
            l += 1
        else:
            sort_list.append(a[r])
            r += 1
    if l > m:
        sort_list += a[r:e + 1]
    else:
        sort_list += a[l:m + 1]
    a[s:e + 1] = sort_list


def merge_sort(s, e):
    if s < e:
        m = (s + e) // 2
        merge_sort(s, m)
        merge_sort(m + 1, e)
        merge(s, m, e)


a = [1, 3, 49, 4, 69, 2, 1, 100, 59, 43]
merge_sort(0, len(a) - 1)
print(a)