import sys
sys.stdin = open('보물상자 비밀번호.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    input_string = input()
    head = 0
    result = []
    each_part = len(input_string) // 4
    for i in range(each_part):
        for j in range(4):