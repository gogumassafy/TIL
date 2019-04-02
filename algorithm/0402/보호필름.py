T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(D)]
