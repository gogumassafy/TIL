N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
count = 0
for a in A:
    count += 1
    if B >= a:
        continue
    a -= B
    count += a // C
    if a % C:
        count += 1
print(count)