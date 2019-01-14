def counting_sort(data):
    temp_list = [0] * len(data)
    counting_list = [0] * 10

    for i in range(len(data)):
        counting_list[data[i]] += 1
    for i in range(1, len(counting_list)):
        counting_list[i] += counting_list[i-1]
    for i in range(len(data) -1, -1, -1):
        temp_list[counting_list[data[i]]-1] = data[i]
        counting_list[data[i]] -= 1










data = list(range(10))
counting_sort(data)
print(data)