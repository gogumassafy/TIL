import sys
sys.stdin = open('미생물격리.txt')

# 상 좌 하 우
dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)


def DFS():
    global N, M
    for t in range(M):
        cir = len(queue)
        for _ in range(cir):
            r, c = queue.pop(0)
            if raw[t % 2][r][c][0] == 0:
                raw[t % 2][r][c] = [0, 0, 0]
                continue
            n = raw[t % 2][r][c][0]
            raw[t % 2][r][c][1] = n
            d = raw[t % 2][r][c][2]
            nr = r + dr[d]
            nc = c + dc[d]
            if not (N - 1 > nr > 0 and N - 1 > nc > 0):
                raw[(t + 1) % 2][nr][nc] = [n // 2, n // 2, (d + 2) % 4]
                queue.append((nr, nc))
            else:
                if raw[(t + 1) % 2][nr][nc][0]:
                    raw[(t + 1) % 2][nr][nc][0] += n
                    if raw[(t + 1) % 2][nr][nc][1] < n:
                        raw[(t + 1) % 2][nr][nc][1] = n
                        raw[(t + 1) % 2][nr][nc][2] = d
                else:
                    raw[(t + 1) % 2][nr][nc] = raw[t % 2][r][c]
                    queue.append((nr, nc))
            raw[t % 2][r][c] = [0, 0, 0]


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    raw = [[[[0, 0, 0] for _ in range(N)] for _ in range(N)] for _ in range(2)]
    queue = []
    for i in range(K):
        r, c, n, d = map(int, input().split())
        # 1:상 2:하 3:좌 4:우
        if d == 2:
            d = 3
        elif d == 3:
            d = 2
        # 총 생명, 합쳐진 애들 중 가장 큰 애, 방향
        raw[0][r][c] = [n, n, d - 1]
        queue.append((r, c))
    DFS()
    result = 0
    for i in range(N):
        for j in range(N):
            result += raw[(M % 2)][i][j][0]
    print('#{} {}'.format(tc, result))
