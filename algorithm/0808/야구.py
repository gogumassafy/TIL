def dfs(depth):
    global order
    if depth == 9:
        game()
        return
    if depth == 3:
        order.append(0)
        visited[0] = 1
        dfs(depth + 1)
        visited[0] = 0
        order.pop()
    for i in range(1, 9):
        if visited[i]:
            continue
        order.append(i)
        visited[i] = 1
        dfs(depth + 1)
        visited[i] = 0
        order.pop()


def game():
    global N, result
    score = 0
    head = 0
    for i in range(N):
        out = 0
        position = [0] * 4
        while out < 3:
            if raw[i][order[head]] == 0:
                out += 1
            else:
                position[0] = 1
                for j in reversed(range(4)):
                    if position[j]:
                        if j + raw[i][order[head]] > 3:
                            score += 1
                        else:
                            position[j + raw[i][order[head]]] = 1
                        position[j] = 0
            head = (head + 1) % 9
    result = max(result, score)


N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * 9
order = []
result = 0
dfs(0)
print(result)

