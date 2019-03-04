sum_time = 0
for _ in range(5):
    s, e = map(float, input().split())
    if e - s - 1 > 0:
        if e - s - 1 >= 4:
            sum_time += 4
        else:
            sum_time += e - s - 1

if sum_time >= 15:
    print(int(sum_time * 2 * 5000 * 0.95))
elif sum_time <= 5:
    print(int(sum_time * 2 * 1.05 * 5000))
else:
    print(int(sum_time * 2 * 5000))