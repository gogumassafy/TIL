import sys
sys.stdin = open("(1206)View_input.txt")
T = 10
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans = 0

    for i in range(2, N-2):
        min = 987654321
        for j in range(5):
            if j != 2:
                if data[i]-data[i-2+j] < min:
                    min = data[i] - data[i-2+j]
        if min > 0:
            ans += min

    print("#{} {}".format(tc+1, ans))


