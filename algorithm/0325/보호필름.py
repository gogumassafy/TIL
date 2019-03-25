import sys
sys.stdin = open('보호필름.txt')


# def combination(n, k):
#     global count
#     if k == n:
#         print(A)
#         return
#     combination(n, k + 1)
#     A[k] = 1
#     count += 1
#     combination(n, k + 1)
#     A[k] = 0
#     count -= 1

def check():
    global D
    for i in range(D):
        combination(i)


def combination(times):
    global D
    comb = [0 for _ in range(D)]
    for _ in range(times):
        for i in range(D):
    return


# A는 0 B는 1
T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(D)]
    A = [0 for _ in range(D)]
    length = len(A)
    count = 0
    combination(length, 0)



    # for col in range(W):
    #     count = 1
    #     first = raw[0][col]
    #     for row in range(1, D):
    #         if first == raw[row][col]:
    #             count += 1
    #         else:
    #             first = raw[row][col]
    #             count = 1
    #
