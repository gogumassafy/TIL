T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    game_map = [list(map(int, input().split())) for _ in range(H)]
