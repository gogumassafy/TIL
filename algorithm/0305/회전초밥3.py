N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
count_list = [0] * (d+1)
max_len = -float('inf')
for i in range(k):
    count_list[sushi[i]] += 1
count_list[c] += 1
count = len([x for x in count_list if x > 0])
for i in range(1, N):
    count_list[sushi[i - 1]] -= 1
    if not count_list[sushi[i - 1]]:
        count -= 1
    if i + k > N:
        if not count_list[sushi[k-(N-i+1)]]:
            count += 1
        count_list[sushi[k-(N-i+1)]] +=1
    else:
        if not count_list[sushi[i+k-1]]:
            count += 1
        count_list[sushi[i+k-1]] += 1

    if count > max_len:
        max_len = count
print(max_len)