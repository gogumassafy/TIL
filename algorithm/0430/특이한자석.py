import sys
sys.stdin = open('특이한자석.txt')


def rotate():
    while stack:
        idx, dir = stack.pop()
        visited[idx] = 1
        # 좌
        left = (idx - 1) % 4
        if idx - 1 == left and visited[left] == 0:
            if raw[idx][(pointer[idx] - 2) % 8] != raw[left][(pointer[left] + 2) % 8]:
                stack.append((left, -dir))
        # 우
        right = (idx + 1) % 4
        if idx + 1 == right and visited[right] == 0:
            if raw[idx][(pointer[idx] + 2) % 8] != raw[right][(pointer[right] - 2) % 8]:
                stack.append((right, -dir))
        pointer[idx] = (pointer[idx] - dir) % 8


T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    raw = [list(map(int, input().split())) for _ in range(4)]
    pointer = [0] * 4
    stack = []
    for i in range(K):
        visited = [0] * 4
        idx, dir = map(int, input().split())
        stack.append((idx - 1, dir))
        rotate()
    result = 1*raw[0][pointer[0]] + 2*raw[1][pointer[1]] + 4*raw[2][pointer[2]] + 8*raw[3][pointer[3]]
    print('#{} {}'.format(tc, result))
