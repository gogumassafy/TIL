A = 300
B = 60
C = 10

T = int(input())

A_cnt = 0
B_cnt = 0
C_cnt = 0

while T // A:
    T -= A
    A_cnt += 1

while T // B:
    T -= B
    B_cnt += 1

while T // C:
    T -= C
    C_cnt += 1

if T:
    print(-1)
else:
    print(f'{A_cnt} {B_cnt} {C_cnt}')