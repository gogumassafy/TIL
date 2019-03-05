import sys
sys.stdin = open('사칙연산_input.txt')


def postorder(node):
    if operator[node]:
        a = postorder(left_child[node])
        b = postorder(right_child[node])
        if operator[node] == '+':
            return a + b
        elif operator[node] == '-':
            return a - b
        elif operator[node] == '*':
            return a * b
        else:
            return a / b
    return num_list[node]


for tc in range(1, 11):
    N = int(input())
    operator = [''] * (N + 1)
    num_list = [0] * (N + 1)
    left_child = [0] * (N + 1)
    right_child = [0] * (N + 1)

    for i in range(N):
        temp = list(input().split())
        addr = int(temp[0])
        if len(temp) == 4:
            left_child[addr] = int(temp[2])
            right_child[addr] = int(temp[3])
            operator[addr] = temp[1]
        else:
            num_list[addr] = int(temp[1])
    print('#{} {}'.format(tc, int(postorder(1))))