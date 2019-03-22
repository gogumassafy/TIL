import sys
sys.stdin = open('보호필름.txt')

# A는 0 B는 1
T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())

