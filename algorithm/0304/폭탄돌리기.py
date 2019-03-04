# 사람의 수는 8명
# 틀리거나 통과시 다음 문제 또 풀어야 함.
K = int(input())
N = int(input())
sum_time = 0

for i in range(N):
    T, Z = input().split()
    sum_time += int(T)
    if sum_time >= 211:
        break
    if Z == 'T':
        if K == 8:
            K = 1
        else:
            K += 1

print(K)