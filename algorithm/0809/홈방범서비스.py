import sys
sys.stdin = open('홈방범서비스.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def dfs(r, c):
    global result, M
    visited = [[0] * N for _ in range(N)]
    que = [(r, c)]
    count = 0
    visited[r][c] = 1
    for depth in range(1, 50):
        time = len(que)
        for i in range(time):
            r, c = que.pop(0)
            if raw[r][c]:
                count += 1
            for j in range(4):
                nr = r + dr[j]
                nc = c + dc[j]
                if not (N > nr >= 0 and N > nc >= 0):
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = 1
                que.append((nr, nc))
        if M * count - K[depth] >= 0:
            result = max(result, count)
    return


K = [0]
for i in range(1, 50):
    temp = i**2 + (i - 1)**2
    K.append(temp)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(N):
            dfs(r, c)
    print("#{} {}".format(tc, result))
