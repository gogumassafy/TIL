import sys
input = sys.stdin.readline
# 12*6의 공간
# R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑. 모두 대문자

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col, color):
    stack = []
    count = 1
    stack.append([row, col, color])
    visited[row][col] = 1
    stack_flag = 1
    while stack_flag:
        stack_flag = 0
        r, c, clr = stack[-1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (12 > nr >= 0 and 6 > nc >= 0):
                continue
            if visited[nr][nc]:
                continue
            if raw[nr][nc] != color:
                continue
            stack.append([nr, nc, color])
            visited[nr][nc] = 1
            count += 1
            stack_flag = 1
    if count >= 4:
        # 카운트가 4 이상일 경우 바로 폭발
        boom(stack)


def boom(stack):
    global global_flag
    for r, c, clr in stack:
        raw[r][c] = '.'
    global_flag = 1


def down():
    for col in range(0, 6):
        for row in range(11, 0, -1):
            first = raw[row][col]
            if first != '.':
                continue
            for row2 in range(row - 1, -1, -1):
                second = raw[row2][col]
                if second == '.':
                    continue
                raw[row][col], raw[row2][col] = second, first
                break


raw = [list(input().strip()) for _ in range(12)]
visited = [[0] * 6 for _ in range(12)]
# 연쇄를 카운트
chain_count = 0
# 한번이라도 폭발이 발생했나 표시하는 플래그
global_flag = 1
while global_flag:
    global_flag = 0
    for row in range(11, -1, -1):
        # if raw[row].count('.') == 6:
        #     break
        for col in range(0, 6):
            if raw[row][col] != '.' and not visited[row][col]:
                dfs(row, col, raw[row][col])
    if global_flag:
        chain_count += 1
        down()
        visited = [[0] * 6 for _ in range(12)]
print(chain_count)
