import sys
import collections
input = sys.stdin.readline

# 동 서 남 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs():
    global result, M, N, gr, gc, gd
    while q:
        r, c, d = q.popleft()
        if r == gr - 1 and c == gc - 1 and d == gd - 1:
            # 걸린 시간 넣기
            result = visited[d][r][c] - 1
            return
        # 3가지 선택이 있음. 그냥 가기. 왼쪽 돌기, 오른쪽 돌기
        for i in range(3):
            if i == 0:
                nr = r
                nc = c
                for dist in range(3):
                    nr += dr[d]
                    nc += dc[d]
                    if not (M > nr >= 0 and N > nc >= 0):
                        break
                    if visited[d][nr][nc]:
                        continue
                    if raw[nr][nc]:
                        break
                    visited[d][nr][nc] = visited[d][r][c] + 1
                    q.append((nr, nc, d))
            # 왼쪽으로 돌기
            elif i == 1:
                if d == 0:
                    nd = d + 3
                elif d == 2 or d == 3:
                    nd = d - 2
                else:
                    nd = d + 1
                if visited[nd][r][c]:
                    continue
                visited[nd][r][c] = visited[d][r][c] + 1
                q.append((r, c, nd))
            # 오른쪽으로 돌기
            else:
                if d == 0 or d == 1:
                    nd = d + 2
                elif d == 2:
                    nd = d - 1
                else:
                    nd = d - 3
                if visited[nd][r][c]:
                    continue
                visited[nd][r][c] = visited[d][r][c] + 1
                q.append((r, c, nd))


M, N = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(M)]
visited = [[[0] * N for _ in range(M)] for _ in range(4)]
sr, sc, sd = map(int, input().split())
gr, gc, gd = map(int, input().split())
q = collections.deque()
visited[sd - 1][sr - 1][sc - 1] = 1
q.append((sr - 1, sc - 1, sd - 1))
result = float('inf')
bfs()
print(result)
