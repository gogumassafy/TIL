N = int(input())
input_list = list(map(int, input().split()))

smart = 0
dull = 0
dull_max = 0
for i in input_list:
    if i > 0:
        smart += i
    if dull + i > 0:
        dull += i
        if dull > dull_max:
            dull_max = dull
    else:
        dull = 0
if smart <= 0 and dull_max <= 0:
    smart = max(input_list)
    dull_max = max(input_list)

print('{} {}'.format(dull_max, smart))