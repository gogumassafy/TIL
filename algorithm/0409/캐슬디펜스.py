# 거리를 계산해서 dist를 채움
def calc():
    for a in range(3):
        for e in range(len(enemy)):
            dist[a][e] = [abs(N - enemy[e][0]) + abs(c[a] - enemy[e][1]), enemy[e][0], enemy[e][1]]


def down():
    global enemy_count
    while enemy_count:
        for a in range(3):
            for e in range(len(dist[a])):
                if dist[a][e][1] > 0:
                    dist[a][e][0] -= 1
                    dist[a][e][1] -= 1
                    # if dist[a][e][1] == 0:
                    #     enemy_count -= 1


def comb(no, start):
    if no == 3:
        # print(c)
        calc()
        down()
        return
    for i in range(start, M):
        c.append(i)
        comb(no + 1, i + 1)
        c.pop()


N, M, D = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
# 궁수의 col idx를 담는데 리스트
c = []
# 결과 값을 담는다.
result = 0
# 적들의 좌표
# r, c
enemy = []
enemy_count = 0
for i in range(N):
    for j in range(M):
        if raw[i][j]:
            enemy.append((i, j))
            enemy_count += 1
dist = [[float('inf')] * len(enemy) for _ in range(3)]
comb(0, 0)
print(result)

