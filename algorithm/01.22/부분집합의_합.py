import sys
sys.stdin = open("부분집합의_합_input.text")

test_num = int(input())

A = list(range(1, 13))

for tc in range(test_num):
    N, K = map(int, input().split())
    count = 0

    for i in range(1, 1 << 12):
        sum = 0
        each_count = 0
        for j in range(12):
            if i & (1 << j):
                sum += A[j]
                each_count += 1
        if sum == K and each_count == N:
            count += 1

    print(f"#{tc + 1} {count}")
