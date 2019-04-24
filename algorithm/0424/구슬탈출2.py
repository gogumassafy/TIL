import collections

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def BFS():
    while q:
        color, row, col = q.popleft()

        for i in range(4):
            nr = row
            nc = col
            while 
                nr += dr[i]
                nc += dc[i]

    return -1


N, M = map(int, input().split())
raw = [input() for _ in range(M)]
q = collections.deque()

for i in range(N):
    for j in range(M):
        if raw[i][j] == 'O':
            goal = (i, j)
        elif raw[i][j] == 'R':
            q.append(('R', i, j))
        elif raw[i][j] == 'B':
            q.append(('B', i, j))

print(BFS())
