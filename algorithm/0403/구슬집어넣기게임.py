import sys, collections
input = sys.stdin.readline


# 5. 이동 시 빨간 구슬과 파란 구슬이 같은 위치로 움직여 부딪히는 경우 구슬이 깨지므로, 게임 실패다.
# 6. 파란구슬이 목표구멍으로 들어가는 것은 게임 실패다.
# 7. 기울임 횟수가 10회를 넘어서면 게임 실패다.

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 비지티드 체크 안함. 어차피 10까지임. 파란 구슬 때문에 전략적으로 돌아가는 경우도 필요.
def bfs():
    time = 0
    while q:
        size = len(q)
        if time > 10:
            return -1
        for _ in range(size):
            pair = q.popleft()
            rr, rc = pair[0][0], pair[0][1]
            br, bc = pair[1][0], pair[1][1]
            if raw[br][bc] == 'H':
                continue
            if raw[rr][rc] == 'H':
                return time
            for i in range(4):
                nrr = rr + dr[i]
                nrc = rc + dc[i]
                if raw[nrr][nrc] == '#':
                    nrr = rr
                    nrc = rc
                nbr = br + dr[i]
                nbc = bc + dc[i]
                if raw[nbr][nbc] == '#':
                    nbr = br
                    nbc = bc
                if visited[0][nrr][nrc] != 0 and visited[0][nrr][nrc] == visited[1][nbr][nbc]:
                    continue
                if nrr == nbr and nrc == nbc:
                    continue
                if nrr == rr and nrc == rc and nbr == br and nbc == bc:
                    continue
                q.append([[nrr, nrc], [nbr, nbc]])
        time += 1
    return -1


T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    raw = [list(input().strip()) for _ in range(R)]
    visited = [[[0] * C for _ in range(R)] for _ in range(2)]
    pair = [[], []]
    q = collections.deque()
    result = float('inf')
    for i in range(R):
        for j in range(C):
            if raw[i][j] == 'B':
                raw[i][j] = '.'
                pair[1] = [i, j]
                visited[1][i][j] = 1
            if raw[i][j] == 'R':
                raw[i][j] = '.'
                pair[0] = [i, j]
                visited[0][i][j] = 1
    q.append(pair)
    print(bfs())
