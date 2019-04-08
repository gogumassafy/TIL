# 후퇴 이동
dr2 = [1, 0, -1, 0]
dc2 = [0, -1, 0, 1]

# 실제 이동
# 서, 북, 남, 동
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


def dfs():
    count = 1
    while stack:
        r, c, d, rotate = stack.pop()
        rotate += 1
        if rotate == 5:
            nr = r + dr2[d]
            nc = c + dc2[d]
        else:
            nr = r + dr[d]
            nc = c + dc[d]
        # 방향 전환 하는거 처리 후에 4 방향 다 돌았다는거 어떻게?
        if not (N > nr >= 0 and M > nc >= 0):
            # 후퇴 했는데 자리가 없을 경우
            if rotate == 5:
                break
            else:
                # 그냥 검사중에 해당 자리가 막혀있을 경우
                stack.append((r, c, (d + 3) % 4, rotate))
                continue
        if raw[nr][nc]:
            if rotate == 5:
                break
            else:
                # 그냥 검사중에 해당 자리가 막혀있을 경우
                stack.append((r, c, (d + 3) % 4, rotate))
                continue
        if visited[nr][nc]:
            if rotate == 5:
                stack.append((nr, nc, d, 0))
                continue
            else:
                stack.append((r, c, (d + 3) % 4, rotate))
                continue
        visited[nr][nc] = 1
        count += 1
        stack.append((nr, nc, (d + 3) % 4, 0))
    return count


N, M = map(int, input().split())
R, C, D = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
stack = []
visited[R][C] = 1
stack.append((R, C, D, 0))
print(dfs())
print()