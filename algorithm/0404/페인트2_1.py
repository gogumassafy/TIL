import sys
import collections
input = sys.stdin.readline


def calc1(r, c):
    global K
    cnt = 0
    for i in range(K + 1):
        if not N > r - i >= 0:
            continue
        for j in range(-(K - i), K - i + 1):
            if not N > c + j >= 0:
                continue
            if not raw[r - i][c + j] and not visited[r - i][c + j]:
                visited[r - i][c + j] = 1
                cnt += 1
    for i in range(1, K + 1):
        if not N > r + i >= 0:
            continue
        for j in range(-(K - i), K - i + 1):
            if not N > c + j >= 0:
                continue
            if not raw[r + i][c + j] and not visited[r + i][c + j]:
                visited[r + i][c + j] = 1
                cnt += 1
    return cnt


def calc2(r, c):
    global K
    cnt = 0
    for i in range(K + 1):
        if not N > r - i >= 0:
            continue
        for j in range(-(K - i), K - i + 1):
            if not N > c + j >= 0:
                continue
            if not raw[r - i][c + j] and not visited[r - i][c + j]:
                cnt += 1
    for i in range(1, K + 1):
        if not N > r + i >= 0:
            continue
        for j in range(-(K - i), K - i + 1):
            if not N > c + j >= 0:
                continue
            if not raw[r + i][c + j] and not visited[r + i][c + j]:
                cnt += 1
    return cnt


N = int(input())
K = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
q = collections.deque()
result = 0
for r1 in range(N):
    for c1 in range(N):
        visited = [[0] * N for _ in range(N)]
        count1 = calc1(r1, c1)
        for r2 in range(r1, N):
            for c2 in range(N):
                count2 = calc2(r2, c2)
                result = max(result, count1 + count2)
print(result)
