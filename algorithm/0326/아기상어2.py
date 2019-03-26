# https://www.acmicpc.net/problem/16236
import queue

# 행동 규칙
# 아기 상어는 1초에 상하좌우로 인전합 한 칸씩 이동
# 자기 보다 큰 물고기를 먹거나 넘어가기 x
# 자기와 크기가 같은 물고기 먹기 x 넘어가기 o
# 1. 아기 상어는 거리가 가까운 물고기 부터 먹는다.
# 2. 거리가 동일하다면 가장 위에 있는 물고기를 선호함. row가 낮은 애들
# 3. 2. 조건을 만족하는 물고기 중 가장 왼쪽 물고기. col이 낮은 애들
# 즉, 탐색 방향은 위에서 아래로, 왼쪽에서 오른쪾으로 큐에 넣자!
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


def bfs(r, c, w, eat):
    global N, result, order
    q = queue.PriorityQueue()
    raw[r][c] = 0
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    q.put((visited[r][c], r, c, w, eat))
    while not q.empty():
        priority, row, col, weight, count = q.get()
        if 0 < raw[row][col] < weight:
            order += 1
            visited_map[row][col] = order
            count += 1
            raw[row][col] = 0
            if count == weight:
                weight += 1
                count = 0
            result += visited[row][col] - 1
            q.queue.clear()
            visited = [[0] * N for _ in range(N)]
            visited[row][col] = 1

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            if raw[nr][nc] > weight:
                continue
            visited[nr][nc] = visited[row][col] + 1
            q.put((visited[nr][nc], nr, nc, weight, count))



# 처음 아기 상어의 크기는 2
N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
visited_map = [[0] * N for _ in range(N)]
order = 0
result = 0

for i in range(N):
    for j in range(N):
        if raw[i][j] == 9:
            bfs(i, j, 2, 0)
            break
    else:
        continue
    break
print(result)
