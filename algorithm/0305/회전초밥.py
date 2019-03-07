N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
max_len = -float('inf')
for i in range(N):
    if i + k > N
        temp = sushi[i:] + sushi[:i]
        result = set(temp[0:k] + [c])
    else:
        result = set(sushi[i:i+k] + [c])
    count = len(result)
    if count > max_len:
        max_len = count
print(max_len)

