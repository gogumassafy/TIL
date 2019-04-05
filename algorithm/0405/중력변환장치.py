import sys
import collections
input = sys.stdin.readline

d = (1, -1)


def bfs():
    global N, M, result
    while q:
        dirr, cnt, r, c = q.popleft()
        if cnt >= result:
            continue
        if raw[r][c] == 'D':
            result = min(result, cnt)
            continue
        # dirr 방향대로 끝 없이 하강
        if raw[r + d[dirr]][c] != '#':
            while 1:
                if dirr:
                    if not r > 0:
                        break
                else:
                    if not N -1 > r:
                        break
                if raw[r + d[dirr]][c] != '#':
                    r += d[dirr]
                    if raw[r][c] == 'D':
                        result = min(result, cnt)
                        continue
                else:
                    if visited[r][c] <= cnt:
                        break
                    visited[r][c] = cnt
                    q.append((dirr, cnt, r, c))
                    break
        else:
            # 하강하고 나서 좌, 우로 움직임.
            for i in range(2):
                nc = c + d[i]
                if not (M > nc >= 0):
                    continue
                if raw[r][nc] == '#':
                    continue
                if visited[r][nc] <= cnt:
                    continue
                # 방향과 카운트 정보 수정된거 체크하기
                visited[r][nc] = cnt
                q.append((dirr, cnt, r, nc))
            # 중력 전환
            q.append(((dirr + 1) % 2, cnt + 1, r, c))


N, M = map(int, input().split())
raw = [list(input().strip()) for _ in range(N)]
visited = [[float('inf')] * M for _ in range(N)]
q = collections.deque()
result = float('inf')
for i in range(N):
    for j in range(M):
        if raw[i][j] == 'C':
            visited[i][j] = 0
            q.append((0, 0, i, j))
        if raw[i][j] == 'D':
            gr, gc = i, j
bfs()
print(result if result != float('inf') else -1)
