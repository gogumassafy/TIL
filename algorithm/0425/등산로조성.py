import sys
sys.stdin = open('등산로조성.txt')

# 1. 등산로
# 1.1. 가장 높은 봉우리에서 시작
# 1.2. 높은 봉우리에서 낮은 봉우리로
# 1.3. 딱 한 곳을 정해 최대 K 깊이만큼 지형을 깎을 수 있다.

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def DFS(k, h, r, c, cnt):
    global N, K, result
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 맵을 벗어난 경우
        if not (N > nr >= 0 and N > nc >= 0):
            continue
        if visited[nr][nc]:
            continue
        if raw[nr][nc] >= h:
            # 다음 길이 자신보다 크거나 같은데 깎을 찬스가 없는 경우
            if k == 0:
                continue
            # 다음 길이 자신보다 크거나 같고 깎을 찬스가 있는데 최대한 깎아도 자신보다 크거나 같은 경우
            if raw[nr][nc] - K >= h:
                continue
            visited[nr][nc] = 1
            DFS(0, raw[r][c] - 1, nr, nc, cnt + 1)
            visited[nr][nc] = 0
            continue
        visited[nr][nc] = 1
        DFS(k, raw[nr][nc], nr, nc, cnt + 1)
        visited[nr][nc] = 0
    result = max(result, cnt)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
    # 가장 높은 봉우리를 찾는다.
    max_height = 0
    for i in range(N):
        max_height = max(max_height, max(raw[i]))
    for i in range(N):
        for j in range(N):
            if raw[i][j] == max_height:
                # 찬스, 현재 높이, 행, 열, 카운트
                visited[i][j] = 1
                DFS(1, max_height, i, j, 1)
                visited[i][j] = 0
    print('#{} {}'.format(tc, result))

#1 6
#2 3
#3 7
#4 4
#5 2
#6 12
#7 6
#8 7
#9 10
#10 19
