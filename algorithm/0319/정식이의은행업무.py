import sys
sys.stdin = open('정식이의은행업무.txt')

T = int(input())
for tc in range(1, T + 1):
    two = input()
    two_len = len(two)
    three = input()
    three_len = len(three)

    temp = two_len - 1
    a_decimal = 0
    for i in two:
        a_decimal += (2**temp) * int(i)
        temp -= 1

    temp = three_len - 1
    b_decimal = 0
    for i in three:
        b_decimal += (3**temp) * int(i)
        temp -= 1

    for i in two:
        two_len -= 1
        ternary_len = three_len
        binary_temp = a_decimal
        binary = int(i)
        if binary:
            binary_temp -= 2**two_len
        else:
            binary_temp += 2**two_len
        for j in three:
            ternary_len -= 1
            ternary = int(j)
            for k in range(3):
                ternary_temp = b_decimal
                if ternary == k:
                    continue
                elif ternary > k:
                    ternary_temp -= 3**ternary_len*(ternary-k)
                else:
                    ternary_temp += 3 ** ternary_len * (k - ternary)
                if ternary_temp == binary_temp:
                    print('#{} {}'.format(tc, binary_temp))
                    break
            else:
                continue
            break
        else:
            continue
        break
