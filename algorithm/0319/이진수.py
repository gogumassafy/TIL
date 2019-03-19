import sys
sys.stdin = open('이진수.txt')


binary_list = [
    '0000',
    '0001',
    '0010',
    '0011',
    '0100',
    '0101',
    '0110',
    '0111',
    '1000',
    '1001',
    '1010',
    '1011',
    '1100',
    '1101',
    '1110',
    '1111',
]


T = int(input())
for tc in range(1, T + 1):
    N, M = input().split()
    binary = ''
    for i in M:
        if i.isalpha():
            idx = ord(i) - ord('A') + 10
        else:
            idx = int(i)
        binary += binary_list[idx]
    print('#{} {}'.format(tc, binary))
