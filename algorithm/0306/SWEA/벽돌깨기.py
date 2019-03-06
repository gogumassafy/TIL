import sys
sys.stdin = open('벽돌깨기.txt')

def dfs(r, c):
    global try_num


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    game_map = [list(map(int, input().split())) for _ in range(H)]

    for i in range(W):
        try_num = N
