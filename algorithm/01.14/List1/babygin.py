num = 135799

cnt = [0] * 12

for i in set(str(num)):
    for j in str(num):
        if i == j:
            cnt[int(i)] += 1

tri = run = i = 0
while i < 10:
    if cnt[i] >= 3:
        cnt[i] -= 3
        tri += 1
        continue
    elif cnt[i] == cnt[i+1] == cnt[i+2]:
        cnt[i] -= 1
        cnt[i+1] -= 1
        cnt[i+2] -= 1
        run +=1
        continue
    i += 1

if tri + run == 2:
    print(f'baby gin')
else:
    print(f'not baby gin')