import sys
sys.stdin = open('input.txt')


def postorder(node):
    global N
    if node <= N:
        if tree[node]:
            return tree[node]
        a = postorder(2*node)
        b = postorder(2*node+1)
        tree[node] = a + b
        return tree[node]
    return 0


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value
    print('#{} {}'.format(tc, postorder(L)))