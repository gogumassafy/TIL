C, R = map(int, input().split())
K = int(input())

seat = [[0] * C for _ in range(R)]
limit = C*R
sum_cir = 0

if K > limit:
    print(0)
else:
    base_row = R
    row = R - 1
    col = 0
    while sum_cir < limit:
        if K <= sum_cir + 2*(R+C-2):
            # (col, row)
            if K <= sum_cir + R:
                base_row -= sum_cir + R - K
                print('{} {}'.format(col + 1, base_row))
                break
            elif K <= sum_cir + R + C - 1:
                col += K - (sum_cir + R) + 1
                print('{} {}'.format(col, base_row))
                break
            elif K <= sum_cir + 2*R + C - 2:
                base_row -= K - (sum_cir + R + C - 1)
                print('{} {}'.format(col + C, base_row))
                break
            else:
                col += sum_cir + 2*(R+C-2) + 2 - K
                print('{} {}'.format(col, base_row-R+1))
                break
        else:
            sum_cir += 2*(R+C-2)
            R -= 2
            C -= 2
            base_row -= 1
            row -= 1
            col += 1
