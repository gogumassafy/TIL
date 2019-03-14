# 이 코드는 중복으로 세는 문제가 발생함.
def pair():
    finished = True
    for i in paired:
        if not i:
            finished = False
            break
    if finished:
        return 1
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not (paired[i] or paired[j]) and areFriends[i][j]:
                paired[i], paired[j] = 1, 1
                cnt += pair()
                paired[i], paired[j] = 0, 0
    return cnt


# 중복은 안세는 코드
def pair2():
    firstOne = -1
    for i in range(n):
        if not paired[i]:
            firstOne = i
            break

    if firstOne == -1:
        return True

    cnt = 0
    for i in range(firstOne + 1, n):
        if not paired[i] and areFriends[firstOne][i]:
            paired[firstOne] = paired[i] = 1
            cnt += pair2()
            paired[firstOne] = paired[i] = 0
    return cnt


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    raw = list(map(int, input().split()))
    areFriends = [[0] * n for _ in range(n)]
    paired = [0] * n
    for i in range(0, 2*m, 2):
        areFriends[raw[i]][raw[i+1]] = 1
        areFriends[raw[i + 1]][raw[i]] = 1
    print(pair())
    print(pair2())
