def BFS():
    while queue:
        row, col = queue.pop(0)
        for i in range(4):
            if not raw_data[row + dr[i]][col + dc[i]] and not visited[row + dr[i]][col + dc[i]]:
                queue.append([row + dr[i], col + dc[i]])
                visited[row + dr[i]][col + dc[i]] = visited[row][col] + 1
            elif raw_data[row + dr[i]][col + dc[i]] == 3:
                return visited[row][col]
    return 1


dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
    N = int(input())
    raw_data = [[1]*(N+2)] + [[1] + list(map(int, input())) + [1] for _ in range(N)] + [[1]*(N+2)]
    visited = [[0]*(N+2) for _ in range(N+2)]
    queue = []

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if raw_data[i][j] == 2:
                visited[i][j] = 1
                queue.append([i, j])
                distance = BFS()
    print(distance - 1)

