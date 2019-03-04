import sys
sys.stdin = open('공통조상.txt')

def find_parent(node):
    if node != 0:
        parent.append(tree[node][2])
        find_parent(tree[node][2])

def direct(node):
    if node not in parent:
        return direct(tree[node][2])
    return node

def preorder(node):
    cnt = 0
    if node != 0:
        cnt += 1
        cnt += preorder(tree[node][0])
        cnt += preorder(tree[node][1])
    return cnt

T = int(input())

for tc in range(T):
    V, E, V1, V2 = map(int, input().split())
    tree = [[0]*3 for _ in range(V+1)]
    input_list = list(map(int, input().split()))
    parent = []
    for i in range(0, len(input_list), 2):
        if tree[input_list[i]][0]:
            tree[input_list[i]][1] = input_list[i+1]
        else:
            tree[input_list[i]][0] = input_list[i+1]
        tree[input_list[i+1]][2] = input_list[i]

    find_parent(V1)
    DP = direct(V2)

    print('#{} {} {}'.format(tc+1, DP, preorder(DP)))

#1 3 8
#2 1 10
#3 21 35
#4 1 100
#5 168 107
#6 1 500
#7 398 840
#8 747 1359
#9 498 3141
#10 7165 2435
