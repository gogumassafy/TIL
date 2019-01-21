def seq_search(a, len, key):
    i = 0
    while i < len and a[i] != key:
        i += 1
    if i < len:
        return i
    else:
        return -1


input_list = [4, 9, 11, 23, 2, 19, 7]
key = 20
print(seq_search(input_list, len(input_list), key))