import sys
sys.stdin = open("작업순서.txt")

def DFS(start):
    visit[start] = 1
    print(start, end=" ")

    if start in node_dict:
        for i in node_dict[start]:
            pre_dict[i].remove(start)
            if visit[i] == 0 and not pre_dict.get(i, False):
                DFS(i)

for tc in range(10):
    V, E = map(int, input().split())
    input_E = list(map(int, input().split()))
    start = set(range(1, V+1))
    goal = set(input_E[1::2])
    start -= goal

    node_dict, pre_dict = {}
    visit = [0 for _ in range(V+1)]

    for i in range(0, 2*E, 2):
        k = input_E[i]
        v = input_E[i+1]
        if k not in node_dict:
            node_dict[k] = []
        node_dict[k] += [v]
        if v not in pre_dict:
            pre_dict[v] = []
        pre_dict[v] += [k]

    print(f'#{tc + 1}', end=" ")
    for i in start:
        if visit[i] == 0:
            DFS(i)
    print()