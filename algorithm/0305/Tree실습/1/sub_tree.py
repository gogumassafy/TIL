import sys
sys.stdin = open('input.txt')

def preorder(node):
    cnt = 0
    if node != 0:
        cnt += 1
        cnt += preorder(edge[node][0])
        cnt += preorder(edge[node][1])
    return cnt

T = int(input())

for tc in range(T):
    E, N = map(int, input().split())
    edge = [[0, 0] for _ in range(E+2)]
    input_list = list(map(int, input().split()))
    for i in range(0, len(input_list), 2):
        if edge[input_list[i]][0]:
            edge[input_list[i]][1] = input_list[i+1]
        else:
            edge[input_list[i]][0] = input_list[i + 1]

    print('#{} {}'.format(tc+1, preorder(N)))