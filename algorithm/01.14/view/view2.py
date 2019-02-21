import sys
sys.stdin = open("(1206)View_input.txt")

for tc in range(10):
    cnt = 0
    N = int(input())
    input_list = list(map(int, input().split()))

    for i in range(2, N-2):
        left = max(input_list[i-2:i])
        right = max(input_list[i+1:i+3])
        if input_list[i] > max(right, left):
            cnt += input_list[i] - max(right, left)
    print(f'#{tc+1} {cnt}')