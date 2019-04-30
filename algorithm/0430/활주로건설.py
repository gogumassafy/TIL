import sys
sys.stdin = open('활주로건설.txt')

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    
    print('#{} {}'.format(tc, result))