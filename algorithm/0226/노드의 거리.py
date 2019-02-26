import sys
sys.stdin = open('노드의_거리.txt')

def BFS(start, end):
    queue.append(start)
    visited[start] = 1
    while queue:
        v = queue.pop(0)
        for i in range(V+1):
            if not visited[i] and input_list[v][i] == 1:
                queue.append(i)
                visited[i] = visited[v] + 1
                if i == end:
                    return visited[i]
    return 1
T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    input_list = [[0] * (V+1) for _ in range(V+1)]
    queue = []
    visited = [0] * (V+1)
    for _ in range(E):
        k, v = map(int, input().split())
        input_list[k][v] = 1
        input_list[v][k] = 1
    start, end = map(int, input().split())
    print(f'#{tc+1} {BFS(start, end) -1}')