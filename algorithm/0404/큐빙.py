T = int(input())
cube = [['w'] * 9, ['r'] * 9, ['y'] * 9, ['o'] * 9, ['g'] * 9, ['b'] * 9]
# print(cube)
for tc in range(1, T + 1):
    N = int(input())
    # U윗, D아래, F앞, B뒷, L왼, R오
    rotate = list(input().split())
    print(rotate[0][0], rotate[0][1])
    print()