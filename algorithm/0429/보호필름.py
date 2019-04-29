import sys, time
start_time = time.time()
sys.stdin = open('보호필름.txt')


def comb(n, r, k):
    global D
    if r == n and flag == 0:
        # print(n, selected)
        check()
        return
    elif k == D or flag:
        return
    else:
        selected[k] = 1
        comb(n, r + 1, k + 1)
        selected[k] = 2
        comb(n, r + 1, k + 1)
        selected[k] = 0
        comb(n, r, k + 1)


def check():
    global D, W, K, flag
    init()
    for c in range(W):
        flag = 0
        count = 1
        for r in range(1, D):
            if data[r][c] == data[r - 1][c]:
                count += 1
            else:
                count = 1
            if count == K:
                flag = 1
                break
        if not flag:
            break


def init():
    global W
    for i in range(D):
        data[i] = raw[i][:]
        if selected[i]:
            data[i] = [selected[i] - 1] * W
    return


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(D)]
    data = [[0] * W for _ in range(D)]
    result = 0
    flag = 0
    if K > 1:
        for i in range(D + 1):
            selected = [0] * D
            comb(i, 0, 0)
            if flag:
                result = i
                break
    print('#{} {}'.format(tc, result))
print("--- %s seconds ---" % (time.time() - start_time))

#1 2
#2 0
#3 4
#4 2
#5 2
#6 0
#7 3
#8 2
#9 3
#10 4
