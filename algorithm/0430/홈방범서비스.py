import sys, collections
sys.stdin = open('홈방범서비스.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def DFS(cnt):
    global N, M, result

    for k in range(1, len(K)):
        if cnt * M >= K[k]:
            result = max(result, cnt)

        time = len(stack)
        for t in range(time):
            r, c = stack.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (N > nr >= 0 and N > nc >= 0):
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = 1
                if raw[nr][nc]:
                    cnt += 1
                stack.append((nr, nc))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    stack = collections.deque()
    K = [0]
    count = 0
    for i in range(N):
        for j in range(N):
            if raw[i][j]:
                count += 1
    earn = count * M
    k = 0
    while 1:
        k += 1
        cost = k**2+(k-1)**2
        K.append(cost)
        if cost > earn:
            break

    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            stack.append((i, j))
            visited[i][j] = 1
            cnt = 0
            if raw[i][j]:
                cnt += 1
            DFS(cnt)
            stack.clear()
    print('#{} {}'.format(tc, result))

#1 5
#2 4
#3 24 o
#4 48
#5 3
#6 65 o
#7 22
#8 22
#9 78 o
#10 400 o