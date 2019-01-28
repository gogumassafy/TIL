import sys
sys.stdin = open("색칠하기_input.text")
test_num = int(input())

for tc in range(test_num):
    N = int(input())
    original_map = [[0 for _ in range(10)] for _ in range(10)]
    count = 0

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for row in range(r1, r2 + 1):
            for col in range(c1, c2 + 1):
                if original_map[row][col] != color and original_map[row][col] != 3:
                    original_map[row][col] += color
                    if original_map[row][col] == 3:
                        count += 1
    print(f"#{tc + 1} {count}")


