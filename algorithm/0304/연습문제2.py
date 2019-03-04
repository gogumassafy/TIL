import sys
sys.stdin = open('연습문제1.txt')

def preorder(node):
    if node != 0:
        print('{}'.format(node), end=" ")
        preorder(result[node][1])
        preorder(result[node][2])

def inorder(node):
    if node != 0:
        inorder(result[node][1])
        print('{}'.format(node), end=" ")
        inorder(result[node][2])

def postorder(node):
    if node != 0:
        postorder(result[node][1])
        postorder(result[node][2])
        print('{}'.format(node), end=" ")

n, e = map(int, input().split())
input_list = list(map(int, input().split()))
result = [[i,0,0,0] for i in range(n+1)]

for i in range(0, len(input_list), 2):
    if result[input_list[i]][1]:
        result[input_list[i]][2] = input_list[i+1]
    else:
        result[input_list[i]][1] = input_list[i+1]
    result[input_list[i+1]][3] = input_list[i]

print("\n".join("{0:3d} {1:3d} {2:3d} {3:3d}".format(*result[i]) for i in range(1, len(result))))
preorder(1)
print()
inorder(1)
print()
postorder(1)