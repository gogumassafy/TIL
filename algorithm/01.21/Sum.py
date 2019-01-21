import sys
from pprint import pprint
sys.stdin = open("input_sum.text")

for tc in range(10):
    n = int(input())
    input_list = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        input_list[i] = list(map(int, input().split()))

    #가로 합
    row_sum = 0
    for i in range(99):
        if sum(input_list[i]) > sum(input_list[i+1]):
            row_sum = sum(input_list[i])
        else:
            row_sum = sum(input_list[i+1])

    #세로 합
    col_sum = 0
    for i in range(100):
        each = 0
        for j in range(100):
            each += input_list[j][i]
        if each > col_sum:
            col_sum = each

    #대각선 합
    dia_sum1 = 0
    dia_sum2 = 0
    for i in range(100):
        dia_sum1 += input_list[i][i]
        dia_sum2 += input_list[i][99-i]
    print(row_sum, col_sum, dia_sum2, dia_sum1)
    print(f"#{n} {max(row_sum, col_sum, dia_sum2, dia_sum1)}")