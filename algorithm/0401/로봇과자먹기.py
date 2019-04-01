def perm(n, k, total):
    global N, result
    if total >= result:
        return
    if n == k:
        result = min(result, total)
        return
    for i in range(N):
        if check[i]:
            continue
        check[i] = 1
        perm(n, k + 1, total + distant[k][i])
        check[i] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    cookies = list(map(int, input().split()))
    robots = list(map(int, input().split()))
    cookie = []
    robot = []
    check = [0] * N
    result = float('inf')
    for i in range(0, len(cookies), 2):
        cookie.append((cookies[i], cookies[i + 1]))
        robot.append((robots[i], robots[i + 1]))
    distant = [[0] * N for _ in range(N)]
    # i는 로봇을 의미 j는 과자를 의미
    for i in range(N):
        for j in range(N):
            distant[i][j] = abs(robot[i][0] - cookie[j][0]) + abs(robot[i][1] - cookie[j][1])
    perm(N, 0, 0)
    print(result)



