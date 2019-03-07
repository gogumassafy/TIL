N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
max_len = -float('inf')
for i in range(N):
    if i + k > N:
        result = set(sushi[i:])|set(sushi[:k - (N - i)])|set([c])
    else:
        result = set(sushi[i:i+k])|set([c])
    count = len(result)
    if count > max_len:
        max_len = count
print(max_len)