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
    for i in range(100):
        row_sum = row_sum if row_sum > sum(input_list[i]) else sum(input_list[i])

    #세로 합
    col_sum = 0
    for i in range(100):
        each = 0
        for j in range(100):
            each += input_list[j][i]
        if each > col_sum:
            col_sum = each

    # for i in range(100):
    #     each = 0
    #     each = sum([input_list[j][i] for j in range(100)])
    #     if each > col_sum:
    #         col_sum = each

    #대각선 합
    dia_sum1 = 0
    dia_sum2 = 0
    # dia_sum1 = sum([input_list[i][i] for i in range(100)])
    # dia_sum2 = sum([input_list[i][99-i] for i in range(100)])

    for i in range(100):
        dia_sum1 += input_list[i][i]
        dia_sum2 += input_list[i][99-i]
    print(f"#{n} {max(row_sum, col_sum, dia_sum2, dia_sum1)}")