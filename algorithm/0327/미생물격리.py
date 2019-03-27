import queue


# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global N, M
    time = 0
    while not q.empty():
        t = time % 2
        nt = (t + 1) % 2
        if time == M:
            sum_num = 0
            while not q.empty():
                r, c = q.get()
                sum_num += raw[r][c][t][0]
            return sum_num
        size = q.qsize()
        for i in range(size, 0, -1):
            r, c = q.get()
            after = raw[r][c][t][0]
            before = raw[r][c][t][1]
            d = raw[r][c][t][2]
            nr = r + dr[d]
            nc = c + dc[d]
        # 합체 고려 X, 기존 위치 삭제 아직
            # 약품지역에 도달했을 경우
            if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
                # 몸뚱이 고쳐줌.
                after //= 2
                before = after
                # 방향을 반대로 바꿔줌
                if d == 0 or d == 2:
                    d += 1
                else:
                    d -= 1
            if raw[nr][nc][(t + 1) % 2]:
                after += raw[nr][nc][(t + 1) % 2][0]
                before = max(before, raw[nr][nc][(t + 1) % 2][1])
                if before < raw[nr][nc][nt][1]:
                    before = raw[nr][nc][nt][1]
                    d = raw[nr][nc][nt][2]
            else:
                q.put((nr, nc))
            raw[r][c][t] = [0, 0, 0]
            raw[nr][nc][nt] = [after, before, d]
        time += 1


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    # [r][c][t]
    raw = [[[[0, 0, 0] for _ in range(2)] for _ in range(N)] for _ in range(N)]
    q = queue.Queue()
    for _ in range(K):
        R, C, G, D = map(int, input().split())
        raw[R][C][0] = [G, G, D - 1]
        q.put((R, C))
    print(bfs())
