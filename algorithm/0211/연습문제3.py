# input값: 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# 받는 방법: 1. 인접행렬
#           2. 인접정점리스트
#           3. 간선배열


def DFS(start):
    visit[start] = 1
    print(start, end="")

    for i in range(1, len(node_list[start])):
        if node_list[start][i] == 1 and visit[i] == 0:
            print("-", end="")
            DFS(i)

N, M = map(int, input().split())
N += 1
node_list = [[0 for _ in range(N)] for _ in range(N)]
input_list = list(map(int, input().split()))

for i in range(0, 2*M, 2):
    node_list[input_list[i]][input_list[i+1]] = 1
    node_list[input_list[i + 1]][input_list[i]] = 1

for i in range(1, N):
    print(f'{i} {node_list[i][1:]}')
visit = [0 for _ in range(N)]
DFS(1)