import sys
sys.stdin = open('보물상자.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    try_num = N // 4
    num = list(input())
    num = [10 if i == 'A' else
           11 if i == 'B' else
           12 if i == 'C' else
           13 if i == 'D' else
           14 if i == 'E' else
           15 if i == 'F' else int(i) for i in num]
    set_sol = set()
    for i in range(try_num):
        for j in range(4):
            start = j*try_num
            end = start + try_num
            exponent = try_num - 1
            total = 0
            for k in num[start:end]:
                total += k * 16 ** exponent
                exponent -= 1
            set_sol.add(total)
        num.insert(0, num.pop())
    set_sol = sorted(list(set_sol), reverse=True)
    print('#{} {}'.format(tc, set_sol[K-1]))
