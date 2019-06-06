import itertools
import sys
sys.stdin = open('캐슬디펜스.txt')

def down():
    pass


def kill():
    pass


def 


N, M, D = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)] + [[0] * M]
result = 0
position = [i for i in range(M)]
archer = list(itertools.combinations(position, 3))

for p in archer:
    pass
print(result)