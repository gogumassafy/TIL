import sys
sys.stdin = open("view_input.txt")

for tc in range(10):
    N = int(input())
    data = list(map(int, input().split()))
    count = 0
    for i in range(2, len(data) - 2):
        left = max(data[i-2:i])
        right = max(data[i+1:i+3])
        max_height = max(left, right)
        if data[i] > max_height:
            count += (data[i] - max_height)
    print(f"#{tc + 1} {count}")
