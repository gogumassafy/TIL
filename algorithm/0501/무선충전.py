import sys
sys.stdin = open('무선충전.txt')


dr = (0, -1, 0, 1, 0)
dc = (0, 0, 1, 0, -1)


def draw(idx, r, c, C, p):
    count = 0
    for i in range(r - C, r + C + 1):
        for j in range(c - count, c + count + 1):
            if not (10 > i >= 0):
                break
            if not (10 > j >= 0):
                continue
            data[idx][i][j] = p
        if i < r:
            count += 1
        else:
            count -= 1


T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    direction = [list(map(int, input().split())) + [0] for _ in range(2)]
    data = [[[0] * 10 for _ in range(10)] for _ in range(A)]
    people = [[0, 0], [9, 9]]
    result = 0
    for i in range(A):
        c, r, C, p = map(int, input().split())
        draw(i, r - 1, c - 1, C, p)

    for i in range(M + 1):
        selected = [0] * A
        for j in range(2):
            if j == 0:
                idx = 0
                for k in range(1, A):
                    if data[k][people[j][0]][people[j][1]] > data[idx][people[j][0]][people[j][1]]:
                        idx = k
                num = data[idx][people[j][0]][people[j][1]]
                if num:
                    selected[idx] = 1
                    result += num
            else:
                num = 0
                for k in range(0, A):
                    if selected[k]:
                        continue
                    if data[k][people[j][0]][people[j][1]] > num:
                        idx = k
                        num = data[k][people[j][0]][people[j][1]]
                result += num

            # 방향 전환
            people[j][0] += dr[direction[j][i]]
            people[j][1] += dc[direction[j][i]]
    print('#{} {}'.format(tc, result))
