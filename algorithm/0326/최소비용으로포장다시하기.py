# 얘는 최대 재귀 회수를 초과하기 때문에 사용안한다.
def perm(n, k, c):
    global min_cost
    if c >= min_cost + raw[0]:
        return
    if n == k:
        min_cost = min(c - raw[0], min_cost)
        return
    else:
        for i in range(k, n):
            raw[i], raw[k] = raw[k], raw[i]
            perm(n, k + 1, c + sum(raw[:k+1]))
            raw[i], raw[k] = raw[k], raw[i]


N = int(input())
raw = list(map(int, input().split()))
min_cost = float('inf')
if N == 1:
    min_cost = raw[0]
else:
    perm(N, 0, 0)
print(min_cost)
