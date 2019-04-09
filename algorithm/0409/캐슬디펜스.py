# 거리를 계산해서 dist를 채움
def calc():
    for i in range(3):
    return


def comb(no, start):
    if no == 3:
        print(c)
        return
    for i in range(start, M):
        c.append(i)
        comb(no + 1, i + 1)
        c.pop()


N, M, D = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
dist = [[0] * M for _ in range(N)]
# 궁수의 col idx를 담는데 리스트
c = []
# 결과 값을 담는다.
result = 0
# 적의 총 숫자
enemy = []
for i in range(N):
    for j in range(M):
        if raw[i][j]:
            enemy += 1
comb(0, 0)
print(result)

