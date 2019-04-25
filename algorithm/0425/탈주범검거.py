import sys
sys.stdin = open('탈주범검거.txt')

import collections

# 탈주범
# 1. 시간당 1의 거리 이동

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

# 상 좌 하 우
pipe = ((0, 0, 0, 0), (1, 1, 1, 1), (1, 0, 1, 0), (0, 1, 0, 1), (1, 0, 0, 1), (0, 0, 1, 1), (0, 1, 1, 0), (1, 1, 0, 0))


def BFS():
    global N, M, L
    count = 1
    while q:
        r, c = q.popleft()
        if visited[r][c] == L:
            continue
        for i in range(4):
            # 현재 위치의 파이프가 해당 방향으로 나갈 구멍이 없을 경우
            if pipe[raw[r][c]][i] == 0:
                continue
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and M > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            if pipe[raw[nr][nc]][(i + 2) % 4] == 0:
                continue
            visited[nr][nc] = 1 + visited[r][c]
            q.append((nr, nc))
            count += 1
    return count


T = int(input())
for tc in range(1, T + 1):
    # 세로, 가로 , 맨홀 뚜껑 세로, 맨홀 뚜껑 가로
    N, M, R, C, L = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = collections.deque()
    q.append((R, C))
    visited[R][C] = 1
    print('#{} {}'.format(tc, BFS()))