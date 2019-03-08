N = int(input())
raw_data = list(map(int, input().split()))

max_len = 0
big_cnt = 1
for i in range(1, len(raw_data)):
    if raw_data[i] >= raw_data[i-1]:
        big_cnt += 1
    else:
        big_cnt = 1
    if max_len < big_cnt:
        max_len = big_cnt

small_cnt = 1
for i in range(1, len(raw_data)):
    if raw_data[i] <= raw_data[i-1]:
        small_cnt += 1
    else:
        small_cnt = 1
    if max_len < small_cnt:
        max_len = small_cnt
print(max_len)