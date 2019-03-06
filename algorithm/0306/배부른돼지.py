N = int(input())
min_num = float('inf')
max_num = -float('inf')
if not N:
    print('F')
else:
    for i in range(N):
        num, answer = input().split()
        if answer == 'Y':
            if min_num > int(num):
                min_num = int(num)
        else:
            if int(num) > max_num:
                max_num = int(num)
    if max_num >= min_num:
        print("F")
    else:
        print(min_num)
