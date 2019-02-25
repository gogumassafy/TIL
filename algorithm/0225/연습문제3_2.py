import sys
sys.stdin = open("연습문제3.txt")

def BFS(V):
    que = []
    que.append(V)
    # visited[V] = 1
    while que:
        v = que.pop(0)
        print(v, end =" ")
        for i in range(0, 2*E, 2):
            if b[i] == v and not visited[b[i+1]]:
                visited[b[i+1]] = visited[v] + 1
                que.append(b[i+1])
    print()
    print(f'최대 간선 길이: {max(visited)}')

if __name__ == "__main__":
    V, E = map(int, input().split())
    b = list(map(int, input().split()))

    visited = [0 for _ in range(V + 1)]

    BFS(1)
