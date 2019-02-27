
T = int(input())
A = T//300
T %= 300
B = T//60
T %= 60
C = T//10
T %= 10
if T :
    print(-1)
else:
    print(A, B, C)