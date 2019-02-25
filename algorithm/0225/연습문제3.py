import sys
sys.stdin = open("연습문제3.txt")

def BFS(V):
    que = []
    que.append(V)
    while que:
        v = que.pop(0)
        if not visited[v]:
            visited[v] = 1
            print("-", end="")
            print(v, end="")
        for i in range(0, 2*E, 2):
            if b[i] == v and not visited[b[i+1]]:
                que.append(b[i+1])

if __name__ == "__main__":
    V, E = map(int, input().split())
    b = list(map(int, input().split()))

    visited = [0 for _ in range(V + 1)]

    BFS(1)
