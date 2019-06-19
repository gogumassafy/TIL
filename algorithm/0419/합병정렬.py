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
    global count
    if s < e:
        m = (s + e) // 2
        merge_sort(s, m)
        merge_sort(m + 1, e)
        if a[s] > a[e]:
            count += 1
        merge(s, m, e)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    count = 0
    a = list(map(int, input().split()))
    merge_sort(0, N - 1)
    print("#{} {} {}".format(tc, a[N // 2], count))
