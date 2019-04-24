import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    raw = list(input())
    for i in range(N):
        if raw[i].isdigit():
            raw[i] = int(raw[i])
        else:
            raw[i] = ord(raw[i]) - ord('A') + 10
    rotate = N // 4
    result = set()
    # 회전 돌리는 횟수
    for i in range(0, rotate):
        # 4등분 되어있는거
        for j in range(4):
            each = 0
            # 4등분 안의 자리
            for r in range(rotate):
                each += raw[(j*rotate + r + i) % N] * 16**(rotate - r -1)
            result.add(each)
    result = sorted(list(result), reverse=True)
    print('#{} {}'.format(tc, result[K - 1]))
