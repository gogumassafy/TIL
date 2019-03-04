a, b = map(int, input().split())
a, b = min(a, b), max(a, b)

num_list = [i if i > 1 else 0 for i in range(b+1)]

for i in range(2, int(b**0.5)+1):
    if not num_list[i]:
        continue
    for j in range(2, b):
        if i * j > b:
            break
        num_list[i*j] = 0

num_list = [i for i in num_list[a:] if i]

print(len(num_list))
print(min(num_list) + max(num_list))
