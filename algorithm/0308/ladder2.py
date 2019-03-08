import sys
sys.stdin = open('ladder2.txt')

def BFS(r, c):
    queue.append([r, c])
    visited[r][c] = 1
    while queue:
        row, col = queue.pop(0)
        if row == 100:
            return visited[row][col]
        for i in range(3):
            if raw_data[row+dr[i]][col+dc[i]]:
                if not visited[row+dr[i]][col+dc[i]]:
                    queue.append([row+dr[i], col+dc[i]])
                    visited[row+dr[i]][col+dc[i]] = 1 + visited[row][col]
                    break
    return float('inf')


dr = [0, 0, 1]
dc = [-1, 1, 0]


for tc in range(1, 11):
    T = int(input())
    raw_data = [[0] * 102] + [[0] + list(map(int, input().split())) + [0] for _ in range(100)] + [[0] * 102]
    queue = []
    min_distance = float('inf')
    min_idx = 0
    for i in range(1, 101):
        if raw_data[1][i]:
            visited = [[0] * 102 for _ in range(102)]
            distance = BFS(1, i)
            if min_distance > distance:
                min_distance = distance
                min_idx = i
    print('#{} {}'.format(T, min_idx - 1))

# 1 18
# 2 96
# 3 16
# 4 5
# 5 99
# 6 0
# 7 97
# 8 0
# 9 62
# 10 3
