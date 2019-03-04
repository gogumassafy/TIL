R = int(input())
cnt = 0
for row in range(R):
    for col in range(R):
        if (R - col)**2 + (R - row)**2 <= R**2:
            cnt += 1
print(cnt*4)

