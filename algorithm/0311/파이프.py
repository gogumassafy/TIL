import time, sys
start_time = time.time()
sys.stdin = open('파이프.txt')


def DFS(r, c, d):
    global N, cnt
    stack.append([r, c, d])
    while stack:
        row, col, direction = stack.pop()
        for i in range(3):
            nr = row + dr[i]
            nc = col + dc[i]
            if not table[nr][nc]:
                if direction != 2 and i != 2 and direction != i:
                    continue
                if i == 2 and conner(nr, nc):
                    continue
                if nr == N and nc == N and not table[nr][nc]:
                    cnt += 1
                    break
                stack.append([nr, nc, i])


def conner(r, c):
    if table[r-1][c] or table[r][c-1]:
        return True
    return False


# 우 하 우하
dr = [0, 1, 1]
dc = [1, 0, 1]
N = int(input())
cnt = 0
stack = []
table = [[1] * (N+2)]
table += [[1] + list(map(int, input().split())) + [1] for _ in range(N)]
table += [[1] * (N+2)]
DFS(1, 2, 0)
print(cnt)
print("--- %s seconds ---" %(time.time() - start_time))
