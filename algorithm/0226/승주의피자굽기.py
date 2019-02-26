import sys
sys.stdin = open('피자굽기_input.txt')
T = int(input())

def ans():
    N, M = map(int,input().split())
    pizzas = list(map(int, input().split()))
    Q = []
    visited = [0]*M
    index = 0

    Q.append([index,pizzas[index]])
    index += 1

    p = []
    while 0 in visited:
        while len(Q) < N and index < M:
            Q.append([index, pizzas[index]])
            index += 1
        for i in range(0, len(Q)):
            if Q[i] != 0:
                Q[i][1] = Q[i][1] // 2
                if Q[i][1] == 0:
                    p.append(i)
        for j in p:
            if visited.count(0) != 1:
                visited[Q[j][0]] = 1
                if index < M:
                    Q[j] = [index, pizzas[index]]
                    index += 1
                else:
                    Q[j] = 0
            else:
                return Q[j][0]+1
        p = []
for tc in range(T):
    print(f'#{tc+1} {ans()}')