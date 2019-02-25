def row(i, j):
    cnt = 0
    while mat[i][j]:
        cnt += 1
        i += 1
    return cnt
def col(i, j):
    cnt = 0
    while mat[i][j]:
        cnt += 1
        j += 1
    return cnt
def zero(i, j, r, c):
    for p in range(r):
        for q in range(c):
            mat[i+p][j+q] = 0
for tc in range(int(input())):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if mat[i][j]:
                r = row(i, j)
                c = col(i, j)
                zero(i, j, r, c)
                result.append((r*c, r, c))
    print(f'#{tc+1}',len(result), *[str(i[1])+' '+str(i[2]) for i in sorted(result)])