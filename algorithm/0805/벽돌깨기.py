import sys
sys.stdin = open('벽돌깨기.txt')


def dfs(depth):
    if N == depth:
        return

    return


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    raw_data = [list(map(int, input().split())) for _ in range(N)]

