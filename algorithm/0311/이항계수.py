def bino2(n, k):
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                b[i][j] = 1
            else:
                b[i][j] = b[i - 1][j - 1] + b[i - 1][j]

    return b[n][k]


b = [[0] * 5 for _ in range(5)]
print(bino2(4, 3))
