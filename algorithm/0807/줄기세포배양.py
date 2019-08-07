import sys
sys.stdin = open('줄기세포배양.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def bfs():
    global K
    now = 0
    while que and now < K:
        rotation = len(que)
        for _ in range(rotation):
            r, c = que.pop(0)
            origin = raw_data[r][c][0]
            life = raw_data[r][c][1]
            if life == 0:
                continue
            if origin != life:
                raw_data[r][c][1] -= 1
                que.append((r, c))
                continue

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (N + K > nr >= 0 and M + K > nc >= 0):
                    continue
                if raw_data[nr][nc] == 0:
                    raw_data[nr][nc] = [origin, 2 * origin, now]
                    que.append((nr, nc))
                elif origin > raw_data[nr][nc][0] and now == raw_data[nr][nc][2]:
                    raw_data[nr][nc] = [origin, 2 * origin, now]
            raw_data[r][c][1] -= 1
            que.append((r, c))
        now += 1


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    raw_data = [[0] * (K + M) for _ in range(K + N)]
    for r in range(N):
        raw_data[r + (K // 2)][K // 2:(K // 2) + M] = list(map(int, input().split()))
    que = []
    result = 0
    for r in range(N + K):
        for c in range(M + K):
            if raw_data[r][c]:
                raw_data[r][c] = [raw_data[r][c], 2 * raw_data[r][c], 0]
                que.append((r, c))
    bfs()
    for r in range(N + K):
        for c in range(M + K):
            if raw_data[r][c] == 0:
                continue
            elif raw_data[r][c][1] != 0:
                result += 1
    print("#{} {}".format(tc, result))
