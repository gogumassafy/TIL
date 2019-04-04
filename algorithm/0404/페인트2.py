import sys
import collections
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
dr2 = [-1, -1, 1, 1]
dc2 = [-1, 1, -1, 1]


def bfs(depth):
    global N, K
    cnt = 0
    while q:
        k, r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if k >= K:
                break
            if not visited[nr][nc] and not raw[nr][nc]:
                cnt += 1
            if depth == 0:
                visited[nr][nc] = 1
            q.append((k + 1, nr, nc))
    return cnt


N = int(input())
K = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
q = collections.deque()
result = 0
for r1 in range(N):
    for c1 in range(N):
        visited = [[0] * N for _ in range(N)]
        q.append((0, r1, c1))
        if raw[r1][c1]:
            count1 = bfs(0)
        else:
            visited[r1][c1] = 1
            count1 = 1 + bfs(0)
        for r2 in range(r1, N):
            for c2 in range(N):
                q.append((0, r2, c2))
                if raw[r2][c2] or visited[r2][c2]:
                    count2 = bfs(1)
                else:
                    count2 = 1 + bfs(1)
                result = max(result, count1 + count2)
print(result)
