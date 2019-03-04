import sys
sys.stdin = open("중위순회.txt")

def inorder(node):
    result = ""
    if node != 0:
        result += inorder(firstChild[node])
        result += word[node]
        result += inorder(secondChild[node])
        return result
    return result
for tc in range(10):
    N = int(input())
    firstChild = [0] * (N+1)
    secondChild = [0] * (N + 1)
    word = [""] * (N+1)

    for i in range(N):
        temp = list(input().split())
        addr = int(temp[0])
        char = temp[1]
        word[addr] = char
        if addr * 2 <= N:
            firstChild[addr] = int(temp[2])
            if addr * 2 + 1 <= N:
                secondChild[addr] = int(temp[3])
    print('#{} {}'.format(tc+1, inorder(1)))