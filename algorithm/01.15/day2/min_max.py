import sys
sys.stdin = open("min_max_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    min = 987654321
    max = -987654321
    for i in range(N):
        if min > data[i]:
            min = data[i]
        if max < data[i]:
            max = data[i]

    ans = max - min
    print("#{0} {1}".format(test_case, ans))

