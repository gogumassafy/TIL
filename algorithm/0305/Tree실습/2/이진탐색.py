import sys
sys.stdin = open('input.txt')

def binary_tree_make(idx):
    global cnt
    if idx <= N:
        binary_tree_make(idx*2)
        binary_tree[idx] = cnt
        cnt += 1
        binary_tree_make(idx*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    binary_tree = [0] * (N + 1)
    cnt = 1
    binary_tree_make(1)
    print('#{} {} {}'.format(tc, binary_tree[1], binary_tree[N//2]))