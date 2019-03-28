# 신맛은 재료 각각의 신맛 정도의 곱
# 쓴맛의 정도는 각각의 합
# 둘의 차가 적을수록 맛있다.


def comb(n, r, sour, bitter):
    global result, count
    if n == r:
        if count <= 0:
            return
        result = min(result, abs(sour - bitter))
        return
    count += 1
    comb(n, r + 1, sour * gre[r][0], bitter + gre[r][1])
    count -= 1
    comb(n, r + 1, sour, bitter)


N = int(input())
gre = []
for i in range(N):
    S, B = map(int, input().split())
    gre.append((S, B))
result = float('inf')
count = 0
comb(len(gre), 0, 1, 0)
print(result)

