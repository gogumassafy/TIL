def init():

    return


R, C, T = map(int, input().split())
raw = [list(map(int,input().split())) for _ in range(R)]
for i in range(2, R - 2):
    if raw[i][0] == -1:
        cleaner = [(i, 0), (i + 1, 0)]
        break
init()
