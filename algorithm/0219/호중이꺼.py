import sys
sys.stdin = open("미로.txt")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data_total = [[0 for _ in range(N)] for _ in range(N)]  # 5~27 데이터 받아오기
    # data_total = [list(map(int, input())) for i in range(N)]

    data = []
    miro = []
    result = 0
    a,b = 0,0
    for i in range(N):
        data.extend(list(map(str, input().split())))
    # print(data)
    for j in range(N):
        for k in range(N):
            data_total[j][k] = int(data[j][k])
    print(data_total)
    for l in range(len(data_total)):
        if 2 in data_total[l]:
            a, b = l, data_total[l].index(2)
    # print(a,b)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    re_a = a
    re_b = b # dx dy 카운트변수




    while data_total[a][b] != 3:
        if a == 4 and b == 4:
            if data_total[a - 1][b] == 0:
                a = a - 1
            elif data_total[a][b - 1] == 0:
                b = b - 1
            else:
                a, b = re_a, re_b
        if data_total[a][b] == 2:
            for l in range(len(dx)):
                if data_total[a + dy[l]][b + dx[l]] == 0 and a + dy[l] >= 0 and b + dx[l] >= 0 and a + dy[l] < 5 and b + \
                        dx[l] < 5:
                    data_total[a][b] = 2  # 시작점 구분
                    a = a + dy[l]
                    b = b + dx[l]
                    l = 0
                    break
            if l == 3:
                print(f"#{tc} 0")
                break
        elif data_total[a][b] == 0:
            for l in range(len(dx)):
                if data_total[a + dy[l]][b + dx[l]] == 0 and a + dy[l] >= 0 and b + dx[l] >= 0 and a + dy[l] < 5 and b + \
                        dx[l] < 5:
                    data_total[a][b] = 9  # 방문
                    a = a + dy[l]
                    b = b + dx[l]
                    l = 0
                    break
                if data_total[a + dy[l]][b + dx[l]] == 3 and a + dy[l] >= 0 and b + dx[l] >= 0 and a + dy[l] < 5 and b + \
                        dx[l] < 5:
                    data_total[a][b] = 9
                    a = a + dy[l]
                    b = b + dx[l]
                    l = 0
                    break

            else:
                a, b = re_a, re_b
                for m in range(len(dx)):
                    if data_total[a + dy[m]][b + dx[m]] != 0 and l == len(dx) - 1 and a + dy[l] >= 0 and b + dx[
                        l] >= 0 and a + dy[l] < 5 and b + \
                            dx[l] < 5:
                        result = 0
                    else:
                        break

                    a = a + dy[l]
                    b = b + dx[l]
                    l = 0
        if data_total[a][b] == 3:
            print(f"#{tc} 1")