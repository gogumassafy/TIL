import sys
sys.stdin = open("작업순서.txt")

T = 10

def DFS(start):
    global visited
    visit[start] = 1
    print(start, end=" ")

    if start in node_dict:
        for i in node_dict[start]:
            if visit[i] == 0:
                DFS(i)

for tc in range(T):
    V, E = map(int, input().split())
    input_E = list(map(int, input().split()))
    start = set(input_E[0::2])
    goal = set(input_E[1::2])
    start -= goal

    node_dict = {}
    pre_dict = {}
    visit = [0 for _ in range(V+1)]
    visited = []

    for i in range(0, 2*E, 2):
        k = input_E[i]
        v = input_E[i+1]
        if not k in node_dict:
            node_dict[k] = []
        node_dict[k] += [v]
        if not v in pre_dict:
            pre_dict[v] = []
        pre_dict[v] += [k]

    print(f'#{tc + 1}', end=" ")
    for i in start:
        if visit[i] == 0:
            DFS(i)
    print()