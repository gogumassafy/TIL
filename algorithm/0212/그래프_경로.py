import sys
sys.stdin = open("그래프_경로.txt")
T = int(input())

def DFS(start):
    visit[start] = 1

    if start in node_dict:
        for i in node_dict[start]:
            if visit[i] == 0:
                DFS(i)

for tc in range(T):
    V, E = map(int, input().split())
    node_dict = {}
    visit = [0 for _ in range(V+1)]

    for _ in range(E):
        k,v = map(int, input().split())
        if not k in node_dict:
            node_dict[k] = []
        node_dict[k] += [v]
    S, G = map(int, input().split())
    DFS(S)

    print(f'#{tc+1} {visit[G]}')




