def counting_sort(data):
    temp_list = [0] * len(data)
    cnt = [0] * 10
    for i in data:
        cnt[i] +=1
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]
    for i in data[::-1]:
        temp_list[cnt[i]-1] = i
        cnt[i] -= 1
    return temp_list



data = [2, 1, 5, 3, 4]
print(counting_sort(data))
